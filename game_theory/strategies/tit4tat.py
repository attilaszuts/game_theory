from game_theory.core import BaseStrategy


class Tit4tat(BaseStrategy):

    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__

    def play_turn(self):
        if self.results:
            return self.make_decision()
        return 0

    def make_decision(self):
        """Make a decision based on the previous turn"""
        if self.results[-1][f"{self.name}_gain"] == 0 or self.results[-1][f"{self.name}_gain"] == 1:
            return 1
        return 0
