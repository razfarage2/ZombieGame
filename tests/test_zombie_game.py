import random
import pprint
from Rules import Rules
from Dice import Dice
from Player import Player
from playerStatus import PlayerStatus
import unittest


class test_board(unittest.TestCase):

   def test_different(self):
      for player in self.players:  # needs to change to while because after all players are iterated it will finish the game even though it might not be finished
         """idk its working with the for loop, the game doesnt end"""
         first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)
         first_dice_roll, second_dice_roll = first_dice.roll(), second_dice.roll()
      self.assertIsNot(first_dice_roll,second_dice_roll)
