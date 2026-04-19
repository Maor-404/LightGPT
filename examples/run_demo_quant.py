import argparse
import torch
from lightgpt import LightGPT, generate
from torch.quantization import quantize_dynamic


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mode", choices=["overkill","normal","underkill"], default="normal")
    p.add_argument("--prompt", default="Hello world")
    p.add_argument("--device", choices=["cpu","cuda"], default="cpu")
    p.add_argument("--quantize", choices=["none","dynamic"], default="none", help="Apply dynamic quantization (CPU only)")
    p.add_argument("--fp16", action="store_true", help="Use FP16 on CUDA (if available)")
    p.add_argument("--sample", action="store_true", help="Use sampling instead of greedy")
    args = p.parse_args()

    device = torch.device("cuda" if args.device == "cuda" and torch.cuda.is_available() else "cpu")
    model = LightGPT(mode=args.mode, max_seq_len=64)

    # Prepare model for quantization or fp16
    if device.type == "cpu":
        model.cpu()
        if args.quantize == "dynamic":
            # Quantize only linear layers for smaller, faster CPU model
            model = quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
    else:
        if args.fp16:
            model.half().to(device)
        else:
            model.to(device)

    # Tokenize
    ids = LightGPT.small_vocab_tokenize(args.prompt)
    # Convert to proper device and dtype when needed
    out_ids = generate(model, ids, max_new_tokens=16, temperature=1.0, device=device, sample=args.sample)
    print("Input ids:", ids)
    print("Output ids:", out_ids)

if __name__ == '__main__':
    main()
