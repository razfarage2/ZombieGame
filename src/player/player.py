import pprint
import random
from src.dice.choice import Choice
from src.player.player_status import PlayerStatus
from src.util.util import generic_question


class Player:
    def __init__(self, name=None):
        self.name = self.gen_names()
        self.status = PlayerStatus.Regular
        self.score = {Choice.Brains: 0, Choice.Shotguns: 0, Choice.Footsteps: 0}
        self.number_of_rolls = 0

    def gen_names(self):
        names = ["Alice", "Bob", "Charlie", "David", "Emily", "Frank"]
        return names[random.randrange(len(names))]

    def increase_roll(self):
        self.number_of_rolls += 1
        """adding a simple rolling number for the player to follow"""
        print(f"you rolled {self.number_of_rolls} times")

    def increase_score(self, rolls):
        """what ever the outcome of the roll is, it will update 1 on the score"""
        for roll in rolls:
            self.score[roll] += 1
        if self.number_of_rolls >= 3:
            for extraroll in rolls:
                self.score[extraroll] += 2

    """Calculates the status of the player compered to rules of the game."""
    def calculate_status(self):
        if self.score[Choice.Brains] >= 3:
            self.status = PlayerStatus.Winner
        elif self.score[Choice.Shotguns] >= 300:
            # print("BAM..you died from a gunshot")
            self.status = PlayerStatus.Dead
        else:
            self.status = PlayerStatus.Regular
        return self.status

    """A simple print of the score for the player to view at the end of each roll"""
    def print_score(self):
        pprint.pprint(self.score)

    """Resets the number of rolls"""
    def reset_rolls(self):
        self.number_of_rolls = 0
    """Checks to see the player number of rolls and status to decide if he has the option to throw"""
    def should_throw(self):
        if self.number_of_rolls == 0:
            return True
        if self.calculate_status() == PlayerStatus.Regular:
            return generic_question("Do you want to throw again? (y/n)",no_answer="Let's move on to the next player then")

