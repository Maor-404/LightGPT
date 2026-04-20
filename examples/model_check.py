import argparse
import time
from lightgpt import LightGPT
from lightgpt.infer import generate
from lightgpt.tiny_runtime import TinyLightGPT
import os

# ONNX runner imported inline to avoid heavy dependencies when not using ONNX
try:
    import onnxruntime as ort
    import numpy as np
    ONNX_AVAILABLE = True
except Exception:
    ONNX_AVAILABLE = False


def onnx_generate(model_path, prompt_ids, max_new_tokens=16, sample=False, intra=1, inter=1):
    if not ONNX_AVAILABLE:
        return '(onnxruntime not available)'
    so = ort.SessionOptions()
    so.intra_op_num_threads = intra
    so.inter_op_num_threads = inter
    so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
    sess = ort.InferenceSession(model_path, sess_options=so, providers=['CPUExecutionProvider'])
    ids = list(prompt_ids)
    for _ in range(max_new_tokens):
        inp = np.array([ids], dtype=np.int64)
        out = sess.run(None, {'input_ids': inp})[0]
        last = out[0][-1]
        if sample:
            probs = np.exp(last - np.max(last))
            probs = probs / probs.sum()
            next_id = int(np.random.choice(len(probs), p=probs))
        else:
            next_id = int(np.argmax(last))
        ids.append(next_id)
    return ids


CHECK_PROMPTS = {
    'conversation': 'User: Hi, how are you?\nAssistant:',
    'questionnaire': 'Please list three benefits of aerobic exercise in brief bullet points:',
    'philosophical': 'Is free will compatible with determinism? Discuss briefly in a thoughtful style.'
}


def run_pytorch_check(mode, prompt, max_new_tokens=32):
    model = LightGPT(mode=mode, max_seq_len=128)
    model.eval()
    ids = model.small_vocab_tokenize(prompt)
    out_ids = generate(model, ids, max_new_tokens=max_new_tokens, temperature=1.0, device='cpu', sample=False)
    return out_ids


def run_tiny_check(npz_path, prompt, max_new_tokens=16):
    rt = TinyLightGPT(npz_path)
    ids = LightGPT.small_vocab_tokenize(prompt)
    out_ids = rt.generate(ids, max_new_tokens=max_new_tokens)
    return out_ids


def ids_to_text(ids):
    # very small reverse mapping using hash mod -> placeholder tokens
    return ' '.join([f'TOK{str(i)}' for i in ids[:50]])


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', default='model_check_report.txt')
    p.add_argument('--onnx', default=None, help='Path to ONNX model (optional)')
    p.add_argument('--npz', default=None, help='Path to NPZ weights for tiny runtime (optional)')
    p.add_argument('--mode', choices=['overkill','normal','underkill'], default='normal')
    args = p.parse_args()

    report = []
    report.append('LightGPT model check report')
    report.append(f'Mode: {args.mode}')
    report.append('')

    for name, prompt in CHECK_PROMPTS.items():
        report.append('---')
        report.append(f'Check: {name}')
        report.append(f'Prompt: {prompt}')

        # PyTorch quick check
        try:
            out_ids = run_pytorch_check(args.mode, prompt, max_new_tokens=24)
            report.append('PyTorch output ids: ' + str(out_ids[:30]))
            report.append('PyTorch output (tokens): ' + ids_to_text(out_ids[:30]))
        except Exception as e:
            report.append('PyTorch run failed: ' + str(e))

        # ONNX check
        if args.onnx:
            try:
                onnx_out = onnx_generate(args.onnx, LightGPT.small_vocab_tokenize(prompt), max_new_tokens=24)
                report.append('ONNX output ids: ' + str(onnx_out[:30]))
                report.append('ONNX output (tokens): ' + ids_to_text(onnx_out[:30]))
            except Exception as e:
                report.append('ONNX run failed: ' + str(e))
        else:
            report.append('ONNX: not provided')

        # Tiny runtime check
        if args.npz:
            try:
                tiny_out = run_tiny_check(args.npz, prompt, max_new_tokens=16)
                report.append('Tiny runtime output ids: ' + str(tiny_out[:30]))
                report.append('Tiny runtime output (tokens): ' + ids_to_text(tiny_out[:30]))
            except Exception as e:
                report.append('Tiny runtime failed: ' + str(e))
        else:
            report.append('Tiny runtime: npz not provided')

        report.append('')

    with open(args.out, 'w') as f:
        f.write('\n'.join(report))

    print('Report written to', args.out)
