# LightGPT – Simple Hugging Face Wrapper

**🎉 LightGPT 1.0.0 – Celebration 🎉**

We’re thrilled to announce the first stable release of LightGPT! This version marks the end of the beta phase and brings a polished, production‑ready package that:
- Uses the lightweight **EleutherAI/gpt‑neo‑125M** model by default.
- Provides holiday personas for fun themed interactions.
- Includes a quick Wikipedia data collector for easy finetuning.
- Adds a new data‑download script for additional corpora (WikiText‑103, OpenWebText, TinyNews).
- Offers a simple CLI, finetuning script, and ONNX export workflow.
- Is publishable both as a Python package *and* as an ONNX model on the Hugging Face Hub.

---

## Quickstart

```bash
# Install dependencies (including Wikipedia and datasets support)
pip install -r requirements.txt
```

```python
from lightgpt.model import LightGPT

lgpt = LightGPT()  # loads EleutherAI/gpt‑neo‑125M
print(lgpt.generate("The future of AI is", max_new_tokens=30))
```

## Command‑line interface

```bash
python -m lightgpt.cli \
    --model EleutherAI/gpt‑neo‑125M \
    --prompt "Once upon a time" \
    --max_new_tokens 40 \
    --temperature 0.9 \
    --do_sample
```

## Finetuning a model

A minimal finetuning script is provided in `src/lightgpt/train.py`. It uses the standard `transformers` training loop.

```bash
# Example: finetune on Wikipedia data
python -m lightgpt.train \
    --model EleutherAI/gpt‑neo‑125M \
    --train_file wiki_corpus.txt \
    --output_dir finetuned_gptneo \
    --epochs 3
```

### Additional corpora

You can download larger text collections with the new helper:

```bash
# WikiText‑103
python scripts/download_data.py --source wikitext --output wikitext.txt

# OpenWebText (small subset)
python scripts/download_data.py --source openwebtext --output openwebtext.txt

# TinyNews (sample news articles)
python scripts/download_data.py --source tinynews --output tinynews.txt
```

These files can be passed to the same `train.py` script just like the Wikipedia corpus.

## Export to ONNX (for Hugging Face Hub)

```bash
python -m lightgpt.export_onnx \
    --model finetuned_gptneo \
    --output lightgpt_neo.onnx
```

The resulting `lightgpt_neo.onnx` can be uploaded directly to the Hugging  Face Model Hub alongside the saved model folder.

## Holiday Personas

```python
from lightgpt.holiday_personas import get_persona_prompt

prompt = get_persona_prompt("may_the_4th") + " What is the Force?"
print(LightGPT().generate(prompt))
```

---

## Publishing to Hugging  Face

1. **Create a repository** on the Hugging  Face Hub (e.g., `Maor-404/LightGPT`).
2. **Push the ONNX file** and the model directory:
   ```bash
   git lfs install
   git clone https://huggingface.co/username/LightGPT
   cp lightgpt_neo.onnx LightGPT/
   cp -r finetuned_gptneo/* LightGPT/
   cd LightGPT && git add . && git commit -m "Add ONNX model and finetuned weights" && git push
   ```
3. Add a model card (`README.md`) – the one you are reading – and the Hub will render it automatically.

---

## License

MIT – see `LICENSE` for details.


