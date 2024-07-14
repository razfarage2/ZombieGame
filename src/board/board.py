import random
import pprint
from src.dice.choice import Choice
from src.rules import Rules
from src.dice.dice import Dice
from src.player.player import Player
from src.player.player_status import PlayerStatus
import time
from src.util.util import generic_question


class Board:
    def __init__(self, number_of_players=2, number_of_dices=13):
        # Print the rules and let him choose number of players etc... --> DONE
        self.players = []
        for i in range(number_of_players):
            self.players.append(Player())

        self.dices = []
        for i in range(number_of_dices):
            self.dices.append(Dice())  # add a config for number of sides

        print("Lets start the game!")
        self.sleep()
        """Iterates inside the rules enum and prints all of it"""
        for rule in Rules:
            pprint.pprint(rule.value)
        self.sleep()

    def sleep(self):    # a simple delay
        time.sleep(1)

    """Checks  if the length of dead players are equal to all the players in the game"""
    def all_dead(self):
        dead_players = list(filter(lambda player: player.calculate_status() == PlayerStatus.Dead, self.players))
        return len(dead_players) == len(self.players)   # <--- returns true or false depend on the outcome


    """This function checks with the any function if any of the players
    have status of a winner in the player in the game"""
    def has_winner(self):
        return any(player.calculate_status() == PlayerStatus.Winner for player in self.players)     # <--- returns true or false depend on the outcome


    """Ideally it filters out the alive players to 1 by substracting
    the number of players - (num of player - 1) to get always 1"""
    def one_alive(self):
        for alive in self.players:
          alive_players = list(filter(lambda player: player.calculate_status() == PlayerStatus.Regular, self.players))
          num_alive_players = len(alive_players)
          num_total_players = len(self.players)
          num_dead_players = num_total_players - num_alive_players

          return (num_alive_players == 1) and (num_dead_players == num_total_players - 1)


    """Checks if the player status is regular"""
    def has_regular(self):
        while True:
            for player in self.players:
                if player.calculate_status() == PlayerStatus.Regular:
                    return PlayerStatus.Regular     # <--- returns true or false depend on the outcome
                else:
                    print(self.has_winner(), self.all_dead())
                    return self.has_winner() and self.all_dead()

    def throws_dices(self, first_dice,second_dice):
        first_dice_roll, second_dice_roll = first_dice.roll(), second_dice.roll()
        self.sleep()
        print(first_dice.sides)
        self.sleep()
        print(first_dice_roll)
        self.sleep()

        print(second_dice.sides)
        self.sleep()
        print(second_dice_roll)
        self.sleep()

        return first_dice_roll, second_dice_roll

    def update_score(self,first_dice_roll, second_dice_roll, player):
        player.increase_score([first_dice_roll, second_dice_roll])
        self.sleep()
        player.print_score()
        self.sleep()
        player.increase_roll()

    def interact_player(self, player):
        print(f"Its your turn to throw {player}")
        self.sleep()
        print("are you ready to throw? (y/n)")
        decision = input()
        if decision == 'y':
            print("throwing...")

        else:
            print("hahaha you have no choice")

    def should_keep_dices(self, first_dice_roll, first_dice, second_dice_roll, second_dice):
        new_first_dice, new_second_dice = first_dice, second_dice

        if first_dice_roll == Choice.Footsteps:
            should_generate_dice = not generic_question(
                f"Do you want to throw the first dice again?(y/n)\n {first_dice.sides}")
            if should_generate_dice:
                new_first_dice = random.choice(self.dices)

        if second_dice_roll == Choice.Footsteps:
            should_generate_dice = not generic_question(
                f"Do you want to throw the second dice again?(y/n)\n {second_dice.sides}")
            if should_generate_dice:
                new_second_dice = random.choice(self.dices)

        return new_first_dice, new_second_dice

    """Initiates the last round of the game"""
    def last_round(self, player):
        if player.calculate_status() == PlayerStatus.Regular:
            player.reset_rolls()

            self.interact_player(player)

            first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)
            first_dice_roll, second_dice_roll = self.throws_dices(first_dice, second_dice)
            self.update_score(first_dice_roll, second_dice_roll, player)
        else:
            if player.calculate_status() == PlayerStatus.Winner or player.calculate_status() == PlayerStatus.Dead:
                return False

    def announce_winner(self):
        for i, player in enumerate(self.players):
            for other_player in self.players[i + 1:]:
                if player.score[Choice.Brains] > other_player.score[Choice.Brains]:
                    print(f"Game over, {player} won the game with {player.score[Choice.Brains]} brains")
                    pass
                elif player.score[Choice.Brains] < other_player.score[Choice.Brains]:
                    print(f"Game over, {player} won the game with {player.score[Choice.Brains]} brains")


    def start_game(self):
        while not self.has_winner() or not self.one_alive():
            for player in self.players:
                if player.calculate_status() != PlayerStatus.Dead or player.calculate_status() != PlayerStatus.Winner:
                    player.reset_rolls()

                    self.interact_player(player)

                    first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)

                    while player.should_throw():
                        if not self.has_winner() or player.calculate_status() != PlayerStatus.Dead:
                            first_dice_roll, second_dice_roll = self.throws_dices(first_dice, second_dice)
                            self.update_score(first_dice_roll, second_dice_roll, player)

                            first_dice, second_dice = self.should_keep_dices(first_dice_roll,first_dice,second_dice_roll,second_dice)
                        else:
                            break

        if self.has_winner() or not self.one_alive():
            print("Final round lets see if you can keep up the Brains!")
            for player in self.players:
                 self.last_round(player)



        self.announce_winner()


"""Tomer Tasks"""
# e. If we got out of the while it means either all dead or there is a winner which means we should say it
# g. If we have a winner, give all other players last round -> refactor the while above to a function that gets the players from outside
# a. printing the dice side value and player name.