import argparse
import torch
from lightgpt import LightGPT


def export_onnx(out_path='lightgpt.onnx', mode='normal', seq_len=64, opset=13):
    model = LightGPT(mode=mode, max_seq_len=seq_len)
    model.eval()
    dummy = torch.zeros((1, seq_len), dtype=torch.long)
    # Export with dynamic axes to allow variable sequence lengths
    torch.onnx.export(
        model,
        dummy,
        out_path,
        opset_version=opset,
        input_names=['input_ids'],
        output_names=['logits'],
        dynamic_axes={
            'input_ids': {1: 'sequence'},
            'logits': {1: 'sequence'}
        }
    )
    print('Exported ONNX model to', out_path)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--out', default='lightgpt.onnx')
    p.add_argument('--mode', choices=['overkill', 'normal', 'underkill'], default='normal')
    p.add_argument('--seq', type=int, default=64)
    p.add_argument('--opset', type=int, default=13)
    args = p.parse_args()
    export_onnx(args.out, mode=args.mode, seq_len=args.seq, opset=args.opset)
