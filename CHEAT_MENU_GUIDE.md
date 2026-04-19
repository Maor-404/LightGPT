# LightGPT Graphical Cheat Menu 🎮

Interactive GUI for configuring and running LightGPT models in Jupyter and Colab notebooks.

## Features

✨ **Interactive Controls**
- Model mode selector (Overkill, Normal, Underkill)
- April Fools stupidity toggle
- Real-time parameter adjustment
- Dynamic code generation

🎨 **Visual Interface**
- Color-coded sections
- Emoji indicators
- Live configuration display
- Copy-paste ready Python code

🚀 **Easy to Use**
- Single cell to run in Colab
- No complex setup
- Visual feedback for all settings
- Comprehensive help section

## Quick Start

### Option 1: Standalone Notebook (Recommended)

Open the dedicated cheat menu notebook in Colab:

```
colab/LightGPT_CheatMenu.ipynb
```

Or upload to Colab and run directly!

### Option 2: In Your Own Notebook

```python
from lightgpt.cheat_menu import create_lightgpt_cheat_menu

# Ensure ipywidgets is installed
import subprocess, sys
subprocess.run([sys.executable, '-m', 'pip', 'install', '-q', 'ipywidgets'])

# Display the menu
create_lightgpt_cheat_menu()
```

## How It Works

### 1. Select Model Mode

Choose one of three modes:

| Mode | Layers | Heads | Embeddings | Use Case |
|------|--------|-------|------------|----------|
| 🚀 Overkill | 8 | 8 | 512 | Powerful GPU, high quality |
| ⚡ Normal | 6 | 6 | 256 | Balanced, most common |
| 🎯 Underkill | 2 | 2 | 64 | CPU-only, lightweight |

### 2. Configure Parameters

**Max Tokens**: How many tokens to generate (1-128)
- Lower = faster, shorter output
- Higher = more text, longer generation time

**Temperature**: Randomness of predictions
- 0.1 = very deterministic, same output each time
- 1.0 = balanced randomness
- 2.0 = highly random, creative but chaotic

**Decoding Strategy**:
- 🎯 Greedy: Always pick the best predicted token
- 🎲 Sampling: Sample randomly based on probabilities (more creative)

### 3. April Fools Mode (Optional)

Toggle **🤪 Stupid Mode** to activate the chaotic easter egg:

```
💡 Normal Thinking  →  🤪 Stupid Mode
```

When enabled:
- Model reasoning becomes backwards
- 15% random token injection
- Silly text corruption
- Absurd phrases mixed in
- Perfect for fun experiments!

### 4. Copy & Run

The menu automatically generates Python code based on your settings:

```python
from lightgpt import LightGPT, generate

# Initialize model
model = LightGPT(mode='normal', max_seq_len=128)

# Prepare prompt
prompt = "Hello LightGPT"
prompt_ids = model.small_vocab_tokenize(prompt)

# Generate
output_ids = generate(
    model,
    prompt_ids,
    max_new_tokens=32,
    temperature=1.0,
    sample=False,
    apply_stupidity=False  # April Fools mode
)

print("Generated:", output_ids)
```

Copy this code, paste it in a new cell, and run!

## Visual Layout

```
┌──────────────────────────────────┐
│  🎮 LightGPT Cheat Menu         │ ← Title
├──────────────────────────────────┤
│ ⚙️  MODEL CONFIGURATION          │ ← Section header
│ [Mode Selector: Buttons]         │
├──────────────────────────────────┤
│ 🎪 APRIL FOOLS MODE             │ ← Section header
│ [April Selector: Buttons]        │
├──────────────────────────────────┤
│ ⚙️  ADVANCED OPTIONS             │ ← Section header
│ [Sliders for tokens, temp, etc]  │
├──────────────────────────────────┤
│ 📋 CURRENT SETTINGS              │ ← Live update box
│ Mode: normal                     │
│ Max Tokens: 32                   │
│ ...etc                           │
├──────────────────────────────────┤
│ 📝 USAGE CODE                    │ ← Auto-generated code
│ ```python                        │
│ from lightgpt import ...         │
│ ...                              │
│ ```                              │
├──────────────────────────────────┤
│ ❓ HELP & INFO                   │ ← Help section
│ • Overkill: ...                  │
│ • Normal: ...                    │
│ ...                              │
└──────────────────────────────────┘
```

## Use Cases

### 💡 Teaching
Show students how to configure models without command-line gymnastics

### 🧪 Experimentation
Quickly try different settings without rewriting code

### 🎉 Fun
Toggle April Fools mode for hilarious experiments

### 📚 Learning
See exactly what parameters do and how code changes

## Requirements

```
ipywidgets>=7.0
jupyter  # or Google Colab
lightgpt  # the package itself
```

In Colab, ipywidgets is usually pre-installed. If not:

```python
!pip install ipywidgets
```

## Files

- **`cheat_menu.py`** — Python module with `create_lightgpt_cheat_menu()` function
- **`colab/LightGPT_CheatMenu.ipynb`** — Standalone notebook ready to run in Colab

## Tips & Tricks

### 🔄 Real-time Updates
All settings update the output code in real-time. Adjust a slider and watch the code change instantly!

### 📋 Copy Button
Most Jupyter environments let you copy code blocks with a click. Use this to quickly grab your generated code.

### 🎯 Presets
Use these recommended configurations:

**Fast Inference:**
```
Mode: Underkill
Max Tokens: 16
Temperature: 0.5
Decoding: Greedy
```

**Balanced:**
```
Mode: Normal
Max Tokens: 32
Temperature: 1.0
Decoding: Sampling
```

**Creative Output:**
```
Mode: Overkill (on GPU)
Max Tokens: 64
Temperature: 1.5
Decoding: Sampling
```

**Maximum Chaos:**
```
Mode: Any
April Fools: ENABLED
Temperature: 2.0
```

## Troubleshooting

### ipywidgets not showing
```python
# Enable widgets in Jupyter
!jupyter nbextension enable --py --sys-prefix widgetsnbextension
```

### Changes not updating
Make sure you're interacting with the toggle buttons and sliders. They should update the config display instantly.

### Code not copying
You can always manually type or select and copy from the code block.

## Have Fun! 🎉

The cheat menu is your dashboard for experimenting with LightGPT. Toggle April Fools mode for chaotic fun, or use normal settings for serious experiments!

Happy tinkering! 🚀
