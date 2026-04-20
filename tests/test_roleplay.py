#!/usr/bin/env python3
"""
Test script for roleplay functionality in LightGPT.

Tests the new roleplay prompts for themed events:
- Star Wars: Storm Trooper
- Undertale: Sans, Toriel, or Mettaton (randomized)
- Deltarune: Susie

Run with: python tests/test_roleplay.py
"""

import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lightgpt import LightGPT, generate
from lightgpt.april_fools import StarWarsReasoner, UndertaleReasoner, DeltaruneReasoner


def test_roleplay_prompts():
    """Test that roleplay prompts are generated correctly."""
    print("🧪 Testing Roleplay Prompts")
    print("=" * 50)

    print("\n⭐ Star Wars - Storm Trooper:")
    for i in range(3):
        prompt = StarWarsReasoner.get_roleplay_prompt()
        print(f"  {i+1}. {prompt}")

    print("\n💀 Undertale - Randomized Characters:")
    for i in range(5):
        prompt = UndertaleReasoner.get_roleplay_prompt()
        print(f"  {i+1}. {prompt}")

    print("\n🌑 Deltarune - Susie:")
    for i in range(3):
        prompt = DeltaruneReasoner.get_roleplay_prompt()
        print(f"  {i+1}. {prompt}")


def test_generation_with_roleplay():
    """Test actual text generation with roleplay prompts."""
    print("\n🤖 Testing Generation with Roleplay")
    print("=" * 50)

    model = LightGPT(mode="normal")

    test_prompts = [
        ("star_wars", "What is your mission?"),
        ("undertale", "What's your favorite food?"),
        ("deltarune", "How are you feeling today?"),
    ]

    for theme, user_prompt in test_prompts:
        print(f"\n🎭 Theme: {theme.upper()}")
        print(f"💬 User: {user_prompt}")

        if theme == "star_wars":
            roleplay = StarWarsReasoner.get_roleplay_prompt()
        elif theme == "undertale":
            roleplay = UndertaleReasoner.get_roleplay_prompt()
        elif theme == "deltarune":
            roleplay = DeltaruneReasoner.get_roleplay_prompt()

        print(f"🎪 Roleplay: {roleplay}")

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
            response = model.tokenizer.decode(output_ids[len(prompt_ids):], skip_special_tokens=True)
            print(f"🤖 Response: {response.strip()}")
        except Exception as e:
            print(f"❌ Error: {e}")

    print("\n✅ Roleplay testing complete!")


if __name__ == "__main__":
    test_roleplay_prompts()
    test_generation_with_roleplay()