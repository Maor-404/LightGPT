import argparse
from onnxruntime.quantization import quantize_dynamic, QuantType


def quantize(in_path, out_path=None):
    out_path = out_path or in_path.replace('.onnx', '.quant.onnx')
    quantize_dynamic(in_path, out_path, weight_type=QuantType.QInt8)
    print('Saved quantized ONNX to', out_path)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('infile')
    p.add_argument('outfile', nargs='?', default=None)
    args = p.parse_args()
    quantize(args.infile, args.outfile)
