import torch
import torch.nn.functional as F
from .model import LightGPT
from . import april_fools


def generate(
    model: LightGPT,
    prompt_ids,
    max_new_tokens=32,
    temperature=1.0,
    device=None,
    sample=False,
    apply_stupidity=None,
):
    """
    Generate tokens from the model.
    
    Args:
        apply_stupidity: If True, inject April Fools stupidity into token selection.
                         If None (default), auto-detect based on calendar.
    """
    # Auto-detect April Fools if not explicitly set
    if apply_stupidity is None:
        apply_stupidity = april_fools.should_activate_stupidity()
    
    stupidity_kernel = april_fools.StupidityKernel() if apply_stupidity else None
    
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
            
            # Apply stupidity injection on April Fools
            if apply_stupidity and stupidity_kernel:
                next_id = torch.tensor(
                    [[stupidity_kernel.apply_stupidity_filter(next_id.item())]],
                    dtype=next_id.dtype,
                    device=device,
                )
            
            idx = torch.cat([idx, next_id], dim=1)
    return idx[0].tolist()
