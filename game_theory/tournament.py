from itertools import combinations

import pandas as pd

from game_theory.core import BaseStrategy, BaseGameMode


class Tournament:

    def __init__(self, game_mode: BaseGameMode, players: list, turns: int) -> pd.DataFrame:
        self.game_mode = game_mode
        self.pairs = None
        self.players = players
        self.turns = turns
        self._create_results_df()
        self.pairs = list(combinations(self.players, 2))

    def _create_results_df(self):
        self.game_results = []

    def play_tournament(self):
        for pair in self.pairs:
            game = self.game_mode(pair[0](), pair[1](), self.turns)
            game_result = game.game(self.turns)
            self.game_results.append(game_result)

    def calculate_winner(self) -> BaseStrategy:
        """"Calculates total score across games played for each player and returns the player with the highest score"""
        for df in self.game_results:
            pass

    def tournament(self):
        self.play_tournament()
        tournament_results = self.calculate_winner()
