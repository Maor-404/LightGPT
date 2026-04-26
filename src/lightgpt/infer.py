import torch
from .model import LightGPT

def generate_text(
    prompt: str,
    model_name: str = "gpt2",
    max_new_tokens: int = 50,
    temperature: float = 1.0,
    do_sample: bool = False,
):
    """Convenient helper for quick generation from the command line.

    Returns the generated text (prompt + continuation).
    """
    gpt = LightGPT(model_name=model_name)
    return gpt.generate(
        prompt=prompt,
        max_new_tokens=max_new_tokens,
        temperature=temperature,
        do_sample=do_sample,
    )

if __name__ == "__main__":
    # Simple demo
    print(generate_text("Hello, my name is"))
