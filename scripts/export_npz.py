import argparse
import torch
import numpy as np

from lightgpt.model import LightGPT


def export_npz(checkpoint_path, out_npz):
    data = torch.load(checkpoint_path, map_location='cpu')
    state = data.get('model_state_dict', data)
    np_dict = {}
    for k, v in state.items():
        np_dict[k] = v.cpu().numpy()
    np.savez_compressed(out_npz, **np_dict)
    print('Saved NPZ to', out_npz)

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('checkpoint')
    p.add_argument('out', nargs='?', default='lightgpt_weights.npz')
    args = p.parse_args()
    export_npz(args.checkpoint, args.out)
