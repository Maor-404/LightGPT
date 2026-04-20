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
    roleplay_prompt=None,
):
    """
    Generate tokens from the model.
    
    Args:
        apply_stupidity: Controls special features and stupidity injection.
                         - None (default): Auto-detect April Fools for stupidity only
                         - "april_fools": Force April Fools stupidity
                         - "star_wars", "undertale", "halloween", "deltarune": Special themed features (no stupidity)
                         - False: Disable all special features
        roleplay_prompt: Optional string to prepend as roleplay context before the main prompt.
                         If None and a themed event is active, will auto-select appropriate character roleplay.
    """
    # Auto-detect April Fools stupidity only
    if apply_stupidity is None:
        stupidity_event = april_fools.should_activate_stupidity()
        special_event = april_fools.get_current_special_event()
        # Only use stupidity for April Fools
        if stupidity_event == "april_fools":
            apply_stupidity = "april_fools"
        # For other special events, use themed features but no stupidity
        elif special_event and special_event != "april_fools":
            apply_stupidity = special_event
    
    # Create appropriate reasoner based on event type
    reasoner = None
    stupidity_injection = False
    roleplay_text = None
    
    if apply_stupidity:
        if apply_stupidity == "april_fools":
            reasoner = april_fools.AprilFoolsReasoner()
            stupidity_injection = True  # Only April Fools gets stupidity injection
        elif apply_stupidity == "star_wars":
            reasoner = april_fools.StarWarsReasoner()
            roleplay_text = reasoner.get_roleplay_prompt()
        elif apply_stupidity == "undertale":
            reasoner = april_fools.UndertaleReasoner()
            roleplay_text = reasoner.get_roleplay_prompt()
        elif apply_stupidity == "halloween":
            reasoner = april_fools.HalloweenReasoner()
        elif apply_stupidity == "deltarune":
            reasoner = april_fools.DeltaruneReasoner()
            roleplay_text = reasoner.get_roleplay_prompt()
        elif apply_stupidity == "forced":
            # Default to April Fools for forced activation
            reasoner = april_fools.AprilFoolsReasoner()
            stupidity_injection = True
    
    device = device or next(model.parameters()).device
    model.eval()

    # Handle roleplay prompt prepending
    if roleplay_prompt or roleplay_text:
        effective_roleplay = roleplay_prompt or roleplay_text
        roleplay_ids = model.tokenizer.encode(effective_roleplay, add_special_tokens=False)
        if isinstance(prompt_ids, list):
            prompt_ids = roleplay_ids + prompt_ids
        else:
            # If prompt_ids is already a tensor, convert roleplay_ids to tensor and concatenate
            roleplay_tensor = torch.tensor([roleplay_ids], dtype=torch.long, device=device)
            prompt_ids = torch.cat([roleplay_tensor, prompt_ids.unsqueeze(0)], dim=1).squeeze(0)

    # Convert prompt_ids to tensor if it's not already
    if isinstance(prompt_ids, list):
        input_ids = torch.tensor([prompt_ids], dtype=torch.long, device=device)
    else:
        input_ids = torch.tensor(prompt_ids, dtype=torch.long, device=device).unsqueeze(0)

    with torch.no_grad():
        for _ in range(max_new_tokens):
            # Get logits from GPT-2 model
            outputs = model.model(input_ids=input_ids)
            logits = outputs.logits

            # Get the last token's logits
            next_token_logits = logits[:, -1, :] / max(temperature, 1e-6)
            probs = torch.softmax(next_token_logits, dim=-1)

            if sample:
                next_id = torch.multinomial(probs, num_samples=1)
            else:
                next_id = torch.argmax(probs, dim=-1, keepdim=True)

            # Apply stupidity injection ONLY for April Fools
            if stupidity_injection and reasoner:
                next_id = torch.tensor(
                    [[reasoner.apply_stupidity_filter(next_id.item())]],
                    dtype=next_id.dtype,
                    device=device,
                )

            input_ids = torch.cat([input_ids, next_id], dim=1)

            # Stop if we hit EOS token
            if next_id.item() == model.tokenizer.eos_token_id:
                break

    return input_ids[0].tolist()
