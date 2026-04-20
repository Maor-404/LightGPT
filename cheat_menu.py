"""
================================================================================
    LightGPT Graphical Cheat Menu - Interactive GUI for Model Configuration
================================================================================

Description:
    A standalone, reusable script that creates an interactive GUI cheat menu 
    for LightGPT model configuration. Perfect for Jupyter Notebooks and Google Colab.
    
    This module provides a complete control panel with:
    - Model mode selection (Overkill/Normal/Underkill)
    - April Fools (stupidity injection) toggle
    - Advanced parameter sliders (max tokens, temperature)
    - Decoding strategy selection (Greedy/Sampling)
    - Real-time settings summary box
    - Auto-generated Python code for copy-paste usage
    - Comprehensive help and information section
    
Usage:
    In a Jupyter cell, simply run:
        from lightgpt.cheat_menu import create_lightgpt_cheat_menu
        create_lightgpt_cheat_menu()
    
    Or if using inline:
        import lightgpt.cheat_menu as cm
        cm.create_lightgpt_cheat_menu()

Requirements:
    - ipywidgets (auto-installed if missing in Colab/Jupyter)
    - IPython (standard in Jupyter/Colab)
    - lightgpt (the main package)

Author: LightGPT Team
Version: 1.0
================================================================================
"""

