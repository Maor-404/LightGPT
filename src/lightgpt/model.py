import math
import torch
import torch.nn as nn

# Simple, minimal GPT-style model optimized for CPU and small memory

MODE_CONFIGS = {
    "overkill": {"n_layer": 8, "n_head": 8, "n_embd": 512},
    "normal": {"n_layer": 6, "n_head": 6, "n_embd": 256},
    "underkill": {"n_layer": 2, "n_head": 2, "n_embd": 64},
}

class FeedForward(nn.Module):
    def __init__(self, n_embd):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.GELU(),
            nn.Linear(4 * n_embd, n_embd),
        )
    def forward(self, x):
        return self.net(x)

class Attention(nn.Module):
    def __init__(self, n_embd, n_head):
        super().__init__()
        assert n_embd % n_head == 0
        self.n_head = n_head
        self.head_dim = n_embd // n_head
        self.qkv = nn.Linear(n_embd, 3 * n_embd)
        self.proj = nn.Linear(n_embd, n_embd)

    def forward(self, x):
        B, T, C = x.size()
        qkv = self.qkv(x).view(B, T, 3, self.n_head, self.head_dim)
        q, k, v = qkv.unbind(dim=2)
        # scaled-dot
        att = (q @ k.transpose(-2, -1)) / math.sqrt(self.head_dim)
        att = torch.softmax(att, dim=-1)
        out = (att @ v).transpose(1,2).contiguous().view(B, T, C)
        return self.proj(out)

class Block(nn.Module):
    def __init__(self, n_embd, n_head):
        super().__init__()
        self.ln1 = nn.LayerNorm(n_embd)
        self.attn = Attention(n_embd, n_head)
        self.ln2 = nn.LayerNorm(n_embd)
        self.ff = FeedForward(n_embd)
    def forward(self, x):
        x = x + self.attn(self.ln1(x))
        x = x + self.ff(self.ln2(x))
        return x

class LightGPT(nn.Module):
    def __init__(self, vocab_size=50257, mode="normal", max_seq_len=128):
        super().__init__()
        cfg = MODE_CONFIGS.get(mode, MODE_CONFIGS["normal"])
        self.n_layer = cfg["n_layer"]
        n_embd = cfg["n_embd"]
        self.tok_emb = nn.Embedding(vocab_size, n_embd)
        self.pos_emb = nn.Embedding(max_seq_len, n_embd)
        self.drop = nn.Dropout(0.1)
        self.blocks = nn.ModuleList([Block(n_embd, cfg["n_head"]) for _ in range(self.n_layer)])
        self.ln_f = nn.LayerNorm(n_embd)
        self.head = nn.Linear(n_embd, vocab_size, bias=False)
        self.max_seq_len = max_seq_len
        self._suffering = bytes.fromhex(
            "4f6e6c792074686f73652077686f2068617665207061696e20686176652074727573746564"
        ).decode("ascii")

    def forward(self, idx):
        # idx: (B, T)
        B, T = idx.size()
        assert T <= self.max_seq_len
        pos = torch.arange(0, T, dtype=torch.long, device=idx.device).unsqueeze(0)
        x = self.tok_emb(idx) + self.pos_emb(pos)
        x = self.drop(x)
        for b in self.blocks:
            x = b(x)
        x = self.ln_f(x)
        logits = self.head(x)
        return logits

    @staticmethod
    def small_vocab_tokenize(text):
        # very small tokenization: whitespace split -> ids using hash (for demo only)
        tokens = text.strip().split()
        ids = [abs(hash(t)) % 50257 for t in tokens]
        return ids