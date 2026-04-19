import argparse
import numpy as np
import onnxruntime as ort
from lightgpt.model import LightGPT


def make_session(model_path, intra_threads=1, inter_threads=1, opt_level=99):
    so = ort.SessionOptions()
    so.intra_op_num_threads = intra_threads
    so.inter_op_num_threads = inter_threads
    # Extended optimizations
    so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_EXTENDED
    # enable all useful runtime options
    sess = ort.InferenceSession(model_path, sess_options=so, providers=['CPUExecutionProvider'])
    return sess


def run_session(sess, input_ids):
    # input_ids: list[int]
    inp = np.array([input_ids], dtype=np.int64)
    out = sess.run(None, {'input_ids': inp})[0]
    # out shape: (1, T, vocab)
    return out[0]


def generate_onnx(sess, prompt_ids, max_new_tokens=16, temperature=1.0, sample=False):
    ids = list(prompt_ids)
    for _ in range(max_new_tokens):
        logits_all = run_session(sess, ids)
        last_logits = logits_all[-1]
        if sample:
            probs = np.exp(last_logits - np.max(last_logits))
            probs = probs / probs.sum()
            next_id = int(np.random.choice(len(probs), p=probs))
        else:
            next_id = int(np.argmax(last_logits))
        ids.append(next_id)
    return ids


def main():
    p = argparse.ArgumentParser()
    p.add_argument('model')
    p.add_argument('--prompt', default='Hello world')
    p.add_argument('--mode', choices=['fp32','quant'], default='fp32')
    p.add_argument('--intra', type=int, default=1)
    p.add_argument('--inter', type=int, default=1)
    p.add_argument('--sample', action='store_true')
    args = p.parse_args()

    model_path = args.model
    sess = make_session(model_path, intra_threads=args.intra, inter_threads=args.inter)

    # simple tokenizer like model
    ids = LightGPT.small_vocab_tokenize(args.prompt)
    out_ids = generate_onnx(sess, ids, max_new_tokens=16, temperature=1.0, sample=args.sample)
    print('Input ids:', ids)
    print('Output ids:', out_ids)

if __name__ == '__main__':
    main()
