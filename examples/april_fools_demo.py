"""
April Fools Demo: LightGPT Stupidity Edition

On April 1st, LightGPT's reasoning becomes hilariously broken.
Stupidity is now its primary mode of thinking!

Run this demo to witness the absurdity.
"""

import sys
import torch
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from lightgpt import LightGPT, generate
from lightgpt.april_fools import (
    AprilFoolsReasoner,
    StupidityKernel,
    is_april_fools_day,
    FORCE_APRIL_FOOLS,
)


def print_header(text):
    """Print a formatted header."""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70 + "\n")


def demo_silly_reasoning():
    """Demo 1: Showcase the absurd reasoning phrases."""
    print_header("DEMO 1: SILLY REASONING PHRASES")

    print("Watch as the model's 'thinking' becomes utterly nonsensical:\n")

    for i in range(5):
        reasoning = AprilFoolsReasoner.get_silly_reasoning()
        print(f"  [{i+1}] {reasoning}")

    print("\n✓ Stupidity module operational!\n")


def demo_token_replacements():
    """Demo 2: Show silly token replacements."""
    print_header("DEMO 2: SILLY TOKEN REPLACEMENTS")

    test_sentences = [
        "The model thinks about logic and error handling.",
        "AI is not supposed to make mistakes in reasoning.",
        "The answer is to not think about the problem.",
    ]

    print("Witness the mangling of normal language:\n")

    for sentence in test_sentences:
        corrupted = AprilFoolsReasoner.apply_silly_token_replacements(sentence)
        print(f"  Original:  {sentence}")
        print(f"  Corrupted: {corrupted}\n")

    print("✓ Language corruption engaged!\n")


def demo_backwards_reasoning():
    """Demo 3: Show backwards reasoning."""
    print_header("DEMO 3: BACKWARDS REASONING")

    test_text = "The light GPT model is very smart and efficient"

    print("Normal text:")
    print(f"  {test_text}\n")

    backwards = AprilFoolsReasoner.backwards_reasoning(test_text)
    print("After 'advanced thinking':")
    print(f"  {backwards}\n")

    print("✓ Neuron reversal complete!\n")


def demo_stupidity_injection():
    """Demo 4: Demonstrate text stupidity injection."""
    print_header("DEMO 4: PROGRESSIVE STUPIDITY INJECTION")

    text = "This is a normal sentence from the model."

    intensities = [0.0, 0.3, 0.5, 0.8, 1.0]

    print("Injecting stupidity at different intensities:\n")

    for intensity in intensities:
        stupid_text = AprilFoolsReasoner.inject_stupidity(text, intensity=intensity)
        print(f"  [Stupidity Level {intensity:.0%}]")
        print(f"  {stupid_text}\n")

    print("✓ Maximum stupidity achieved!\n")


def demo_stupidity_kernel():
    """Demo 5: Show the StupidityKernel in action."""
    print_header("DEMO 5: STUPIDITY KERNEL")

    kernel = StupidityKernel()

    print("Kernel thinking about various prompts:\n")

    prompts = [
        "What is the meaning of life?",
        "How does machine learning work?",
        "What is 2 + 2?",
    ]

    for prompt in prompts:
        thought = kernel.think(prompt)
        print(f"  Q: {prompt}")
        print(f"  A: {thought}\n")

    print("✓ Confused thinking protocols activated!\n")


def demo_token_stupidity():
    """Demo 6: Show random token injection."""
    print_header("DEMO 6: RANDOM TOKEN INJECTION")

    kernel = StupidityKernel()

    print("Normal token selection: token_id → predicted_token")
    print("With stupidity: some predictions get randomized\n")

    print("Simulating 20 token selections:")
    print("(X marks stupidly chosen tokens)\n")

    for i in range(20):
        original_token = 1000 + i
        selected_token = kernel.apply_stupidity_filter(original_token)

        marker = " ← STUPID!" if selected_token != original_token else ""
        print(f"  Token {i+1:2d}: {original_token} → {selected_token}{marker}")

    print("\n✓ Random nonsense successfully deployed!\n")


def main():
    """Run all April Fools demos."""
    import datetime

    today = datetime.date.today()
    is_april_1st = is_april_fools_day()

    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "🎉 LIGHTGPT APRIL FOOLS DEMO 🎉" + " " * 19 + "║")
    print("║" + " " * 68 + "║")
    print("║" + " STUPIDITY IS NOW THE PRIMARY REASONING ENGINE ".center(68) + "║")
    print("║" + " " * 68 + "║")
    print("║" + f" Today's Date: {today.strftime('%B %d, %Y')}".ljust(68) + "║")
    if is_april_1st:
        print("║" + " [🚨 APRIL FOOLS ACTIVATED - STUPIDITY MODE ENABLED] 🚨".center(68) + "║")
    elif FORCE_APRIL_FOOLS:
        print("║" + " [FORCED STUPIDITY MODE ENABLED]".center(68) + "║")
    else:
        print("║" + " [Note: Not April 1st - stupidity is optional]".center(68) + "║")
    print("╚" + "═" * 68 + "╝")

    # Run all demos
    demo_silly_reasoning()
    demo_token_replacements()
    demo_backwards_reasoning()
    demo_stupidity_injection()
    demo_stupidity_kernel()
    demo_token_stupidity()

    # Final message
    print_header("DEMO COMPLETE")
    print("✨ LightGPT's intelligence has been successfully inverted! ✨\n")
    print("The model is now:")
    print("  • Confidently incorrect")
    print("  • Hilariously backwards")
    print("  • Reasoning with bananas")
    print("  • Thinking in vibes instead of logic")
    print("  • 100% less trustworthy\n")

    print("To enable April Fools in your code, use:")
    print("  from lightgpt.april_fools import FORCE_APRIL_FOOLS")
    print("  lightgpt.april_fools.FORCE_APRIL_FOOLS = True\n")
    print("Or simply run the code on April 1st!\n")


if __name__ == "__main__":
    main()
