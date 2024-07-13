import unittest
from src.player.player import Player
from src.dice.choice import Choice


"""This is a simple test to practice unitest"""
class test_player(unittest.TestCase):
    def test_print(self):
        thor = Player()
        thor.score[Choice.Brains] = 2
        """Checks if Brains in score is equal to 2"""
        self.assertEquals(thor.score[Choice.Brains], 2)
        thor.print_score()