#!/usr/bin/env python3
"""
Quick test of the new GPT-2 based LightGPT model and themed easter eggs.
"""

import sys
print("This test script has moved to tests/test_gpt2_lightgpt.py.")
sys.exit(0)
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lightgpt.model import LightGPT
from lightgpt.infer import generate
from lightgpt import april_fools

def test_model_loading():
    """Test if the new GPT-2 based model loads correctly."""
    print("=== Model Loading Test ===")
    try:
        model = LightGPT(mode='underkill')
        print("✅ Model loaded successfully!")
        print(f"   Config: {model.get_config()}")
        print(f"   Vocab size: {model.get_vocab_size()}")
        return True
    except Exception as e:
        print(f"❌ Model loading failed: {e}")
        return False

def test_tokenization():
    """Test tokenization with GPT-2 tokenizer."""
    print("\n=== Tokenization Test ===")
    try:
        model = LightGPT(mode='underkill')
        text = "Hello world"
        tokens = model.small_vocab_tokenize(text)
        decoded = model.decode_tokens(tokens)
        print(f"   Original: '{text}'")
        print(f"   Tokens: {tokens}")
        print(f"   Decoded: '{decoded}'")
        return True
    except Exception as e:
        print(f"❌ Tokenization failed: {e}")
        return False

def test_generation():
    """Test text generation."""
    print("\n=== Generation Test ===")
    try:
        model = LightGPT(mode='underkill')
        prompt = "The future of AI is"
        tokens = model.small_vocab_tokenize(prompt)
        print(f"   Prompt tokens: {tokens}")

        generated = generate(model, tokens, max_new_tokens=10, temperature=0.8)
        decoded = model.decode_tokens(generated)
        print(f"   Generated: '{decoded}'")
        return True
    except Exception as e:
        print(f"❌ Generation failed: {e}")
        return False

def test_easter_eggs():
    """Test easter egg detection."""
    print("\n=== Easter Egg Test ===")
    current_event = april_fools.get_current_special_event()
    should_stupidity = april_fools.should_activate_stupidity()

    print(f"   Current special event: {current_event}")
    print(f"   Should activate stupidity: {should_stupidity}")

    return True

if __name__ == "__main__":
    print("🧪 Testing New GPT-2 Based LightGPT\n")

    success = True
    success &= test_model_loading()
    success &= test_tokenization()
    success &= test_generation()
    success &= test_easter_eggs()

    print(f"\n{'🎉 All tests passed!' if success else '❌ Some tests failed!'}")