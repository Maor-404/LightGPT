"""
Very small NumPy runtime for Underkill mode.
Supports a tiny subset of LightGPT model architecture and loads weights exported via `scripts/export_npz.py`.
This is meant for extremely constrained environments (CPU-only, no PyTorch).

Limitations:
- Only tested for `mode='underkill'` (2 layers, small dims)
- Uses simple greedy generation
- No LayerNorm epsilon tuning beyond defaults
"""
import numpy as np
import math


class TinyLightGPT:
    def __init__(self, npz_path):
        data = np.load(npz_path)
        self._load_from_npz(data)

    def _load_from_npz(self, data):
        # required tensors
        self.vocab_size = data['head.weight'].shape[0]
        self.tok_emb = data['tok_emb.weight']  # (vocab, emb)
        self.pos_emb = data['pos_emb.weight']  # (max_pos, emb)
        self.max_seq_len = self.pos_emb.shape[0]
        # detect number of layers by counting block parameters
        layer_ids = []
        for k in data.files:
            if k.startswith('blocks.') and k.endswith('.ln1.weight'):
                parts = k.split('.')
                layer_ids.append(int(parts[1]))
        self.n_layer = max(layer_ids)+1 if layer_ids else 0
        self.layers = []
        for i in range(self.n_layer):
            layer = {}
            prefix = f'blocks.{i}.'
            # Attention qkv: qkv.weight shape (3*emb, emb)
            layer['qkv_w'] = data[prefix + 'attn.qkv.weight']
            layer['qkv_b'] = data[prefix + 'attn.qkv.bias']
            layer['proj_w'] = data[prefix + 'attn.proj.weight']
            layer['proj_b'] = data[prefix + 'attn.proj.bias']
            # FF
            layer['fc1_w'] = data[prefix + 'ff.net.0.weight']
            layer['fc1_b'] = data[prefix + 'ff.net.0.bias']
            layer['fc2_w'] = data[prefix + 'ff.net.2.weight']
            layer['fc2_b'] = data[prefix + 'ff.net.2.bias']
            # LayerNorm params
            layer['ln1_w'] = data[prefix + 'ln1.weight']
            layer['ln1_b'] = data[prefix + 'ln1.bias']
            layer['ln2_w'] = data[prefix + 'ln2.weight']
            layer['ln2_b'] = data[prefix + 'ln2.bias']
            self.layers.append(layer)
        # final ln and head
        self.ln_f_w = data['ln_f.weight']
        self.ln_f_b = data['ln_f.bias']
        self.head_w = data['head.weight']  # (vocab, emb)

    def _layernorm(self, x, w, b, eps=1e-5):
        mu = x.mean(-1, keepdims=True)
        var = ((x - mu)**2).mean(-1, keepdims=True)
        xhat = (x - mu) / np.sqrt(var + eps)
        return w * xhat + b

    def _attention(self, x, layer):
        # x: (T, C)
        C = x.shape[1]
        qkv = x @ layer['qkv_w'].T + layer['qkv_b']
        # split
        q, k, v = np.split(qkv, 3, axis=1)
        # simple single-head attention for tiny runtime: assume underkill small heads
        # compute scaled dot
        scale = 1.0 / math.sqrt(q.shape[1])
        att = (q @ k.T) * scale
        att = np.exp(att - att.max(axis=-1, keepdims=True))
        att = att / att.sum(axis=-1, keepdims=True)
        out = att @ v
        out = out @ layer['proj_w'].T + layer['proj_b']
        return out

    def _ff(self, x, layer):
        h = x @ layer['fc1_w'].T + layer['fc1_b']
        # GELU approximation
        h = 0.5 * h * (1.0 + np.tanh(np.sqrt(2.0 / np.pi) * (h + 0.044715 * h**3)))
        h2 = h @ layer['fc2_w'].T + layer['fc2_b']
        return h2

    def forward(self, ids):
        # ids: list of token ids length T
        T = len(ids)
        if T > self.max_seq_len:
            raise ValueError('Sequence too long for tiny runtime')
        x = self.tok_emb[ids, :] + self.pos_emb[np.arange(T), :]
        for layer in self.layers:
            ln1 = self._layernorm(x, layer['ln1_w'], layer['ln1_b'])
            a = self._attention(ln1, layer)
            x = x + a
            ln2 = self._layernorm(x, layer['ln2_w'], layer['ln2_b'])
            f = self._ff(ln2, layer)
            x = x + f
        x = self._layernorm(x, self.ln_f_w, self.ln_f_b)
        logits = x @ self.head_w.T
        return logits  # (T, vocab)

    def generate(self, prompt_ids, max_new_tokens=16, temperature=1.0):
        ids = list(prompt_ids)
        for _ in range(max_new_tokens):
            logits = self.forward(ids)
            last = logits[-1]
            # greedy
            next_id = int(np.argmax(last))
            ids.append(next_id)
            if len(ids) > self.max_seq_len:
                break
        return ids
