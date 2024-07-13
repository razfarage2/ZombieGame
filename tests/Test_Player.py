import unittest
from Player import Player
from Choice import Choice


"""This is a simple test to practice unitest"""
class test_player(unittest.TestCase):
    def test_print(self):
        thor = Player()
        thor.score[Choice.Brains] = 2
        """Checks if Brains in score is equal to 2"""
        self.assertEquals(thor.score[Choice.Brains], 2)
        thor.print_score()