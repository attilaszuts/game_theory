from game_theory.core import BaseStrategy


class AlwaysDefect(BaseStrategy):

    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__

    def play_turn(self):
        """0 for cooperate, 1 for defect"""
        return 1
