# LightGPT – Simple Hugging Face Wrapper

**🎉 LightGPT 1.0.0 – Celebration 🎉**

We’re thrilled to announce the first stable release of LightGPT! This version marks the end of the beta phase and brings a polished, production‑ready package that:
- Uses the lightweight **EleutherAI/gpt‑neo‑125M** model by default.
- Provides holiday personas for fun themed interactions.
- Includes a quick Wikipedia data collector for easy finetuning.
- Offers a simple CLI, finetuning script, and ONNX export workflow.

---

## Quickstart

```bash
# Install dependencies (including Wikipedia support)
pip install -r requirements.txt
```

```python
from lightgpt.model import LightGPT

lgpt = LightGPT()  # loads EleutherAI/gpt-neo-125M
print(lgpt.generate("The future of AI is", max_new_tokens=30))
```

## Command‑line interface

```bash
python -m lightgpt.cli \
    --model EleutherAI/gpt-neo-125M \
    --prompt "Once upon a time" \
    --max_new_tokens 40 \
    --temperature 0.9 \
    --do_sample
```

## Finetuning a model

A minimal finetuning script is provided in `src/lightgpt/train.py`. It uses the standard `transformers` training loop.

```bash
python -m lightgpt.train \
    --model EleutherAI/gpt-neo-125M \
    --train_file data/my_corpus.txt \
    --output_dir finetuned_gptneo \
    --epochs 3
```

The script writes a new directory containing a `pytorch_model.bin` and tokenizer files that can be loaded with `LightGPT(model_name="finetuned_gptneo")`.

## Export to ONNX (for Hugging Face Hub)

```bash
python -m lightgpt.export_onnx \
    --model finetuned_gptneo \
    --output lightgpt_neo.onnx
```

The resulting `lightgpt_neo.onnx` can be uploaded to the Hugging Face Model Hub alongside the saved model folder.

## Wikipedia data collection

Use the provided script to fetch articles for training:

```bash
python scripts/download_wiki.py \
    --topics "Artificial intelligence" "Machine learning" "Natural language processing" \
    --output wiki_corpus.txt
```

## Holiday Personas

```python
from lightgpt.holiday_personas import get_persona_prompt

prompt = get_persona_prompt("may_the_4th") + " What is the Force?"
print(LightGPT().generate(prompt))
```

---

## License

MIT – see `LICENSE` for details.

