# LightGPT

LightGPT — a lightweight GPT implementation built on top of pre-trained GPT-2 small, designed to run on a wide range of hardware. It supports three modes:

[![PyPI version](https://img.shields.io/pypi/v/lightgpt.svg)](https://pypi.org/project/lightgpt/)
[![CI](https://github.com/Maor-404/LightGPT/actions/workflows/ci.yml/badge.svg)](https://github.com/Maor-404/LightGPT/actions/workflows/ci.yml)
[![Publish](https://github.com/Maor-404/LightGPT/actions/workflows/publish.yml/badge.svg)](https://github.com/Maor-404/LightGPT/actions/workflows/publish.yml)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Maor-404/LightGPT/blob/main/colab/LightGPT_Colab.ipynb)

- **Overkill**: Full GPT-2 small with 512 token context (for modern hardware)
- **Normal**: GPT-2 small with 256 token context (balanced for decent CPU/RAM)
- **Underkill**: GPT-2 small with 128 token context (minimal footprint for low-memory hardware)

**What's New**: LightGPT now uses a real pre-trained GPT-2 small model instead of a custom transformer! This provides much better performance and language understanding while maintaining the lightweight footprint.

This repo contains a minimal reference implementation and demo to run on CPU.

Quickstart (CPU):

1. Create a Python environment with Python 3.10+.
2. Install dependencies:

```
pip install -r requirements.txt
```

1. Run the demo:

```
python examples/run_demo.py --mode normal
```

See `src/lightgpt` for the model and `examples/run_demo.py` for usage.

For roleplay system prompts, see `ROLEPLAY_PROMPTS.txt`.

## Project Structure

- `src/lightgpt/` — main package implementation
- `tests/` — compact test scripts and entry points
- `scripts/` — helper utilities for publishing and repo maintenance
- `examples/` — runnable demo scripts

Root-level helpers such as `load_env.sh` and `push_changes.sh` now delegate to the `scripts/` directory for a cleaner top-level layout.

## Fine-tuning the Model

LightGPT uses a pre-trained GPT-2 small model as the base. You can fine-tune it on your own dataset:

```bash
# Fine-tune on WikiText-2 (default)
python -m lightgpt.train --mode normal --epochs 1 --batch_size 4 --lr 5e-5

# Fine-tune with custom parameters
python -m lightgpt.train --mode underkill --max_seq_len 64 --epochs 2 --batch_size 2
```

The training script will:

- Load the pre-trained GPT-2 small model
- Fine-tune on WikiText-2 dataset
- Save checkpoints for each epoch
- Use much lower learning rates appropriate for fine-tuning

## Advanced: ONNX Export

Since LightGPT now uses GPT-2 as the base model, you can export to ONNX for optimized inference:

- Export ONNX model:

```
python3 examples/export_onnx.py --out lightgpt.onnx --mode normal
```

- Run ONNX Runtime optimized inference:

```
python3 examples/run_onnx.py lightgpt.onnx --prompt "Hello world" --intra 2 --inter 1
```

**Note**: The NumPy Tiny runtime is not compatible with the new GPT-2 based model. For extremely constrained environments, consider using the ONNX runtime with quantization.

Benchmarks & Model Checks

- Compare FP32 vs INT8 ONNX:

```
python3 examples/onnx_benchmark.py lightgpt.onnx --quant lightgpt.quant.onnx --prompt "Hello" --runs 5 --gen 16
```

- Run the model checks (Conversation / Questionnaire / Philosophical) across PyTorch, ONNX and Tiny runtime:

```
python3 examples/model_check.py --out report.txt --onnx lightgpt.onnx --npz lightgpt_weights.npz --mode normal
```

The `model_check.py` script will write a textual report `report.txt` containing the generated token ids and a simple tokenized token-preview. Use this to verify that LightGPT produces outputs for different content styles and runtimes.

Packaging & publishing to PyPI
-----------------------------

This repository is configured to publish as a Python package. Steps to publish a release:

1. Create a PyPI API token: go to <https://pypi.org/manage/account/#api-tokens> and create a token with `upload` scope.

Continuous Integration (recommended)
----------------------------------

Add the token as a repository secret named `PYPI_API_TOKEN` in GitHub (Settings → Secrets). A release workflow is included that publishes automatically when you push a tag matching `v*` (e.g. `v0.1.0`).

Manual (local)
--------------

If you prefer to publish locally, set an environment variable and run the included publish script. Use a secure shell environment — do not commit your token.

POSIX example:

```
export TWINE_PASSWORD=pypi-...
./scripts/publish_pypi.sh
```

PowerShell example:

```
$env:TWINE_PASSWORD='pypi-...'; ./scripts/publish_pypi.ps1
```

Notes:

- The package uses `pyproject.toml` + `setuptools` and includes `README.md` as the long description.
- For Colab, you can install directly from GitHub: `pip install git+https://github.com/Maor-404/LightGPT.git`.