def create_lightgpt_cheat_menu():
    """
    Create and display an interactive cheat menu for LightGPT.
    
    This function builds a complete graphical control panel with multiple sections:
    1. MODEL CONFIGURATION - Select efficiency mode (Overkill/Normal/Underkill)
    2. APRIL FOOLS MODE - Toggle stupidity injection for chaotic behavior
    3. QUICK ACTIONS - Buttons for demo, benchmarks, April Fools showcase
    4. ADVANCED OPTIONS - Fine-tune parameters (tokens, temperature, sampling)
    5. CURRENT SETTINGS - Real-time summary of all selected configuration
    6. USAGE CODE - Auto-generated Python code that reflects current settings
    7. HELP & INFO - Explanations of each mode and parameter
    
    No return value. Displays interactive widgets directly in notebook cell.
    """
    
    try:
        # Import required display libraries
        import ipywidgets as widgets
        from IPython.display import display, HTML, Markdown
    except ImportError:
        # Graceful fallback if ipywidgets not available
        print("ipywidgets not installed. Install with: pip install ipywidgets")
        return
    
    # ===== WIDGET STYLING CONFIGURATION =====
    # Define common style parameters used throughout the menu
    # - description_width: Width of parameter labels (e.g., "Mode:", "Temperature:")
    # - button_width: Width of buttons (used in Quick Actions section)
    style = {
        'description_width': '120px',    # Label column width in pixels
        'button_width': '200px'          # Button width for Quick Actions
    }
    
    # ===== TITLE BANNER =====
    # Create eye-catching gradient header with emojis
    # Uses CSS gradient for visual appeal: purple to magenta
    title = HTML("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                color: white; border-radius: 10px; margin-bottom: 20px;">
        <h1>🎮 LightGPT Cheat Menu</h1>
        <p><i>Interactive Control Panel for Lightweight GPT</i></p>
    </div>
    """)
    
    # ===== SECTION 1: MODEL CONFIGURATION =====
    # Display header for model configuration section with light gray background
    display(HTML("""
    <div style="background: #f0f0f0; padding: 15px; border-radius: 8px; margin: 10px 0;">
        <h3>⚙️ MODEL CONFIGURATION</h3>
    </div>
    """))
    
    # Create toggle buttons to select model efficiency mode
    # Three options represent different computational/quality tradeoffs:
    # - Overkill: Maximum model size/quality (8 layers, 8 heads, 512 dim)
    # - Normal: Balanced approach (6 layers, 6 heads, 256 dim)
    # - Underkill: Minimal footprint for CPU/edge (2 layers, 2 heads, 64 dim)
    mode_selector = widgets.ToggleButtons(
        options=['🚀 Overkill', '⚡ Normal', '🎯 Underkill'],  # Display labels with emojis
        description='Mode:',                                    # Label shown before widget
        style=style,                                           # Apply standard styling
        button_style='info'                                    # Blue button color (info style)
    )
    
    display(widgets.Label("Select Model Mode:"))  # Instructional text above buttons
    display(mode_selector)                         # Display the toggle button widget
    
    # ===== SECTION 2: APRIL FOOLS MODE =====
    # Display header with yellow warning background (indicates this is special mode)
    display(HTML("""
    <div style="background: #fff3cd; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>🎪 APRIL FOOLS MODE</h3>
    </div>
    """))
    
    # Create toggle to enable stupidity injection
    # When enabled, the model produces chaotic, backwards reasoning
    # Perfect for fun experiments or April 1st (auto-enabled then)
    april_fools_toggle = widgets.ToggleButtons(
        options=['💡 Normal Thinking', '🤪 Stupid Mode'],  # Normal vs Chaotic
        description='Reasoning:',                           # Label displayed
        style=style,                                       # Standard styling
        button_style='warning'                             # Orange/yellow button color
    )
    
    display(widgets.Label("Enable Stupidity (for April 1st or forced chaos):"))  # Instructions
    display(april_fools_toggle)  # Display the toggle widget
    
    # ===== SECTION 3: QUICK ACTIONS =====
    # Display header with green background (indicates positive/action section)
    display(HTML("""
    <div style="background: #d4edda; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>🎯 QUICK ACTIONS</h3>
    </div>
    """))
    
    # Create horizontal box (HBox) containing action buttons side-by-side
    # This keeps buttons compact and all visible on screen
    # Each button has a tooltip that appears on hover
    action_buttons = widgets.HBox([
        # Button 1: Run quick demo of model generation
        widgets.Button(
            description='📊 Run Demo',
            button_style='success',           # Green button (success style)
            tooltip='Run quick demo'           # Hover text
        ),
        # Button 2: Show performance benchmarks
        widgets.Button(
            description='📈 Benchmarks',
            button_style='success',           # Green button
            tooltip='Show performance'         # Hover text
        ),
        # Button 3: Run April Fools silly demo
        widgets.Button(
            description='🎭 April Fools',
            button_style='danger',            # Red button (danger/alert style)
            tooltip='Run silly demo'           # Hover text
        ),
    ])
    
    display(action_buttons)  # Display all three buttons in a row
    
    # ===== SECTION 4: ADVANCED OPTIONS =====
    # Display header with light purple background (indicates advanced/technical section)
    display(HTML("""
    <div style="background: #e8dff5; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>⚙️ ADVANCED OPTIONS</h3>
    </div>
    """))
    
    # SLIDER 1: Maximum tokens to generate (sequence length)
    # Controls how long the model's response can be
    # Range: 1-128 tokens (small for lightweight model)
    # Default: 32 tokens (reasonable length without being too verbose)
    max_tokens = widgets.IntSlider(
        value=32,                                          # Default value
        min=1,                                             # Minimum allowed (at least 1 token)
        max=128,                                           # Maximum allowed (reasonable for LightGPT)
        step=1,                                            # Increment by 1 token
        description='Max Tokens:',                         # Label shown
        style=style                                        # Standard styling
    )
    
    # SLIDER 2: Temperature parameter for generation randomness
    # Controls diversity vs determinism in token selection
    # Range: 0.1-2.0 (low = deterministic, high = chaotic)
    # Default: 1.0 (standard/neutral temperature)
    temperature = widgets.FloatSlider(
        value=1.0,                                         # Default: neutral temp
        min=0.1,                                           # Min: very cold/deterministic
        max=2.0,                                           # Max: very hot/random
        step=0.1,                                          # Fine-tune in 0.1 increments
        description='Temperature:',                        # Label shown
        style=style                                        # Standard styling
    )
    
    # TOGGLE 2: Decoding strategy selection
    # Greedy: always pick highest probability token (deterministic)
    # Sampling: randomly pick tokens weighted by probability (creative)
    sample_toggle = widgets.ToggleButtons(
        options=['🎯 Greedy', '🎲 Sampling'],  # Two strategies with emojis
        description='Decoding:',                # Label shown
        style=style,                           # Standard styling
        button_style='info'                    # Blue button color
    )
    
    # Display all three advanced widgets to user
    display(max_tokens)                      # Integer slider
    display(temperature)                     # Float slider
    display(widgets.Label("Decoding Strategy:"))  # Label for toggle
    display(sample_toggle)                   # Toggle buttons
    
    # ===== SECTION 5: CURRENT SETTINGS SUMMARY =====
    # Display header with light gray background
    display(HTML("""
    <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>📋 CURRENT SETTINGS</h3>
    </div>
    """))
    
    # Create an output widget that will display the settings summary
    # This widget is updated whenever any control changes
    summary_output = widgets.Output()
    
    def update_summary(*args):
        """
        Callback function that updates the settings summary display.
        
        This function is triggered whenever any widget value changes (observed above).
        It displays a formatted ASCII-art box showing the current configuration.
        
        Args:
            *args: Unused - passed by ipywidgets observer mechanism
        """
        with summary_output:
            # Clear previous output before printing new summary
            summary_output.clear_output()
            
            # Create mapping dictionaries to convert widget values to config values
            # These maps translate emoji labels to actual configuration strings
            mode_map = {
                '🚀 Overkill': 'overkill',     # Large model
                '⚡ Normal': 'normal',          # Medium model
                '🎯 Underkill': 'underkill'    # Tiny model
            }
            april_map = {
                '💡 Normal Thinking': False,    # Normal mode
                '🤪 Stupid Mode': True          # Stupidity enabled
            }
            sample_map = {
                '🎯 Greedy': False,             # Greedy decoding
                '🎲 Sampling': True             # Sampling decoding
            }
            
            # Get current values from all widgets
            mode = mode_map.get(mode_selector.value, 'normal')
            stupid = april_map.get(april_fools_toggle.value, False)
            sample = sample_map.get(sample_toggle.value, False)
            
            # Print formatted summary with ASCII-art box
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
    
    # Register update_summary as observer for all widgets
    # This means whenever a widget value changes, update_summary is called
    mode_selector.observe(update_summary, names='value')              # Mode changed
    april_fools_toggle.observe(update_summary, names='value')          # April Fools toggled
    max_tokens.observe(update_summary, names='value')                  # Token slider moved
    temperature.observe(update_summary, names='value')                 # Temperature slider moved
    sample_toggle.observe(update_summary, names='value')               # Sampling mode changed
    
    # Display the summary output widget and trigger initial population
    display(summary_output)
    update_summary()  # Initial call to populate summary on first load
    
    # ===== SECTION 6: AUTO-GENERATED PYTHON CODE =====
    # Display header with light gray background
    display(HTML("""
    <div style="background: #f5f5f5; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>📝 USAGE CODE (Copy & Paste)</h3>
    </div>
    """))
    
    # Create output widget to display generated Python code
    # Code updates in real-time as user changes settings
    code_output = widgets.Output()
    
    def update_code(*args):
        """
        Callback function that generates Python code based on current settings.
        
        This function is triggered whenever any widget value changes.
        It generates a complete, ready-to-run Python code snippet that reflects
        the user's current selections in the cheat menu.
        
        Args:
            *args: Unused - passed by ipywidgets observer mechanism
        """
        with code_output:
            # Clear previous code output before generating new code
            code_output.clear_output()
            
            # Create mapping dictionaries (same as in update_summary)
            mode_map = {
                '🚀 Overkill': 'overkill',
                '⚡ Normal': 'normal',
                '🎯 Underkill': 'underkill'
            }
            april_map = {
                '💡 Normal Thinking': False,
                '🤪 Stupid Mode': True
            }
            sample_map = {
                '🎯 Greedy': False,
                '🎲 Sampling': True
            }
            
            # Get current values from all widgets
            mode = mode_map.get(mode_selector.value, 'normal')
            stupid = april_map.get(april_fools_toggle.value, False)
            sample = sample_map.get(sample_toggle.value, False)
            
            # Generate Python code string with current settings embedded
            # This code can be copy-pasted directly into a new cell
            code = f"""
from lightgpt import LightGPT, generate

# Initialize model with selected mode
model = LightGPT(mode='{mode}', max_seq_len=128)

# Prepare prompt by tokenizing
prompt = \"Hello LightGPT\"
prompt_ids = model.small_vocab_tokenize(prompt)

# Generate text with configured parameters
output_ids = generate(
    model,
    prompt_ids,
    max_new_tokens={max_tokens.value},        # Token limit from slider
    temperature={temperature.value},           # Temperature from slider
    sample={sample},                           # Sampling strategy
    apply_stupidity={stupid}                   # April Fools mode toggle
)

print(\"Generated:\", output_ids)
            """
            
            # Print code in markdown format for nice formatting in notebook
            print("```python")
            print(code)
            print("```")
    
    # Register update_code as observer for all widgets
    # Code regenerates whenever any setting changes
    mode_selector.observe(update_code, names='value')
    april_fools_toggle.observe(update_code, names='value')
    max_tokens.observe(update_code, names='value')
    temperature.observe(update_code, names='value')
    sample_toggle.observe(update_code, names='value')
    
    # Display the code output widget and trigger initial generation
    display(code_output)
    update_code()  # Initial call to generate default code on first load
    
    # ===== SECTION 7: HELP & INFORMATION =====
    # Display header with light blue background (indicates informational section)
    display(HTML("""
    <div style="background: #d1ecf1; padding: 15px; border-radius: 8px; margin: 20px 0;">
        <h3>❓ HELP & INFO</h3>
    </div>
    """))
    
    # Create HTML widget with help text and explanations
    # HTML widget allows rich formatting (bold, lists, etc.)
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
    display(help_text)  # Display help information to user
    
    # ===== FOOTER BANNER =====
    # Display closing message with encouragement and decorative styling
    display(HTML("""
    <div style="text-align: center; padding: 20px; background: #e9ecef; 
                border-radius: 10px; margin-top: 30px; border: 2px solid #dee2e6;">
        <p><b>LightGPT Cheat Menu</b> — Ready to generate! 🚀</p>
        <p style="font-size: 12px; color: #666;">
            Run your configured settings with the code above. Happy training! ✨
        </p>
    </div>
    """))
    # End of function - menu is now fully displayed and interactive


# ===== MODULE ENTRY POINT =====
# Uncomment the line below to run the menu when this file is executed directly
# if __name__ == '__main__':
#     create_lightgpt_cheat_menu()
if __name__ == "__main__":
    create_lightgpt_cheat_menu()
