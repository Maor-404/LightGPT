# LightGPT package
from .model import LightGPT, MODE_CONFIGS
from .infer import generate

# the easter egg is kept private and only revealed by a very specific hidden attribute
import base64

_secret_pain_phrase = "T25seSB0aGUgcGF0aCB0aHJvdWdoIHBhaW4gcmV2ZWFscyB0aGUgd2F5Lg=="

def __getattr__(name):
    if name == "_only_true_pain":
        return base64.b64decode(_secret_pain_phrase).decode("utf-8")
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
