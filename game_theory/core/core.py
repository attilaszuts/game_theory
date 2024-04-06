from abc import ABC, abstractmethod

import pandas as pd


class BaseStrategy(ABC):

    def __init__(self):
        self.name = None
        self.results = []
        self.score = 0

    @abstractmethod
    def play_turn(self) -> int:
        """Must return either 0 or 1"""
        pass

    def get_info(self, result: dict):
        """Get the results of the previous turn from the Game"""
        self.results.append(result)


class BaseGameMode(ABC):

    def __init__(self, player_one: BaseStrategy, player_two: BaseStrategy, turns: int) -> pd.DataFrame:
        """
        :param player_one:
        :param player_two:

        Each player has a choice of either cooperate (0) or defect (1). If both cooperate, both gain 3 points. If
        both defect, both gain 1 point. If one cooperates and the other defects, the defector gains 5 points and the
        cooperator gains 0 points.
        """
        self.p1 = player_one
        self.p2 = player_two
        self.results = []
        self.turns = turns

    @abstractmethod
    def evaluate_turn(self):
        """
        This method should be implemented in the child class.
        It should evaluate a turn and return the result.
        """
        pass

    def __one_turn(self):
        result = self.evaluate_turn()
        self.results.append(result)
        self.p1.get_info(result)
        self.p2.get_info(result)

    def one_turn(self):
        self.__one_turn()

    def __game(self, turns: int):
        for _ in range(turns):
            self.one_turn()
        return pd.DataFrame(self.results)

    def game(self, turns: int):
        return self.__game(turns)
