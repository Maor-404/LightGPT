# Export LightGPT as an ONNX model for Hugging Face Hub
# ---------------------------------------------------------------
# This script loads a pretrained causal model via the ``LightGPT``
# wrapper, then exports it to ONNX. The exported file can be uploaded
# directly to the Hugging Face Model Hub.
# ---------------------------------------------------------------

import argparse
import os
import torch
from .model import LightGPT

def export_to_onnx(
    model_name: str,
    output_path: str,
    opset_version: int = 11,
    max_seq_len: int = 64,
):
    # Load the model wrapper (which loads the HF model internally)
    gpt = LightGPT(model_name=model_name)
    gpt.model.eval()
    # Dummy input for tracing – batch size 1, ``max_seq_len`` tokens
    dummy_input = torch.randint(0, 50257, (1, max_seq_len))
    # Export to ONNX
    torch.onnx.export(
        gpt.model,
        dummy_input,
        output_path,
        export_params=True,
        opset_version=opset_version,
        do_constant_folding=True,
        input_names=["input_ids"],
        output_names=["logits"],
        dynamic_axes={
            "input_ids": {0: "batch_size", 1: "seq_len"},
            "logits": {0: "batch_size", 1: "seq_len"},
        },
        verbose=False,
    )
    print(f"ONNX model exported to {output_path}")
    return output_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Export LightGPT to ONNX")
    parser.add_argument("--model", default="gpt2", help="Base model name or path")
    parser.add_argument("--output", default="lightgpt.onnx", help="Output ONNX file path")
    parser.add_argument("--opset", type=int, default=11, help="ONNX opset version")
    parser.add_argument("--seq_len", type=int, default=64, help="Maximum sequence length for dummy input")
    args = parser.parse_args()
    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    export_to_onnx(args.model, args.output, args.opset, args.seq_len)
