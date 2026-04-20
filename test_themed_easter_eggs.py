#!/usr/bin/env python3
"""
Quick test of the new themed easter eggs.
"""

import sys
print("This test script has moved to tests/test_themed_easter_eggs.py.")
sys.exit(0)
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from lightgpt.april_fools import (
    should_activate_stupidity,
    get_current_special_event,
    AprilFoolsReasoner,
    StarWarsReasoner,
    UndertaleReasoner,
    HalloweenReasoner,
    RudeBusterReasoner
)

def test_event_detection():
    """Test event detection functions."""
    print("=== Event Detection Test ===")
    current_event = get_current_special_event()
    should_activate = should_activate_stupidity()

    print(f"Current special event: {current_event}")
    print(f"Should activate stupidity: {should_activate}")
    print()

def test_reasoners():
    """Test all reasoner classes."""
    print("=== Reasoner Classes Test ===")

    reasoners = [
        ("April Fools", AprilFoolsReasoner()),
        ("Star Wars", StarWarsReasoner()),
        ("Undertale", UndertaleReasoner()),
        ("Halloween", HalloweenReasoner()),
        ("Rude Buster", RudeBusterReasoner()),
    ]

    test_text = "The model processes data"

    for name, reasoner in reasoners:
        print(f"\n{name} Reasoner:")
        print(f"  Thinking: {reasoner.think('test prompt')[:50]}...")
        print(f"  Token replacement: {reasoner.apply_silly_token_replacements(test_text)}")
        print(f"  With suffix: {reasoner.add_silly_suffix(test_text)[:60]}...")

if __name__ == "__main__":
    test_event_detection()
    test_reasoners()
    print("\n=== Test Complete ===")