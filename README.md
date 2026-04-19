# LightGPT

LightGPT — a lightweight, GPT-styled LLM designed to run on a wide range of hardware. It supports three modes:

- Overkill: uses larger architecture and optimized libraries (for modern hardware)
- Normal: balanced parameters for decent CPU/RAM machines
- Underkill: very small footprint for ancient/low-memory hardware

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

Advanced: ONNX & Tiny runtime

- Export ONNX: `python3 examples/export_onnx.py`
- Export NPZ weights for Tiny runtime (after training or checkpoint):
 `python3 scripts/export_npz.py lightgpt.chkpt lightgpt_weights.npz`
- Run NumPy Tiny runtime (Underkill):
 `python3 benchmarks/bench_infer.py lightgpt_weights.npz`

ONNX Runtime (optimized CPU)

- Export dynamic-axes ONNX model:

```
python3 examples/export_onnx.py --out lightgpt.onnx --mode normal --seq 64
```

- Optionally quantize the ONNX model (int8 weights):

```
python3 examples/quantize_onnx.py lightgpt.onnx
```

- Run ONNX Runtime optimized inference (set threads for CPU parallelism):

```
python3 examples/run_onnx.py lightgpt.onnx --prompt "Hello world" --intra 2 --inter 1
```

The ONNX runner uses `onnxruntime` with `ORT_ENABLE_EXTENDED` optimizations and lets you tune `intra_op_num_threads` and `inter_op_num_threads` for your CPU.

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
