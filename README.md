# LightGPT – Simple Hugging Face Wrapper

LightGPT is now a thin wrapper around any Hugging Face causal language model (e.g. `gpt2`, `distilgpt2`, `EleutherAI/gpt‑neo‑125M`).
It provides a very small API for loading a model, generating text, saving/loading weights, and exporting to ONNX.

---

## Quickstart

```bash
# Install dependencies (torch, transformers, onnx, onnxruntime)
pip install -r requirements.txt
```

```python
from lightgpt.model import LightGPT

# Load a model (downloads from Hugging Face if needed)
lgpt = LightGPT(model_name="gpt2")

# Generate text
txt = lgpt.generate(
    prompt="The future of AI is",
    max_new_tokens=30,
    temperature=0.8,
    do_sample=True,
)
print(txt)
```

## Command‑line interface

```bash
python -m lightgpt.cli \
    --model gpt2 \
    --prompt "Once upon a time" \
    --max_new_tokens 40 \
    --temperature 0.9 \
    --do_sample
```

## Finetuning a model

A minimal finetuning script is provided in `src/lightgpt/train.py`. It uses the standard `transformers` training loop.

```bash
python -m lightgpt.train \
    --model gpt2 \
    --train_file data/my_corpus.txt \
    --output_dir finetuned_gpt2 \
    --epochs 3
```

The script writes a new directory containing a `pytorch_model.bin` and tokenizer files that can be loaded with `LightGPT(model_name="finetuned_gpt2")`.

## Export to ONNX (for Hugging Face Hub)

```bash
python -m lightgpt.export_onnx \
    --model finetuned_gpt2 \
    --output lightgpt.onnx
```

The resulting `lightgpt.onnx` can be uploaded to the Hugging Face Model Hub alongside the saved model folder.

---

## Why this wrapper?

* **Simplicity** – No custom architecture to maintain; you rely on the battle‑tested `transformers` implementations.
* **Portability** – Export to ONNX for fast CPU inference or deployment to environments where PyTorch isn’t available.
* **Flexibility** – Swap the base model by changing a single string (`model_name`).

---

## License

MIT – see `LICENSE` for details.
