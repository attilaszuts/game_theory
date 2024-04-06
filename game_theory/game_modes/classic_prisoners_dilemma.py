import pandas as pd

from game_theory.core import BaseStrategy, BaseGameMode


class ClassicPrisonersDilemma(BaseGameMode):

    def __init__(self, player_one: BaseStrategy, player_two: BaseStrategy, turns: int) -> pd.DataFrame:
        """
        :param player_one:
        :param player_two:

        For each turn the choice of each player and the final score will be recorded. And the running total for the
        game.

        Example for turn 1:
        {
            "p1_choice": 0,
            "p2_choice": 1,
            "p1_gain": 0,
            "p2_gain": 5,
            "p1_total": 0,
            "p2_total": 5
        }

        Each player has a choice of either cooperate (0) or defect (1). If both cooperate, both gain 3 points. If
        both defect, both gain 1 point. If one cooperates and the other defects, the defector gains 5 points and the
        cooperator gains 0 points.
        """
        super().__init__(player_one, player_two, turns)

    def evaluate_turn(self):
        one = self.p1.play_turn()
        two = self.p2.play_turn()
        result = {
            f"{self.p1.name}_choice": one,
            f"{self.p2.name}_choice": two
        }
        if one == 0 and two == 0:
            result[f"{self.p1.name}_gain"] = 3
            result[f"{self.p2.name}_gain"] = 3
        elif one == 0 and two == 1:
            result[f"{self.p1.name}_gain"] = 0
            result[f"{self.p2.name}_gain"] = 5
        elif one == 1 and two == 0:
            result[f"{self.p1.name}_gain"] = 5
            result[f"{self.p2.name}_gain"] = 0
        else:
            result[f"{self.p1.name}_gain"] = 1
            result[f"{self.p2.name}_gain"] = 1

        result[f"{self.p1.name}_total"] = self.results[-1][f"{self.p1.name}_total"] + result[
            f"{self.p1.name}_gain"] if self.results else result[f"{self.p1.name}_gain"]
        result[f"{self.p2.name}_total"] = self.results[-1][f"{self.p2.name}_total"] + result[
            f"{self.p2.name}_gain"] if self.results else result[f"{self.p2.name}_gain"]

        return result

