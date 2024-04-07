import random

from game_theory.game_modes import ClassicPrisonersDilemma

class NoisyPrisonersDilemma(ClassicPrisonersDilemma):

    def __init__(self, player_one, player_two, turns, noise):
        """
        :param player_one:
        :param player_two:
        :param turns:
        :param noise: The probability that a player will make the wrong choice
        """
        super().__init__(player_one, player_two, turns)
        self.noise = noise

    def evaluate_turn(self, p1_choice, p2_choice):
        if random.random() < self.noise:
            p1_choice = 1 - p1_choice
            p2_choice = 1 - p2_choice
        return super().evaluate_turn(p1_choice, p2_choice)