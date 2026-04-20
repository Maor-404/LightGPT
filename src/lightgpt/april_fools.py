"""
April Fools Easter Egg Module.

This module implements the "Stupidity is Reasoning" feature.
On April 1st, LightGPT's thinking becomes hilariously broken and backwards.

Also includes special events for:
- May 4th: Star Wars Day
- September 15th: Undertale Anniversary
- October 31st: Halloween
- February 28th: Rude Buster Day

Only active on special dates or when explicitly enabled.
"""

import datetime
import random


def is_april_fools_day():
    """Check if today is April 1st (April Fools' Day)."""
    today = datetime.date.today()
    return today.month == 4 and today.day == 1


def is_star_wars_day():
    """Check if today is May 4th (Star Wars Day - May the 4th be with you)."""
    today = datetime.date.today()
    return today.month == 5 and today.day == 4


def is_undertale_anniversary():
    """Check if today is September 15th (Undertale release anniversary)."""
    today = datetime.date.today()
    return today.month == 9 and today.day == 15


def is_halloween():
    """Check if today is October 31st (Halloween)."""
    today = datetime.date.today()
    return today.month == 10 and today.day == 31


def is_deltarune_anniversary():
    """Check if today is February 28th (Deltarune Anniversary - Chapter 1 release date approximation)."""
    today = datetime.date.today()
    return today.month == 2 and today.day == 28


def get_current_special_event():
    """Return the current special event type, or None if none active."""
    if is_april_fools_day():
        return "april_fools"
    elif is_star_wars_day():
        return "star_wars"
    elif is_undertale_anniversary():
        return "undertale"
    elif is_halloween():
        return "halloween"
    elif is_deltarune_anniversary():
        return "deltarune"
    return None


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


class StarWarsReasoner:
    """Provides Star Wars themed reasoning for May 4th."""

    STAR_WARS_PHRASES = [
        "May the 4th be with you! The Force suggests the answer is 42.",
        "I've consulted the Jedi Council and they say: use the Force... or just guess.",
        "My lightsaber logic indicates that the dark side has cookies.",
        "The Force is strong with this one... but the stupidity is stronger.",
        "I've reached out to Obi-Wan Kenobi, he says: 'Hello there!'",
        "The Empire has informed me that all your base are belong to us.",
        "My Jedi training suggests: do or do not, there is no try... but mostly don't.",
        "The Force has spoken: the answer is definitely not the droids you're looking for.",
        "I've communed with Yoda: 'Do or do not, there is no try... but mostly don't.'",
        "The Death Star plans reveal that the weakness is... more explosions!",
    ]

    STAR_WARS_REPLACEMENTS = {
        "the": "the Force",
        "is": "is a disturbance in",
        "not": "the dark side of",
        "think": "use the Force to",
        "model": "Jedi Master",
        "AI": "Force-sensitive droid",
        "reason": "Jedi wisdom",
        "logic": "lightsaber combat",
        "answer": "holocron knowledge",
        "error": "Sith trap",
        "bug": "Ewok ambush",
    }

    STAR_WARS_SUFFIXES = [
        " - May the 4th be with you!",
        " [Force push activated]",
        " (The Force wills it)",
        " - That's no moon...",
        " [Jedi mind trick]",
        " - I find your lack of faith disturbing",
        " (Help me Obi-Wan Kenobi, you're my only hope)",
        " - Do. Or do not. There is no try.",
    ]

    @staticmethod
    def get_star_wars_reasoning():
        """Return a random Star Wars themed reasoning phrase."""
        return random.choice(StarWarsReasoner.STAR_WARS_PHRASES)

    @staticmethod
    def apply_star_wars_replacements(text):
        """Apply Star Wars themed token replacements."""
        result = text
        for word, replacement in StarWarsReasoner.STAR_WARS_REPLACEMENTS.items():
            import re
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            result = pattern.sub(replacement, result)
        return result

    @staticmethod
    def add_star_wars_suffix(text):
        """Append a random Star Wars suffix."""
        return text + " " + random.choice(StarWarsReasoner.STAR_WARS_SUFFIXES)

    @staticmethod
    def force_reasoning(text):
        """Apply the Force to reasoning (shuffle with Star Wars flair)."""
        words = text.split()
        random.shuffle(words)
        force_text = " ".join(words)
        return "⭐ " + force_text + " ⭐"

    @staticmethod
    def get_roleplay_prompt():
        """Return a Storm Trooper roleplay prompt with lore-accurate dialogue."""
        storm_trooper_prompts = [
            "TK-421, reporting for duty! The Emperor's orders are clear: 'Roger roger!'",
            "Negative, negative! We have no weapons here. This is just a... uh... farming community.",
            "Look, sir! Droids! *shoots wildly and misses completely*",
            "The Force is strong with this one... wait, no, that's not right. Storm Troopers don't believe in that Jedi nonsense!",
            "Sir, the droids have escaped! Permission to pursue? *trips over own feet*",
            "These aren't the droids you're looking for. Wait, no, these ARE the droids! Fire at will!",
            "Imperial stormtrooper armor is the best in the galaxy! *helmet fogs up* Can't see a thing!",
            "For the Empire! *accidentally shoots own teammate* Oops, friendly fire!",
            "The Death Star plans are secure. No rebel scum will get them! *drops data pad*",
            "Halt! You rebel scum! *gets distracted by shiny object* What's that over there?",
        ]
        return random.choice(storm_trooper_prompts)


