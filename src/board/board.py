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
        self.players = []
        for i in range(number_of_players):
            self.players.append(Player())

        self.dices = []
        for i in range(number_of_dices):
            self.dices.append(Dice())

        print("Lets start the game!")
        self.add_delay()
        """Iterates inside the rules enum and prints all of it"""
        for rule in Rules:
            pprint.pprint(rule.value)
        self.add_delay()

    """simple Delay to add time for the player to react"""
    def add_delay(self):    # a simple delay
        time.sleep(1)

    """Checks if the length of dead players are equal to all the players in the game"""
    def all_dead(self):
        dead_players = list(filter(lambda player: player.calculate_status() == PlayerStatus.Dead, self.players))
        return len(dead_players) == len(self.players)   # <--- returns true or false depend on the outcome

    """This function checks with the any function if any of the players
    have status of a winner in the player in the game"""
    def has_winner(self):
        return any(player.calculate_status() == PlayerStatus.Winner for player in self.players)

    """Checks to see if there is only one player alive"""
    def one_alive(self):
        alive_players = []
        for player in self.players:
            if player.calculate_status() != PlayerStatus.Dead:
                alive_players.append(player)

        if len(alive_players) == 1:
            winner = alive_players[0]
            winner.status = PlayerStatus.Winner
            print(f"Game over, {winner.name} won the game with {winner.score[Choice.Brains]} brains")
            return True

        return False

    """The throwing function itself, prints the scores and so."""
    def throws_dices(self, first_dice,second_dice):
        first_dice_roll, second_dice_roll = first_dice.roll(), second_dice.roll()
        self.add_delay()
        print(first_dice.sides)
        self.add_delay()
        print(first_dice_roll)
        self.add_delay()

        print(second_dice.sides)
        self.add_delay()
        print(second_dice_roll)
        self.add_delay()

        return first_dice_roll, second_dice_roll

    """Updates the score of the player after each throws"""
    def update_score(self,first_dice_roll, second_dice_roll, player):
        player.increase_score([first_dice_roll, second_dice_roll])
        self.add_delay()
        player.print_score()
        self.add_delay()
        player.increase_roll()

    """Interaction with the players, asks him questions about throwing the dices and recives input"""
    def interact_player(self, player):
        if player.calculate_status() == PlayerStatus.Regular and not self.has_winner():
            print(f"Its your turn to throw {player.name}")
            self.add_delay()
            print("are you ready to throw? (y/n)")
            decision = input()
            if decision == 'y':
                print("throwing...")

            else:
                print("hahaha you have no choice")
        elif player.calculate_status() == PlayerStatus.Dead:
            print("you died and cant roll again")
        else:
            print("you seem to be winning")

    """Checks if the player can keep the dice he threw"""
    def should_keep_dices(self, first_dice_roll, first_dice, second_dice_roll, second_dice):
        new_first_dice, new_second_dice = first_dice, second_dice

        if first_dice_roll == Choice.Footsteps and not self.has_winner():
            should_generate_dice = not generic_question(
                f"Do you want to throw the first dice again?(y/n)\n {first_dice.sides}")
            if should_generate_dice:
                new_first_dice = random.choice(self.dices)

        if second_dice_roll == Choice.Footsteps and not self.has_winner():
            should_generate_dice = not generic_question(
                f"Do you want to throw the second dice again?(y/n)\n {second_dice.sides}")
            if should_generate_dice:
                new_second_dice = random.choice(self.dices)

        return new_first_dice, new_second_dice

    """Checks the number of rolls each player has"""
    def check_num_of_rolls(self):
        regular_players = list(filter(lambda player: player.calculate_status() == PlayerStatus.Regular, self.players))
        for player in regular_players:
            return player.number_of_rolls

    """Checks the players status and appends them into a list of regular players"""
    def check_if_in_regular(self):
        regular_list = [list(filter(lambda player: player.calculate_status() == PlayerStatus.Regular, self.players))]
        return regular_list

    """Initiates the last round of the game"""
    def last_round(self):
        regular_list = (list(filter(lambda player: player.calculate_status() == PlayerStatus.Regular, self.players)))
        if self.has_winner() and not self.one_alive():
            for player in regular_list:
                self.add_delay()
                print("Final round, lets see if everyone can keep up!")
                self.add_delay()
                print(f"Its your turn to throw {player.name}")
                if self.check_num_of_rolls() < 1:

                    first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)
                    first_dice_roll, second_dice_roll = self.throws_dices(first_dice, second_dice)
                    self.update_score(first_dice_roll, second_dice_roll, player)
                    break
                else:
                        break

    """Allows the player to throw if he has a regular status"""
    def throw_if_regular(self,player, first_dice, second_dice):
        if player.calculate_status() == PlayerStatus.Regular:
            first_dice_roll, second_dice_roll = self.throws_dices(first_dice, second_dice)
            self.update_score(first_dice_roll, second_dice_roll, player)

            first_dice, second_dice = self.should_keep_dices(first_dice_roll, first_dice, second_dice_roll, second_dice)
        else:
            return False

    """Announce the winner at the end of the game, if there is more then 1 player alive"""
    def announce_winner(self):
        winners = list(filter(lambda player: player.calculate_status() == PlayerStatus.Winner, self.players))
        winner = winners[0]
        print(f"Game over, {winner.name} won the game with {winner.score[Choice.Brains]} brains")

    """Prints the score of all the players"""
    def print_all_scores(self):
        for player in self.players:
            pprint.pprint(f"{player.name} has a score of {player.score}")
            self.add_delay()

    """Main function(Game Loop)"""
    def start_game(self):
        """If there is no winner, runs the loop"""
        while not self.has_winner():
            if self.one_alive():
                break

            for player in self.players:
                if self.one_alive():
                    break

                if player.calculate_status() == PlayerStatus.Regular:
                    player.reset_rolls()

                    self.interact_player(player)

                    first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)

                    while player.should_throw() and not self.has_winner():
                        self.throw_if_regular(player, first_dice, second_dice)
            break

        if self.has_winner():
            self.add_delay()
            self.last_round()

        if not self.one_alive():
            self.announce_winner()
            self.add_delay()
            self.print_all_scores()

        if self.one_alive():
            print(self.one_alive())
            self.add_delay()
            self.print_all_scores()


"""Tomer Tasks"""
# a. printing the dice side value.


