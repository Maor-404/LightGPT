import argparse
import os
from .model import LightGPT

def main():
    parser = argparse.ArgumentParser(description="LightGPT command‑line utility")
    parser.add_argument("--model", default="gpt2", help="HuggingFace model name or path")
    parser.add_argument("--prompt", required=True, help="Prompt text to generate from")
    parser.add_argument("--max_new_tokens", type=int, default=50, help="Number of tokens to generate")
    parser.add_argument("--temperature", type=float, default=1.0, help="Sampling temperature")
    parser.add_argument("--do_sample", action="store_true", help="Enable sampling (instead of greedy)")
    parser.add_argument("--save_dir", default=None, help="Directory to save the model after loading (optional)")
    args = parser.parse_args()

    # Initialise LightGPT wrapper
    gpt = LightGPT(model_name=args.model)
    # Generate text
    out = gpt.generate(
        prompt=args.prompt,
        max_new_tokens=args.max_new_tokens,
        temperature=args.temperature,
        do_sample=args.do_sample,
    )
    print(out)
    # Optionally save the model locally
    if args.save_dir:
        os.makedirs(args.save_dir, exist_ok=True)
        gpt.save(args.save_dir)

if __name__ == "__main__":
    main()
