#!/usr/bin/env python3
"""
Quick test of the new themed easter eggs.
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from lightgpt.april_fools import (
    should_activate_stupidity,
    get_current_special_event,
    AprilFoolsReasoner,
    StarWarsReasoner,
    UndertaleReasoner,
    HalloweenReasoner,
    DeltaruneReasoner,
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
        ("Deltarune", DeltaruneReasoner()),
    ]

    test_text = "The model processes data"

    for name, reasoner in reasoners:
        print(f"\n{name} Reasoner:")
        if hasattr(reasoner, 'get_' + name.lower().replace(' ', '_') + '_reasoning'):
            # Generic introspection fallback
            pass
        print(f"  Reasoning snippet: {reasoner.__class__.__name__}")

        if name == 'April Fools':
            print(f"  Sample reasoning: {reasoner.get_silly_reasoning()}")
            print(f"  Token replacement: {reasoner.apply_silly_token_replacements(test_text)}")
            print(f"  Suffix: {reasoner.add_silly_suffix(test_text)}")
        elif name == 'Star Wars':
            print(f"  Sample reasoning: {reasoner.get_star_wars_reasoning()}")
            print(f"  Token replacement: {reasoner.apply_star_wars_replacements(test_text)}")
            print(f"  Suffix: {reasoner.add_star_wars_suffix(test_text)}")
        elif name == 'Undertale':
            print(f"  Sample reasoning: {reasoner.get_undertale_reasoning()}")
            print(f"  Token replacement: {reasoner.apply_undertale_replacements(test_text)}")
            print(f"  Suffix: {reasoner.add_undertale_suffix(test_text)}")
        elif name == 'Halloween':
            print(f"  Sample reasoning: {reasoner.get_halloween_reasoning()}")
            print(f"  Token replacement: {reasoner.apply_halloween_replacements(test_text)}")
            print(f"  Suffix: {reasoner.add_halloween_suffix(test_text)}")
        elif name == 'Deltarune':
            print(f"  Sample reasoning: {reasoner.get_deltarune_reasoning()}")
            print(f"  Token replacement: {reasoner.apply_deltarune_replacements(test_text)}")
            print(f"  Suffix: {reasoner.add_deltarune_suffix(test_text)}")


if __name__ == "__main__":
    test_event_detection()
    test_reasoners()
    print("\n=== Test Complete ===")