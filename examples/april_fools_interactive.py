"""
April Fools Interactive Demo: LightGPT Stupidity Edition

This demo shows LightGPT generating text while the stupidity engine is active.
Perfect for April 1st when intelligence is inverted!

Run with: python examples/april_fools_interactive.py
"""

import sys
import torch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from lightgpt import LightGPT, generate
from lightgpt.april_fools import (
    AprilFoolsReasoner,
    should_activate_stupidity,
    FORCE_APRIL_FOOLS,
    is_april_fools_day,
)
from lightgpt.silly_metrics import (
    SillyMetrics,
    AprilFoolsDebugger,
    print_april_fools_banner,
)


def print_separator(char="=", width=70):
    """Print a separator line."""
    print(char * width)


def demo_with_stupidity_injection():
    """Generate text with April Fools stupidity applied."""
    print("\n")
    print_separator("=")
    print("DEMO: GENERATION WITH STUPIDITY INJECTION")
    print_separator("=")

    # Load model
    print("\n🤔 Loading model in stupidity mode...\n")
    model = LightGPT(mode="normal")
    device = "cuda" if torch.cuda.is_available() else "cpu"
    model = model.to(device)
    model.eval()

    # Tokenize prompt
    prompt = "The future of AI"
    prompt_ids = LightGPT.small_vocab_tokenize(prompt)

    print(f"📝 Prompt: '{prompt}'")
    print(f"🔢 Token IDs: {prompt_ids}\n")

    # Generate with stupidity
    print("🎲 Generating text WITH stupidity injection...")
    output_ids_stupid = generate(
        model,
        prompt_ids,
        max_new_tokens=8,
        temperature=1.0,
        device=device,
        sample=True,
        apply_stupidity=True,  # Force stupidity!
    )

    print(f"✨ Output (Stupid):  {output_ids_stupid}\n")

    # Generate without stupidity (for comparison)
    print("📄 Generating text WITHOUT stupidity (for comparison)...")
    output_ids_normal = generate(
        model,
        prompt_ids,
        max_new_tokens=8,
        temperature=1.0,
        device=device,
        sample=True,
        apply_stupidity=False,
    )

    print(f"✨ Output (Normal):  {output_ids_normal}\n")

    print("🎭 Notice the difference? One has CHAOS injected!\n")


def demo_text_corruption():
    """Show text being corrupted through the stupidity pipeline."""
    print("\n")
    print_separator("=")
    print("DEMO: TEXT CORRUPTION PIPELINE")
    print_separator("=")

    original = "The model learns from data"

    print(f"\n📄 Original Text:\n  '{original}'\n")

    # Step 1: Token replacement
    replaced = AprilFoolsReasoner.apply_silly_token_replacements(original)
    print(f"Step 1 - Token Replacement:\n  '{replaced}'\n")

    # Step 2: Add silly suffix
    with_suffix = AprilFoolsReasoner.add_silly_suffix(replaced)
    print(f"Step 2 - Add Silly Suffix:\n  '{with_suffix}'\n")

    # Step 3: Full stupidity injection
    full_stupid = AprilFoolsReasoner.inject_stupidity(original, intensity=1.0)
    print(f"Step 3 - MAXIMUM STUPIDITY:\n  '{full_stupid}'\n")


def demo_metrics_and_status():
    """Show fake metrics and model status."""
    print("\n")
    print_separator("=")
    print("DEMO: FAKE METRICS & STATUS")
    print_separator("=")

    print(SillyMetrics.get_silly_metric_report())
    print(SillyMetrics.get_silly_inference_log())

    print("\n🔍 Current Model Status:")
    for _ in range(3):
        print(f"  {SillyMetrics.get_model_status()}")

    print()


def demo_decision_explanations():
    """Provide hilarious explanations for model decisions."""
    print("\n")
    print_separator("=")
    print("DEMO: DECISION EXPLANATIONS (WRONG)")
    print_separator("=")

    print("\n📊 Model Decision Analysis (100% Fabricated)\n")

    for i in range(5):
        token_id = 1000 + i * 100
        predicted = 2000 + i * 50
        explanation = AprilFoolsDebugger.explain_stupid_decision(token_id, predicted)
        print(f"  Decision {i+1}:")
        print(f"    Input Token: {token_id}")
        print(f"    Output Token: {predicted}")
        print(f"    'Explanation': {explanation}\n")


def demo_training_advice():
    """Show completely wrong training advice."""
    print("\n")
    print_separator("=")
    print("DEMO: EXPERT TRAINING ADVICE (IGNORE THIS)")
    print_separator("=")

    print("\n🎓 Top 5 Training Tips (All Wrong):\n")

    for i in range(5):
        advice = AprilFoolsDebugger.get_training_advice()
        print(f"  Tip {i+1}: {advice}\n")


def demo_model_internals():
    """Show made-up model internals."""
    print("\n")
    print_separator("=")
    print("DEMO: MODEL INTERNALS EXPLANATION")
    print_separator("=")

    print(AprilFoolsDebugger.get_model_internals_explanation())


def print_header_with_date():
    """Print a decorative header."""
    import datetime

    today = datetime.date.today()
    print(print_april_fools_banner())

    if is_april_fools_day():
        print("\n⚠️  CRITICAL ALERT: IT'S APRIL 1ST! STUPIDITY PROTOCOL ACTIVATED! ⚠️\n")
    elif FORCE_APRIL_FOOLS:
        print("\n⚠️  FORCED STUPIDITY MODE: April Fools is artificially enabled. ⚠️\n")
    else:
        print("\n💡 Note: Not April 1st, but stupidity is still available if enabled. 💡\n")

    print(f"Current Date: {today.strftime('%A, %B %d, %Y')}\n")


def main():
    """Run all April Fools interactive demos."""
    print_header_with_date()

    print("This interactive demo showcases the April Fools easter egg:\n")
    print("  • Stupidity injection into token selection")
    print("  • Silly text corruption and manipulation")
    print("  • Fake metrics and status reports")
    print("  • Hilariously wrong explanations")
    print("  • Invalid training advice")
    print("  • Made-up model internals\n")

    # Run the demos
    demo_with_stupidity_injection()
    demo_text_corruption()
    demo_metrics_and_status()
    demo_decision_explanations()
    demo_training_advice()
    demo_model_internals()

    # Final message
    print_separator("=")
    print("APRIL FOOLS DEMO COMPLETE")
    print_separator("=")
    print("""
    ✨ LightGPT's Intelligence Has Been Successfully Inverted ✨

    Key Achievements:
    ✓ Model now reasons with bananas
    ✓ Attention heads are not paying attention
    ✓ Feed-forward layers feed backwards
    ✓ Confidence metrics are wrong with style
    ✓ Maximum chaos deployed
    ✓ Trust level: CRITICALLY LOW

    To use April Fools in your own code:
    
    from lightgpt.april_fools import FORCE_APRIL_FOOLS
    import lightgpt.april_fools as af
    af.FORCE_APRIL_FOOLS = True  # Enable even when not April 1st
    
    Then generate as normal:
    output = generate(model, prompt_ids, apply_stupidity=True)

    The stupidity will be automatically applied!

    Happy April Fools! 🎉
    """)


if __name__ == "__main__":
    main()
