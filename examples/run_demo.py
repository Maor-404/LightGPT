import argparse
import torch
from lightgpt import LightGPT, generate


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["overkill","normal","underkill"], default="normal")
    p.add_argument("--prompt", default="Hello world")
    args = p.parse_args()

    device = torch.device("cpu")
    model = LightGPT(mode=args.mode, max_seq_len=64)
    model.to(device)

    ids = LightGPT.small_vocab_tokenize(args.prompt)
    out_ids = generate(model, ids, max_new_tokens=16, temperature=1.0, device=device)
    print("Input ids:", ids)
    print("Output ids:", out_ids)

if __name__ == '__main__':
    main()
