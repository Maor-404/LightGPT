import torch
import torch.nn.functional as F
from .model import LightGPT


def generate(model: LightGPT, prompt_ids, max_new_tokens=32, temperature=1.0, device=None, sample=False):
    device = device or next(model.parameters()).device
    model.eval()
    idx = torch.tensor([prompt_ids], dtype=torch.long, device=device)
    with torch.no_grad():
        for _ in range(max_new_tokens):
            logits = model(idx)
            logits = logits[:, -1, :] / max(temperature, 1e-6)
            probs = F.softmax(logits, dim=-1)
            if sample:
                next_id = torch.multinomial(probs, num_samples=1)
            else:
                next_id = torch.argmax(probs, dim=-1, keepdim=True)
            idx = torch.cat([idx, next_id], dim=1)
    return idx[0].tolist()
