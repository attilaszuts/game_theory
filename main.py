from game_theory import Tournament
from game_theory.strategies import AlwaysDefect, Tit4tat
from game_theory.game_modes import ClassicPrisonersDilemma

if __name__ == "__main__":
    Tournament(ClassicPrisonersDilemma, [Tit4tat, AlwaysDefect], 10).tournament()

