"""
April Fools Metrics Module

Track and report hilariously wrong statistics about LightGPT's performance.
All metrics are confidently incorrect.
"""

import random
from datetime import datetime


class SillyMetrics:
    """Generate absurd performance metrics."""

    SILLY_UNITS = [
        "bananas per second",
        "chaos units (CU)",
        "confidence levels",
        "levels of confusion",
        "potato equivalents",
        "vibes",
        "backwards calculations",
        "sideways thoughts",
        "confused neurons",
        "existential crises",
    ]

    SILLY_METRICS = {
        "Reasoning IQ": -42,
        "Logic Accuracy": "Yes",
        "Thinking Speed": "Backwards",
        "Confidence Level": "Absolute",
        "Error Rate": "Intentional",
        "Correctness Score": "Confidently Wrong",
        "Brain Power": "Potato-equivalent",
        "Common Sense": 0.0,
        "Vibes": "Immaculate",
        "Stupidity Multiplier": 999.9,
        "Backwards-ness": "Maximum",
        "Reality Comprehension": "Nonexistent",
    }

    @staticmethod
    def get_silly_metric_report():
        """Generate a completely bogus metric report."""
        report = "\n📊 PERFORMANCE METRICS (ABSOLUTELY UNRELIABLE)\n"
        report += "=" * 60 + "\n\n"

        for metric_name, metric_value in SillyMetrics.SILLY_METRICS.items():
            if isinstance(metric_value, (int, float)):
                unit = random.choice(SillyMetrics.SILLY_UNITS)
                report += f"  {metric_name:.<40} {metric_value} {unit}\n"
            else:
                report += f"  {metric_name:.<40} {metric_value}\n"

        report += "\n" + "=" * 60 + "\n"
        return report

    @staticmethod
    def get_silly_inference_log():
        """Generate a fake inference log full of absurdities."""
        logs = [
            "⚠️  Token 42: Decided it was a banana",
            "⚠️  Token 69: Confused philosophy with physics",
            "⚠️  Token 100: Accidentally thought backwards",
            "⚠️  Neuron cluster 3.14: On coffee break",
            "⚠️  Attention head 7: Not paying attention",
            "⚠️  Feed-forward layer: Feeding backwards instead",
            "⚠️  Softmax computation: Applied Hardmin instead (oops)",
            "⚠️  Gradient: Calculated in imaginary numbers",
            "⚠️  Loss function: Gained function actually",
            "⚠️  Optimization: Successfully optimized chaos",
            "⚠️  Memory: Forgot what it was doing",
            "⚠️  Confidence: Maxed out at 'Wrong'",
        ]

        report = "\n📝 INFERENCE LOG (HILARIOUSLY BROKEN)\n"
        report += "=" * 60 + "\n\n"

        # Show random logs
        selected_logs = random.sample(logs, min(6, len(logs)))
        for log in sorted(selected_logs):
            report += f"  {log}\n"

        report += "\n" + "=" * 60 + "\n"
        return report

    @staticmethod
    def get_model_status():
        """Get the current model status during April Fools."""
        statuses = [
            "Status: 🤔 Confidently Confused",
            "Status: 🎭 Method Acting as a Stupid Model",
            "Status: 🌀 Spinning in Circles (Literally)",
            "Status: 🥔 Thinking with Potatoes",
            "Status: 🎲 Random Number Generator Mode",
            "Status: 🔄 Running Backwards Successfully",
            "Status: 🎪 Circus Mode Enabled",
            "Status: 🌙 Operating Under a Different Moon",
            "Status: ⚡ Chaos Engine Activated",
            "Status: 🦆 Quack Computing Enabled",
        ]
        return random.choice(statuses)


class AprilFoolsDebugger:
    """Provide debug information during April Fools stupidity."""

    @staticmethod
    def explain_stupid_decision(token_id, predicted_token):
        """Generate a hilariously wrong explanation for a prediction."""
        explanations = [
            f"Token {predicted_token} was chosen because it's purple (obviously).",
            f"The model detected that {token_id} is divisible by... wait, are we dividing?",
            f"After considering {token_id} alternatives, {predicted_token} felt right.",
            f"Token {predicted_token} was selected by popular vote (1 vote: the model itself).",
            f"My neurons said: {predicted_token}. I don't ask questions anymore.",
            f"Random number generator blessed {predicted_token} with its chaos.",
            f"Backwards logic suggests: if {token_id}, then definitely {predicted_token}!",
            f"The model flipped a coin and got {predicted_token} (coins don't have logic).",
        ]
        return random.choice(explanations)

    @staticmethod
    def get_training_advice():
        """Provide completely wrong training advice."""
        advice = [
            "Pro tip: Subtract your loss function instead of minimizing it!",
            "For better results, train with negative learning rate!",
            "Always backpropagate forwards instead - it's faster!",
            "Use only random data for training - diversity is overrated!",
            "Skip normalization - let chaos reign!",
            "Maximize loss instead of minimizing it - trust me bro!",
            "Gradient descent? Try gradient sideways!",
            "Shuffle data? Never heard of her!",
            "Validation set? We don't do that here!",
            "Hyperparameter tuning? Just use all 1s!",
        ]
        return random.choice(advice)

    @staticmethod
    def get_model_internals_explanation():
        """Explain what's supposedly happening inside the model."""
        explanations = """
        🧠 MODEL INTERNALS EXPLANATION (100% MADE UP)
        
        Layer 1 (Token Embedding): Converts input to philosophical questions
        Layer 2 (Attention): Not paying attention (on purpose)
        Layer 3 (Feed-Forward): Feeds backwards through time
        Layer 4 (Normalization): Violently denormalizes for chaos
        Layer 5 (Confusion): Intentionally mixes up all signals
        Output Layer: Screams random numbers at maximum volume
        
        The thinking process:
        1. Read input (but ignore it)
        2. Consult the banana dimension
        3. Ask the potato oracle
        4. Flip a cosmic coin
        5. Output whatever feels wrong
        6. Celebrate the magnificent failure
        """
        return explanations


def print_april_fools_banner():
    """Print an ASCII art banner for April Fools."""
    banner = """
    ╔═══════════════════════════════════════════════════════════════╗
    ║                                                               ║
    ║            🎪 APRIL FOOLS: STUPIDITY ENGAGED 🎪             ║
    ║                                                               ║
    ║   LightGPT Has Achieved: MAXIMUM INTELLIGENCE INVERSION      ║
    ║                                                               ║
    ║    Your Model Now Reasons With:                              ║
    ║    • Bananas as primary data structure                       ║
    ║    • Vibes instead of vectors                                ║
    ║    • Confidence in being wrong                               ║
    ║    • Potato-based neural networks                            ║
    ║                                                               ║
    ║    Trust Level: 💀 CRITICAL 💀                              ║
    ║                                                               ║
    ╚═══════════════════════════════════════════════════════════════╝
    """
    return banner
