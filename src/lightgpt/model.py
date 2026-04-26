import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from .holiday_personas import get_persona_prompt

class LightGPT:
    """A thin wrapper around a HuggingFace causal language model.

    It loads a pretrained model, provides a simple ``generate`` method, and
    supports optional holiday personas that can be prepended to the prompt.
    """

    def __init__(self, model_name: str = "EleutherAI/gpt-neo-125M", device: str | None = None):
        """Initialize the model and tokenizer.

        Args:
            model_name: Name or path of the Hugging Face model.
            device: ``"cpu"`` or ``"cuda"``. If ``None`` the best available device is chosen.
        """
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = AutoModelForCausalLM.from_pretrained(model_name)
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)
        self.model.eval()

    def generate(
        self,
        prompt: str,
        max_new_tokens: int = 50,
        temperature: float = 1.0,
        do_sample: bool = False,
        top_k: int | None = None,
        top_p: float | None = None,
        persona: str | None = None,
    ) -> str:
        """Generate text continuation for a prompt.

        Args:
            prompt: Input text.
            max_new_tokens: Number of tokens to generate.
            temperature: Sampling temperature.
            do_sample: Whether to sample (True) or use greedy decoding.
            top_k: Top‑k sampling (optional).
            top_p: Nucleus sampling (optional).
            persona: Optional holiday persona key (e.g. ``"may_the_4th"``). If provided,
                the corresponding persona prompt is prepended.
        """
        # Apply persona if requested
        if persona:
            persona_prompt = get_persona_prompt(persona)
            if persona_prompt:
                prompt = f"{persona_prompt}\n{prompt}"
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        gen_kwargs = {
            "max_length": inputs["input_ids"].shape[1] + max_new_tokens,
            "temperature": temperature,
            "do_sample": do_sample,
            "pad_token_id": self.tokenizer.pad_token_id,
            "eos_token_id": self.tokenizer.eos_token_id,
        }
        if top_k is not None:
            gen_kwargs["top_k"] = top_k
        if top_p is not None:
            gen_kwargs["top_p"] = top_p
        with torch.no_grad():
            output_ids = self.model.generate(**inputs, **gen_kwargs)
        return self.tokenizer.decode(output_ids[0], skip_special_tokens=True)

    def save(self, save_directory: str) -> None:
        """Save the model and tokenizer to ``save_directory``."""
        self.model.save_pretrained(save_directory)
        self.tokenizer.save_pretrained(save_directory)
        print(f"Model and tokenizer saved to {save_directory}")

    @classmethod
    def load(cls, load_directory: str, device: str | None = None) -> "LightGPT":
        """Load a previously saved model from ``load_directory``."""
        return cls(model_name=load_directory, device=device)
