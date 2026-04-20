#!/usr/bin/env python3
"""
Test script for roleplay functionality in LightGPT.
This file has been moved to tests/ for a cleaner root structure.

Tests the new roleplay prompts for themed events:
- Star Wars: Storm Trooper
- Undertale: Sans, Toriel, or Mettaton (randomized)
- Deltarune: Susie

Run with: python test_roleplay.py
"""

import sys
print("This test script has moved to tests/test_roleplay.py.")
sys.exit(0)
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))

from lightgpt import LightGPT, generate
from lightgpt.april_fools import StarWarsReasoner, UndertaleReasoner, DeltaruneReasoner


def test_roleplay_prompts():
    """Test that roleplay prompts are generated correctly."""
    print("🧪 Testing Roleplay Prompts")
    print("=" * 50)

    # Test Star Wars Storm Trooper
    print("\n⭐ Star Wars - Storm Trooper:")
    for i in range(3):
        prompt = StarWarsReasoner.get_roleplay_prompt()
        print(f"  {i+1}. {prompt}")

    # Test Undertale characters
    print("\n💀 Undertale - Randomized Characters:")
    for i in range(5):
        prompt = UndertaleReasoner.get_roleplay_prompt()
        print(f"  {i+1}. {prompt}")

    # Test Deltarune Susie
    print("\n🌑 Deltarune - Susie:")
    for i in range(3):
        prompt = DeltaruneReasoner.get_roleplay_prompt()
        print(f"  {i+1}. {prompt}")


def test_generation_with_roleplay():
    """Test actual text generation with roleplay prompts."""
    print("\n🤖 Testing Generation with Roleplay")
    print("=" * 50)

    # Load model
    print("\n📦 Loading LightGPT model...")
    model = LightGPT(mode="normal")

    # Test prompts
    test_prompts = [
        ("star_wars", "What is your mission?"),
        ("undertale", "What's your favorite food?"),
        ("deltarune", "How are you feeling today?"),
    ]

    for theme, user_prompt in test_prompts:
        print(f"\n🎭 Theme: {theme.upper()}")
        print(f"💬 User: {user_prompt}")

        # Get roleplay prompt
        if theme == "star_wars":
            roleplay = StarWarsReasoner.get_roleplay_prompt()
        elif theme == "undertale":
            roleplay = UndertaleReasoner.get_roleplay_prompt()
        elif theme == "deltarune":
            roleplay = DeltaruneReasoner.get_roleplay_prompt()

        print(f"🎪 Roleplay: {roleplay}")

        # Generate response
        try:
            prompt_ids = model.tokenizer.encode(user_prompt, add_special_tokens=False)
            output_ids = generate(
                model,
                prompt_ids,
                max_new_tokens=20,
                temperature=0.8,
                sample=True,
                apply_stupidity=theme,
            )

            # Decode response
            response = model.tokenizer.decode(output_ids[len(prompt_ids):], skip_special_tokens=True)
            print(f"🤖 Response: {response.strip()}")

        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n✅ Roleplay testing complete!")


if __name__ == "__main__":
    test_roleplay_prompts()
    test_generation_with_roleplay()