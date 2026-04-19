import time
import argparse
import numpy as np
import onnxruntime as ort


def make_session(model_path, intra_threads=1, inter_threads=1):
    so = ort.SessionOptions()
    so.intra_op_num_threads = intra_threads
    so.inter_op_num_threads = inter_threads
    so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
    return ort.InferenceSession(model_path, sess_options=so, providers=['CPUExecutionProvider'])


def run_once(sess, input_ids):
    inp = np.array([input_ids], dtype=np.int64)
    out = sess.run(None, {'input_ids': inp})[0]
    return out[0]


def measure_generation(sess, prompt_ids, gen_tokens=16, runs=5, sample=False):
    times = []
    for _ in range(runs):
        start = time.time()
        ids = list(prompt_ids)
        for _ in range(gen_tokens):
            logits_all = run_once(sess, ids)
            last_logits = logits_all[-1]
            if sample:
                probs = np.exp(last_logits - np.max(last_logits))
                probs = probs / probs.sum()
                next_id = int(np.random.choice(len(probs), p=probs))
            else:
                next_id = int(np.argmax(last_logits))
            ids.append(next_id)
        times.append(time.time() - start)
    return sum(times) / len(times)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('fp32')
    p.add_argument('--quant', default=None, help='Path to quantized ONNX (optional)')
    p.add_argument('--prompt', default='Hello world')
    p.add_argument('--runs', type=int, default=5)
    p.add_argument('--gen', type=int, default=16)
    p.add_argument('--intra', type=int, default=1)
    p.add_argument('--inter', type=int, default=1)
    args = p.parse_args()

    print('Loading FP32 ONNX:', args.fp32)
    sess_fp32 = make_session(args.fp32, intra_threads=args.intra, inter_threads=args.inter)
    prompt_ids = [abs(hash(t)) % 50257 for t in args.prompt.strip().split()]
    t_fp32 = measure_generation(sess_fp32, prompt_ids, gen_tokens=args.gen, runs=args.runs)
    print(f'FP32 avg generation time ({args.runs} runs, {args.gen} tokens): {t_fp32:.4f}s')

    if args.quant:
        print('Loading quantized ONNX:', args.quant)
        sess_q = make_session(args.quant, intra_threads=args.intra, inter_threads=args.inter)
        t_q = measure_generation(sess_q, prompt_ids, gen_tokens=args.gen, runs=args.runs)
        print(f'Quant INT8 avg generation time ({args.runs} runs, {args.gen} tokens): {t_q:.4f}s')
        print('Speedup:', t_fp32 / t_q if t_q>0 else float('inf'))
