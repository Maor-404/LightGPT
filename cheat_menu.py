"""
LightGPT Graphical Cheat Menu

A standalone script that creates an interactive GUI cheat menu for LightGPT.
Perfect for Jupyter/Colab notebooks.

Run this in a notebook cell and get an interactive menu!
"""

def create_lightgpt_cheat_menu():
    """Create and display an interactive cheat menu for LightGPT."""
    
    try:
        import ipywidgets as widgets
        from IPython.display import display, HTML, Markdown
    except ImportError:
        print("ipywidgets not installed. Install with: pip install ipywidgets")
        return
    
    # ===== STYLES =====
    style = {
        'description_width': '120px',
        'button_width': '200px'
    }
    
    title = HTML("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 10px; margin-bottom: 20px;">
        <h1>🎮 LightGPT Cheat Menu</h1>
        <p><i>Interactive Control Panel for Lightweight GPT</i></p>
    </div>
    """)
    
    # Model Selection Section
    display(HTML("""
    <div style="background: #f0f0f0; padding: 15px; border-radius: 8px; margin: 10px 0;">
        <h3>⚙️ MODEL CONFIGURATION</h3>
    </div>
    """))
    
    mode_selector = widgets.ToggleButtons(
        options=['🚀 Overkill', '⚡ Normal', '🎯 Underkill'],
        description='Mode:',
        style=style,
        button_style='info'
    )
    
    display(widgets.Label("Select Model Mode:"))
    display(mode_selector)
    
    # April Fools Section
    display(HTML("""
    <div style="background: #fff3cd; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>🎪 APRIL FOOLS MODE</h3>
    </div>
    """))
    
    april_fools_toggle = widgets.ToggleButtons(
        options=['💡 Normal Thinking', '🤪 Stupid Mode'],
        description='Reasoning:',
        style=style,
        button_style='warning'
    )
    
    display(widgets.Label("Enable Stupidity (for April 1st or forced chaos):"))
    display(april_fools_toggle)
    
    # Quick Actions
    display(HTML("""
    <div style="background: #d4edda; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>🎯 QUICK ACTIONS</h3>
    </div>
    """))
    
    action_buttons = widgets.HBox([
        widgets.Button(description='📊 Run Demo', button_style='success', tooltip='Run quick demo'),
        widgets.Button(description='📈 Benchmarks', button_style='success', tooltip='Show performance'),
        widgets.Button(description='🎭 April Fools', button_style='danger', tooltip='Run silly demo'),
    ])
    
    display(action_buttons)
    
    # Advanced Options
    display(HTML("""
    <div style="background: #e8dff5; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>⚙️ ADVANCED OPTIONS</h3>
    </div>
    """))
    
    max_tokens = widgets.IntSlider(
        value=32,
        min=1,
        max=128,
        step=1,
        description='Max Tokens:',
        style=style
    )
    
    temperature = widgets.FloatSlider(
        value=1.0,
        min=0.1,
        max=2.0,
        step=0.1,
        description='Temperature:',
        style=style
    )
    
    sample_toggle = widgets.ToggleButtons(
        options=['🎯 Greedy', '🎲 Sampling'],
        description='Decoding:',
        style=style,
        button_style='info'
    )
    
    display(max_tokens)
    display(temperature)
    display(widgets.Label("Decoding Strategy:"))
    display(sample_toggle)
    
    # Settings Summary
    display(HTML("""
    <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>📋 CURRENT SETTINGS</h3>
    </div>
    """))
    
    summary_output = widgets.Output()
    
    def update_summary(*args):
        with summary_output:
            summary_output.clear_output()
            
            mode_map = {'🚀 Overkill': 'overkill', '⚡ Normal': 'normal', '🎯 Underkill': 'underkill'}
            april_map = {'💡 Normal Thinking': False, '🤪 Stupid Mode': True}
            sample_map = {'🎯 Greedy': False, '🎲 Sampling': True}
            
            mode = mode_map.get(mode_selector.value, 'normal')
            stupid = april_map.get(april_fools_toggle.value, False)
            sample = sample_map.get(sample_toggle.value, False)
            
            print(f"""
╔════════════════════════════════════════╗
║        🔧 CURRENT CONFIGURATION        ║
╠════════════════════════════════════════╣
║ Model Mode:        {mode:24s} ║
║ Max Tokens:        {max_tokens.value:24d} ║
║ Temperature:       {temperature.value:24.1f} ║
║ Sampling:          {str(sample):24s} ║
║ April Fools:       {str(stupid):24s} ║
╚════════════════════════════════════════╝
            """)
    
    mode_selector.observe(update_summary, names='value')
    april_fools_toggle.observe(update_summary, names='value')
    max_tokens.observe(update_summary, names='value')
    temperature.observe(update_summary, names='value')
    sample_toggle.observe(update_summary, names='value')
    
    display(summary_output)
    update_summary()
    
    # Copy-Paste Code Section
    display(HTML("""
    <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>📝 USAGE CODE (Copy & Paste)</h3>
    </div>
    """))
    
    code_output = widgets.Output()
    
    def update_code(*args):
        with code_output:
            code_output.clear_output()
            
            mode_map = {'🚀 Overkill': 'overkill', '⚡ Normal': 'normal', '🎯 Underkill': 'underkill'}
            april_map = {'💡 Normal Thinking': False, '🤪 Stupid Mode': True}
            sample_map = {'🎯 Greedy': False, '🎲 Sampling': True}
            
            mode = mode_map.get(mode_selector.value, 'normal')
            stupid = april_map.get(april_fools_toggle.value, False)
            sample = sample_map.get(sample_toggle.value, False)
            
            code = f"""
from lightgpt import LightGPT, generate

# Initialize model
model = LightGPT(mode='{mode}', max_seq_len=128)

# Prepare prompt
prompt = "Hello LightGPT"
prompt_ids = model.small_vocab_tokenize(prompt)

# Generate
output_ids = generate(
    model,
    prompt_ids,
    max_new_tokens={max_tokens.value},
    temperature={temperature.value},
    sample={sample},
    apply_stupidity={stupid}  # April Fools mode
)

print("Generated:", output_ids)
            """
            
            print("```python")
            print(code)
            print("```")
    
    mode_selector.observe(update_code, names='value')
    april_fools_toggle.observe(update_code, names='value')
    max_tokens.observe(update_code, names='value')
    temperature.observe(update_code, names='value')
    sample_toggle.observe(update_code, names='value')
    
    display(code_output)
    update_code()
    
    # Help Section
    display(HTML("""
    <div style="background: #d1ecf1; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>❓ HELP & INFO</h3>
    </div>
    """))
    
    help_text = widgets.HTML("""
    <ul style="font-size: 14px; line-height: 1.8;">
        <li><b>Overkill:</b> 8 layers, 8 heads, 512 embeddings — for powerful GPUs</li>
        <li><b>Normal:</b> 6 layers, 6 heads, 256 embeddings — balanced sweet spot</li>
        <li><b>Underkill:</b> 2 layers, 2 heads, 64 embeddings — ultra-lightweight CPU mode</li>
        <li><b>Temperature:</b> Higher = more random, Lower = more deterministic</li>
        <li><b>April Fools:</b> Enable for chaotic, backwards reasoning (activate your stupidity!)</li>
        <li><b>Sampling:</b> Greedy picks best token, Sampling is more creative</li>
    </ul>
    """)
    display(help_text)
    
    # Footer
    display(HTML("""
    <div style="text-align: center; padding: 20px; background: #e9ecef; 
                border-radius: 10px; margin-top: 30px; border: 2px solid #dee2e6;">
        <p><b>LightGPT Cheat Menu</b> — Ready to generate! 🚀</p>
        <p style="font-size: 12px; color: #666;">
            Run your configured settings with the code above. Happy training! ✨
        </p>
    </div>
    """))


# Run the menu when this cell is executed
if __name__ == "__main__":
    create_lightgpt_cheat_menu()
