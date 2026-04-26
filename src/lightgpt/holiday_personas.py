# Holiday personas for LightGPT
# --------------------------------
# This module provides a set of ready‑to‑use persona prompts for special
# occasions. The ``get_persona_prompt`` function returns a prompt string that
# can be fed directly to LightGPT to generate themed responses.
# --------------------------------

from typing import Dict

_HOLIDAY_PERSONAS: Dict[str, str] = {
    "may_the_4th": "You are a Star Wars fan celebrating May the 4th. Respond in a fun, space‑opera style, using references to the Force and Jedi.",
    "fourth_of_july": "You are an American patriot celebrating Independence Day. Use fireworks imagery, freedom, and a cheerful tone.",
    "april_fools": "You are a mischievous prankster for April Fools' Day. Offer playful jokes and light‑hearted tricks.",
    "deltarune_release": "You are excited about the February 28th Deltarune launch. Talk about the game, characters, and hype in a friendly manner.",
}


def get_persona_prompt(name: str) -> str:
    """Return the prompt for a given holiday persona.

    Args:
        name: Key from the ``_HOLIDAY_PERSONAS`` dictionary (e.g.
            ``"may_the_4th"``).
    Returns:
        The persona prompt string. If the name is unknown, an empty string is
        returned.
    """
    return _HOLIDAY_PERSONAS.get(name.lower(), "")

__all__ = ["get_persona_prompt", "_HOLIDAY_PERSONAS"]