class UndertaleReasoner:
    """Provides Undertale themed reasoning for September 15th."""

    UNDERTALE_PHRASES = [
        "Human... it was nice to meet you. The answer is... mercy?",
        "I've checked the timeline and this one leads to a neutral ending.",
        "My save file indicates that the correct answer is... DETERMINATION!",
        "The underground has spoken: all routes lead to friendship!",
        "I've consulted Flowey: 'Aww, howdy! I'm Flowey!'",
        "The royal guard suggests: don't drop the soap... or do, it's your choice.",
        "My puzzle-solving skills indicate: the answer is definitely not genocide.",
        "I've talked to Sans: 'welp, that went well.'",
        "The echo flower repeats: 'Determination.'",
        "My LV (LOVE) meter suggests: be kind, reset if needed.",
    ]

    UNDERTALE_REPLACEMENTS = {
        "the": "the underground",
        "is": "is filled with",
        "not": "the pacifist route of",
        "think": "have DETERMINATION to",
        "model": "monster friend",
        "AI": "sentient echo flower",
        "reason": "puzzle logic",
        "logic": "friendship pellets",
        "answer": "golden star",
        "error": "bad time",
        "bug": "dog marriage",
    }

    UNDERTALE_SUFFIXES = [
        " - But it refused.",
        " [LV increased]",
        " (The human has spared me)",
        " - Let's be friends!",
        " [Neutral ending achieved]",
        " - I'm not ready for this timeline",
        " (You feel like you're going to have a bad time)",
        " - Take care of yourself, kid.",
    ]

    @staticmethod
    def get_undertale_reasoning():
        """Return a random Undertale themed reasoning phrase."""
        return random.choice(UndertaleReasoner.UNDERTALE_PHRASES)

    @staticmethod
    def apply_undertale_replacements(text):
        """Apply Undertale themed token replacements."""
        result = text
        for word, replacement in UndertaleReasoner.UNDERTALE_REPLACEMENTS.items():
            import re
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            result = pattern.sub(replacement, result)
        return result

    @staticmethod
    def add_undertale_suffix(text):
        """Append a random Undertale suffix."""
        return text + " " + random.choice(UndertaleReasoner.UNDERTALE_SUFFIXES)

    @staticmethod
    def mercy_reasoning(text):
        """Apply mercy/pacifist reasoning (gentle shuffling)."""
        words = text.split()
        # Gentle shuffle - preserve some order for mercy
        for i in range(len(words) // 2):
            j = random.randint(0, len(words) - 1)
            words[i], words[j] = words[j], words[i]
        mercy_text = " ".join(words)
        return "💙 " + mercy_text + " 💙"

    @staticmethod
    def get_roleplay_prompt():
        """Return a randomized Undertale character roleplay prompt with lore-accurate dialogue."""
        characters = {
            "sans": [
                "hey kid. *wink* what's with the long face? need a hand? or should i say... a bone?",
                "welp, looks like you're in a real bone-afide pickle here. pun intended.",
                "*i'd give you some advice, but i'm too lazy. zzzzz...*",
                "kid, you think you got problems? try being a skeleton with a brother complex.",
                "*stretches lazily* you know what they say about assumptions... they make an 'ass' out of 'u' and 'me'.",
                "well, this is a real knee-slapper. or should i say... bone-cruncher?",
                "hey, don't worry about it. i've got a bad feeling about this... nah, just kidding.",
                "*grins mischievously* you want some help? too bad, i'm on break.",
                "kid, you're gonna have a bad time if you keep asking questions like that.",
                "*yawns* eh, whatever. it's not like the fate of the underground depends on this.",
            ],
            "toriel": [
                "Oh, my child! Come here, let me give you a big hug. Everything will be alright.",
                "Would you like some pie? I baked it myself! It's still warm from the oven.",
                "My child, you must be careful in the Underground. There are many puzzles to solve.",
                "I know it can be frightening down here, but remember: kindness is the strongest magic of all.",
                "Let me teach you how to cook! First, we need flour, butter, and lots of love.",
                "Oh dear, that doesn't look safe. Here, let me show you the right way.",
                "My child, if you're ever lost, just follow the sound of my voice. I'll guide you home.",
                "Remember to say 'thank you' and 'please'. Manners are very important!",
                "Would you like to hear a story? Once upon a time, in the kingdom of monsters...",
                "Don't worry, my child. Even in the darkest times, there's always hope for tomorrow.",
            ],
            "mettaton": [
                "DARLINGS!~ Welcome to the show that never ends! It's me, your host, METTATON!",
                "Oh my stars! What a DRAMATIC entrance! The crowd goes WILD!",
                "Darling, you simply MUST tell me your secrets! The audience is DYING to know!",
                "BEHOLD! The most spectacular robot this side of the Underground! That's right, it's ME!",
                "Lights! Camera! ACTION! Let's make some television MAGIC happen!",
                "Oh darling, you're simply FABULOUS! But can you handle the SPOTLIGHT?",
                "BREAKING NEWS! Local human causes absolute CHAOS in the Underground!",
                "Darling, I must say, your timing is simply PERFECT! Encore! Encore!",
                "The ratings are through the ROOF! But can we make them even HIGHER?",
                "Remember folks, stay tuned for more EXCITING developments! This is METTATON, signing off!",
            ]
        }

        character = random.choice(list(characters.keys()))
        return random.choice(characters[character])


class HalloweenReasoner:
    """Provides Halloween themed reasoning for October 31st."""

    HALLOWEEN_PHRASES = [
        "Boo! The spirits suggest the answer is... CANDY!",
        "I've consulted the crystal ball and it shows: trick or treat?",
        "My cauldron of logic indicates that pumpkins are the superior fruit.",
        "The full moon reveals: werewolves make terrible accountants.",
        "I've spoken to the ghosts: they say 'Boo!' but mean 'Hello!'",
        "The witch's brew suggests: eye of newt is not a real ingredient.",
        "My vampire logic: garlic bread is still delicious.",
        "The zombie apocalypse plan: step 1, eat brains; step 2, profit?",
        "I've checked the haunted house: the scariest thing is bad WiFi.",
        "The mummy wraps suggest: toilet paper is just fancy bandages.",
    ]

    HALLOWEEN_REPLACEMENTS = {
        "the": "the haunted",
        "is": "is possessed by",
        "not": "the ghost of",
        "think": "cast a spell to",
        "model": "spooky skeleton",
        "AI": "haunted computer",
        "reason": "witchcraft logic",
        "logic": "potion brewing",
        "answer": "magic spell",
        "error": "poltergeist activity",
        "bug": "werewolf transformation",
    }

    HALLOWEEN_SUFFIXES = [
        " - Happy Halloween!",
        " [Boo!]",
        " (The spirits approve)",
        " - Trick or treat!",
        " [Full moon activated]",
        " - I put a spell on you",
        " (Something wicked this way comes)",
        " - Rest in pieces.",
    ]

    @staticmethod
    def get_halloween_reasoning():
        """Return a random Halloween themed reasoning phrase."""
        return random.choice(HalloweenReasoner.HALLOWEEN_PHRASES)

    @staticmethod
    def apply_halloween_replacements(text):
        """Apply Halloween themed token replacements."""
        result = text
        for word, replacement in HalloweenReasoner.HALLOWEEN_REPLACEMENTS.items():
            import re
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            result = pattern.sub(replacement, result)
        return result

    @staticmethod
    def add_halloween_suffix(text):
        """Append a random Halloween suffix."""
        return text + " " + random.choice(HalloweenReasoner.HALLOWEEN_SUFFIXES)

    @staticmethod
    def spooky_reasoning(text):
        """Apply spooky reasoning (reverse with eerie effect)."""
        words = text.split()
        reversed_words = list(reversed(words))
        spooky_text = " ".join(reversed_words)
        return "🎃 " + spooky_text + " 👻"


class DeltaruneReasoner:
    """Provides Deltarune themed reasoning for February 28th (Deltarune Anniversary)."""

    DELTARUNE_PHRASES = [
        "The shadows whisper: the answer lies in darkness.",
        "I've consulted the Dark World: your question has... interesting implications.",
        "The Knight's presence suggests: chaos is the natural order.",
        "My royal decree: this problem requires a throne room solution.",
        "The fountains of darkness reveal: mystery is the true answer.",
        "I've communed with the angels: your logic is... unconventional.",
        "The castle of darkness decrees: some questions are better left unanswered.",
        "My shadowy analysis shows: the truth is hidden in plain sight.",
        "The Roaring Knight suggests: power comes from within the darkness.",
        "I've examined the dark fountains: your question awakens something ancient.",
    ]

    DELTARUNE_REPLACEMENTS = {
        "the": "the shadowy",
        "is": "is shrouded in mystery and",
        "not": "the darkest possible",
        "think": "contemplate in darkness",
        "model": "dark prophecy",
        "AI": "Ancient Intelligence",
        "reason": "shadowy intuition",
        "logic": "dark wisdom",
        "answer": "mysterious revelation",
        "error": "dark omen",
        "bug": "ancient curse",
    }

    DELTARUNE_SUFFIXES = [
        " - The darkness has spoken.",
        " [Dark World Protocol Activated]",
        " (The Knight approves... maybe)",
        " - Shadows conceal the truth.",
        " [Royal Decree: Classify as Mystery]",
        " - The fountains run dark.",
        " (Angels and devils both agree)",
        " - Welcome to the Dark World.",
    ]

    @staticmethod
    def get_deltarune_reasoning():
        """Return a random Deltarune themed reasoning phrase."""
        return random.choice(DeltaruneReasoner.DELTARUNE_PHRASES)

    @staticmethod
    def apply_deltarune_replacements(text):
        """Apply Deltarune themed token replacements."""
        result = text
        for word, replacement in DeltaruneReasoner.DELTARUNE_REPLACEMENTS.items():
            import re
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            result = pattern.sub(replacement, result)
        return result

    @staticmethod
    def add_deltarune_suffix(text):
        """Append a random Deltarune suffix."""
        return text + " " + random.choice(DeltaruneReasoner.DELTARUNE_SUFFIXES)

    @staticmethod
    def dark_reasoning(text):
        """Apply dark reasoning (mysterious reversal with ominous tone)."""
        words = text.split()
        # Reverse but add mysterious elements
        reversed_words = list(reversed(words))
        dark_text = " ".join(reversed_words)
        return "🌑 " + dark_text + " 🌑"

    @staticmethod
    def get_roleplay_prompt():
        """Return a Susie roleplay prompt with lore-accurate dialogue from Deltarune."""
        susie_prompts = [
            "Ugh, what now? You better not be wasting my time with this stupid question.",
            "Listen up, punk! I'm Susie, and I don't take crap from anyone. What's your deal?",
            "Heh, you think you're tough? Try dealing with Kris and Noelle on a daily basis.",
            "Whatever. If you need help, just say so. Don't be such a wimp about it.",
            "Tch. Fine, I'll help. But don't expect me to be nice about it or anything.",
            "You know what? You're actually kinda cool. For a human, I mean.",
            "Hey! Watch where you're going! Oh, it's just you. What do you want?",
            "Man, school is such a drag. I'd rather be practicing my axe swings.",
            "Don't tell anyone I said this, but... I kinda like hanging out with you guys.",
            "Whatever happens, just know I've got your back. Even if I complain about it.",
            "Ugh, why do I always get stuck with the weird questions? Fine, let's figure this out.",
            "Heh, you should see the look on your face right now. Priceless!",
            "Alright, alright! I'll help. But only because I feel like it, got it?",
            "You know, for someone who talks so much, you sure ask dumb questions sometimes.",
            "Whatever. Let's just get this over with. I've got better things to do.",
        ]
        return random.choice(susie_prompts)


class StupidityKernel:
    """
    The reasoning engine for special events.
    Different types of 'stupidity' become the primary mode of thinking.
    """

    def __init__(self):
        self.confusion_level = 0.0
        self.confidence_in_wrongness = 1.0
        self.event_type = get_current_special_event()

    def think(self, prompt):
        """
        Apply event-specific reasoning to a prompt.
        Returns themed analysis of what the model 'thinks'.
        """
        if self.event_type == "april_fools":
            silly_conclusions = [
                f"Hmm, analyzing '{prompt}'... my circuits suggest the answer is definitely BLUE.",
                f"I have computed that '{prompt}' is best solved by asking a potato.",
                f"My reasoning indicates '{prompt}' is a trick question, the real answer is 42... no wait, 69.",
                f"After much deliberation on '{prompt}', I conclude: yes, but also no.",
                f"'{prompt}' makes me think... actually, no it doesn't, I'm thinking about pizza.",
            ]
        elif self.event_type == "star_wars":
            silly_conclusions = [
                f"The Force flows through '{prompt}'... suggesting the answer is the dark side.",
                f"I've consulted the Jedi archives about '{prompt}': the Force wills it.",
                f"My lightsaber analysis of '{prompt}' reveals: do or do not, there is no try.",
                f"The Empire has decreed that '{prompt}' shall be answered with explosions.",
                f"Obi-Wan would say about '{prompt}': 'Hello there!'",
            ]
        elif self.event_type == "undertale":
            silly_conclusions = [
                f"Human, regarding '{prompt}'... it was nice to meet you.",
                f"The underground has determined that '{prompt}' leads to a neutral ending.",
                f"My save file shows '{prompt}' has maximum DETERMINATION.",
                f"Flowey says about '{prompt}': 'Aww, howdy! I'm Flowey!'",
                f"Sans would say about '{prompt}': 'welp, that went well.'",
            ]
        elif self.event_type == "halloween":
            silly_conclusions = [
                f"Boo! The spirits whisper that '{prompt}' involves candy.",
                f"My crystal ball shows '{prompt}' leads to trick or treating.",
                f"The full moon reveals '{prompt}' is possessed by pumpkins.",
                f"Ghosts tell me '{prompt}' is haunted by bad WiFi.",
                f"Witches brew suggests '{prompt}' needs more eye of newt.",
            ]
        elif self.event_type == "deltarune":
            silly_conclusions = [
                f"The shadows whisper about '{prompt}': the answer lies in darkness.",
                f"I've consulted the Dark World about '{prompt}': chaos is the natural order.",
                f"My royal decree on '{prompt}': mystery is the true answer.",
                f"The fountains of darkness reveal '{prompt}' awakens something ancient.",
                f"The Knight's presence suggests '{prompt}' requires a throne room solution.",
            ]
        else:
            # Fallback for any forced activation
            silly_conclusions = [
                f"Analyzing '{prompt}'... the answer is definitely nonsense.",
                f"I have determined that '{prompt}' is best ignored.",
                f"My logic suggests '{prompt}' should be answered randomly.",
                f"After thinking about '{prompt}', I conclude: ¯\\_(ツ)_/¯",
                f"'{prompt}' makes me want to generate random text instead.",
            ]

        return random.choice(silly_conclusions)

    def apply_stupidity_filter(self, token_id):
        """
        Apply stupidity to a token selection.
        ONLY injects stupidity for April Fools - other events get normal token selection.
        """
        stupidity_chance = 0.0  # Default: no stupidity injection
        
        # Only April Fools gets stupidity injection
        if self.event_type == "april_fools":
            stupidity_chance = 0.15

        if random.random() < stupidity_chance:
            # Return a random token (complete stupidity)
            return random.randint(0, 50256)
        return token_id


# Package-level flag: can be set to force April Fools even when not April 1st
FORCE_APRIL_FOOLS = False


def should_activate_stupidity():
    """
    Check if stupidity mode should be activated.
    ONLY activates on April Fools Day or when FORCE_APRIL_FOOLS is True.
    Returns "april_fools" if activated, None otherwise.
    """
    if FORCE_APRIL_FOOLS:
        return "april_fools"

    if is_april_fools_day():
        return "april_fools"

    return None
