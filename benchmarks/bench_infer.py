import time
import numpy as np
from lightgpt.tiny_runtime import TinyLightGPT


def bench(npz_path, runs=5, seq_len=16):
    rt = TinyLightGPT(npz_path)
    prompt = [0] * seq_len
    # warmup
    rt.generate(prompt, max_new_tokens=4)
    times = []
    for _ in range(runs):
        t0 = time.time()
        rt.generate(prompt, max_new_tokens=8)
        times.append(time.time()-t0)
    print('Avg generation time:', sum(times)/len(times))

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('npz')
    p.add_argument('--runs', type=int, default=5)
    p.add_argument('--seq', type=int, default=8)
    args = p.parse_args()
    bench(args.npz, runs=args.runs, seq_len=args.seq)
