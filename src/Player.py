import pprint
import random
from Choice import Choice
from Dice import Dice
from playerStatus import PlayerStatus


class Player:
    def __init__(self):
        self.score = {Choice.Brains: 0, Choice.Shotguns: 0, Choice.Footsteps: 0}
        self.number_of_rolls = 0
        self.player_status = PlayerStatus.Regular   # <-- I added this to make sure he starts as a regular status

    def increase_roll(self):
        self.number_of_rolls += 1
        """adding a simple rolling number for the player to follow"""
        print(f"you rolled {self.number_of_rolls} times")

    def increase_score(self, rolls):
        """what ever the outcome of the roll is, it will update 1 on the score"""
        for roll in rolls:
            self.score[roll] += 1
        """Checks to see if the number of rolls is 3 or more, if it is every face is equal to 2 and not 1"""
        if self.number_of_rolls >= 3:
            for extraroll in rolls:
                self.score[extraroll] += 2

    """Calculates the status of the player compered to rules of the game."""
    def calculate_status(self):
        if self.score[Choice.Brains] >= 13:
            print("Final round lets see if you can keep up the Brains!")
            return PlayerStatus.Winner

        if self.score[Choice.Shotguns] >= 3:
            print("brrrr.... you died")
            return PlayerStatus.Dead

        return PlayerStatus.Regular

    """A simple print of the score for the player to view at the end of each roll"""
    def print_score(self):
        pprint.pprint(self.score)