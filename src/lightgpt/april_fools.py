"""
April Fools Easter Egg Module.

This module implements the "Stupidity is Reasoning" feature.
On April 1st, LightGPT's thinking becomes hilariously broken and backwards.

Only active on April 1st (month=4, day=1) or when explicitly enabled.
"""

import datetime
import random


def is_april_fools_day():
    """Check if today is April 1st (April Fools' Day)."""
    today = datetime.date.today()
    return today.month == 4 and today.day == 1


class AprilFoolsReasoner:
    """Provides absurd 'reasoning' logic for April Fools Day."""

    SILLY_THINKING_PHRASES = [
        "Wait... if light has GPT, then GPT must be heavy? Therefore LightGPT is a paradox!",
        "I've thought about this deeply and the answer is clearly BANANA.",
        "The reasoning engine has determined: backwards is the new forwards!",
        "After extensive computation (2ms), I conclude that numbers are made of yams.",
        "My logic circuits indicate that the color purple tastes like Thursdays.",
        "I have calculated that if you add 2+2, you get 🦆.",
        "Error corrected: 1.0 actually equals potato.",
        "The universe has informed me that all roads lead to confused roadmaps.",
        "My neural networks suggest that gravity is just a hoax invented by heavy things.",
        "I've reasoned that stupidity is actually high intelligence in disguise.",
        "After much thought: does AI even eat breakfast? This model does.",
        "Confidently incorrect: the sky is definitely underground.",
        "My deep reasoning suggests: if a tree falls in a forest, it's probably laughing at me.",
        "I have scienced the science and concluded: MORE SCIENCE will not help.",
        "The thinking is that thinking is overrated; let's just guess.",
        "Probability analysis: there's a 100% chance I'm making this up.",
    ]

    SILLY_TOKEN_REPLACEMENTS = {
        "the": "the definitely-not-suspicious",
        "is": "might-probably-be",
        "not": "totally-definitely",
        "think": "don't-not-think",
        "model": "sentient blob of computation",
        "AI": "Advanced Incorrectness",
        "reason": "chaotic guessing",
        "logic": "vibes",
        "answer": "confident guess",
        "error": "feature",
        "bug": "undocumented behavior",
    }

    SILLY_SUFFIXES = [
        " ...or does it? (it doesn't)",
        " [citation needed from alternate universe]",
        " (probably wrong lol)",
        " - ask a banana, it knows better",
        " (I have no idea what I'm talking about)",
        " [backwards reasoning enabled]",
        " (trust me bro)",
        " - also, birds aren't real",
    ]

    @staticmethod
    def get_silly_reasoning():
        """Return a random absurd reasoning phrase."""
        return random.choice(AprilFoolsReasoner.SILLY_THINKING_PHRASES)

    @staticmethod
    def apply_silly_token_replacements(text):
        """Apply ridiculous token replacements to text."""
        result = text
        for word, replacement in AprilFoolsReasoner.SILLY_TOKEN_REPLACEMENTS.items():
            # Replace case-insensitive
            import re
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            result = pattern.sub(replacement, result)
        return result

    @staticmethod
    def add_silly_suffix(text):
        """Append a random silly suffix to text."""
        return text + " " + random.choice(AprilFoolsReasoner.SILLY_SUFFIXES)

    @staticmethod
    def backwards_reasoning(text):
        """Reverse the logic (literally reverse and mangle)."""
        words = text.split()
        # Shuffle and reverse with silly twist
        random.shuffle(words)
        reversed_text = " ".join(reversed(words))
        return "🤔 " + reversed_text + " 🤔"

    @staticmethod
    def inject_stupidity(text, intensity=0.5):
        """
        Apply varying levels of 'stupidity' to generated text.
        
        intensity: 0.0 = normal, 1.0 = maximum stupidity
        """
        if intensity <= 0:
            return text

        # Progressive stupidity levels
        if intensity > 0.7:
            # Maximum stupidity: backwards reasoning
            text = AprilFoolsReasoner.backwards_reasoning(text)
        elif intensity > 0.4:
            # High stupidity: token replacements + suffix
            text = AprilFoolsReasoner.apply_silly_token_replacements(text)
            text = AprilFoolsReasoner.add_silly_suffix(text)
        else:
            # Light stupidity: just add reasoning
            text = text + " " + AprilFoolsReasoner.get_silly_reasoning()

        return text


class StupidityKernel:
    """
    The reasoning engine for April Fools.
    Stupidity becomes the primary mode of thinking.
    """

    def __init__(self):
        self.confusion_level = 0.0
        self.confidence_in_wrongness = 1.0

    def think(self, prompt):
        """
        Apply stupidity-based reasoning to a prompt.
        Returns absurd analysis of what the model 'thinks'.
        """
        silly_conclusions = [
            f"Hmm, analyzing '{prompt}'... my circuits suggest the answer is definitely BLUE.",
            f"I have computed that '{prompt}' is best solved by asking a potato.",
            f"My reasoning indicates '{prompt}' is a trick question, the real answer is 42... no wait, 69.",
            f"After much deliberation on '{prompt}', I conclude: yes, but also no.",
            f"'{prompt}' makes me think... actually, no it doesn't, I'm thinking about pizza.",
        ]
        return random.choice(silly_conclusions)

    def apply_stupidity_filter(self, token_id):
        """
        Apply stupidity to a token selection.
        Sometimes return nonsense instead of the predicted token.
        """
        if random.random() < 0.15:  # 15% chance of stupidity injection
            # Return a random token (completely stupid choice)
            return random.randint(0, 50256)
        return token_id


# Package-level flag: can be set to force April Fools even when not April 1st
FORCE_APRIL_FOOLS = False


def should_activate_stupidity():
    """Check if stupidity mode should be activated."""
    return FORCE_APRIL_FOOLS or is_april_fools_day()
