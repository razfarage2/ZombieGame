import unittest
from unittest.mock import patch
import random

from src.dice.choice import Choice
from src.dice.dice import Dice


class DiceTest(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    @patch.object(random, 'choice')
    def test_init_sides_populated(self, mock_choice):
        # Mock the random.choice call to control what gets added to sides
        mock_choice.side_effect = [Choice.Brains, Choice.Shotguns, Choice.Footsteps]
        dice = Dice(number_of_sides=3)

        self.assertEqual(dice.sides, [Choice.Brains, Choice.Shotguns, Choice.Footsteps])

    @patch.object(random, 'choice')
    def test_roll_returns_side(self, mock_choice):
        # Mock the random.choice call to simulate a roll
        mock_choice.return_value = Choice.Footsteps
        result = self.dice.roll()

        self.assertEqual(result, Choice.Footsteps)


if __name__ == '__main__':
    unittest.main()
