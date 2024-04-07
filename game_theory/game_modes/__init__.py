# game_theory/game_modes/__init__.py

from .classic_prisoners_dilemma import ClassicPrisonersDilemma
from .noisy_prisoners_dilemma import NoisyPrisonersDilemma
# Other game mode imports...

__all__ = ["ClassicPrisonersDilemma", "NoisyPrisonersDilemma"]  # Add other game modes to this list