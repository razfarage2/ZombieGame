from enum import Enum
from src.player.player_status import PlayerStatus


class Rules(Enum):
    rule_1 = '1. there are 13 dices, you pick randomly 2 dices and throw them.'
    rule_2 = '2. there are 3 options to recieve from the dices Brains, Shotgun and Footsteps'
    rule_3 = '3. you need to collect the most brains to win the game! but we wary if you get 3 shotgun shots you die!'
    rule_4 = '4. when a player reaches 13 brains the final round start to let the other player catch up, whoever has the most brains win!'