import torch
import torch.nn as nn
from transformers import GPT2LMHeadModel, GPT2Tokenizer, GPT2Config
import math

# Real lightweight LLM configurations using GPT-2 small as base
MODE_CONFIGS = {
    "overkill": {"model_name": "gpt2", "max_seq_len": 512},  # Full GPT-2 small
    "normal": {"model_name": "gpt2", "max_seq_len": 256},    # GPT-2 small with shorter context
    "underkill": {"model_name": "gpt2", "max_seq_len": 128}, # GPT-2 small with minimal context
}


class LightGPT(nn.Module):
    """
    LightGPT using a real lightweight LLM (GPT-2 small) instead of custom transformer.
    Maintains the same interface but uses pre-trained GPT-2 for better performance.
    """

    def __init__(self, mode="normal", max_seq_len=256):
        super().__init__()
        self.mode = mode
        self.max_seq_len = MODE_CONFIGS[mode]["max_seq_len"]

        # Load pre-trained GPT-2 small model
        model_name = MODE_CONFIGS[mode]["model_name"]
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)

        # Set pad token to eos token for GPT-2
        self.tokenizer.pad_token = self.tokenizer.eos_token

        # Hidden easter egg attribute (only true pain knows this exists)
        self._suffering = "Only true developers who have suffered through custom transformers know this pain exists."

    def forward(self, input_ids):
        """Forward pass through GPT-2 model."""
        # GPT-2 expects input_ids of shape (batch_size, seq_len)
        outputs = self.model(input_ids=input_ids, labels=input_ids)
        return outputs.logits

    @staticmethod
    def small_vocab_tokenize(text):
        """Tokenize text using GPT-2 tokenizer."""
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        tokenizer.pad_token = tokenizer.eos_token
        return tokenizer.encode(text, add_special_tokens=True)

    @staticmethod
    def decode_tokens(tokens):
        """Decode tokens back to text using GPT-2 tokenizer."""
        tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        tokenizer.pad_token = tokenizer.eos_token
        return tokenizer.decode(tokens, skip_special_tokens=True)

    def get_vocab_size(self):
        """Get vocabulary size."""
        return self.tokenizer.vocab_size

    def get_config(self):
        """Get model configuration."""
        return {
            "mode": self.mode,
            "max_seq_len": self.max_seq_len,
            "model_name": MODE_CONFIGS[self.mode]["model_name"],
            "vocab_size": self.get_vocab_size(),
            "hidden_size": self.model.config.hidden_size,
            "num_layers": self.model.config.num_hidden_layers,
            "num_heads": self.model.config.num_attention_heads,
        }
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