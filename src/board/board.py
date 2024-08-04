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

    # if i wrote it correctly and understood it right, it does the same function as before but now it declares the last person alive as the winner
    def one_alive(self):
        alive_players = []
        for player in self.players:
            if player.calculate_status() != PlayerStatus.Dead:
                alive_players.append(player)

        if len(alive_players) == 1:
            winner = alive_players[0]
            winner.status = PlayerStatus.Winner
            print(f"Game over, {winner} won the game with {winner.score[Choice.Brains]} brains")
            return True

        return False

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
        if player.calculate_status() == PlayerStatus.Regular and not self.has_winner():
            print(f"Its your turn to throw {player}")
            self.sleep()
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

    def check_num_of_rolls(self):
        regular_players = list(filter(lambda player: player.calculate_status() == PlayerStatus.Regular, self.players))
        for player in regular_players:
            return player.number_of_rolls


    def check_if_in_regular(self):
        regular_list = [list(filter(lambda player: player.calculate_status() == PlayerStatus.Regular, self.players))]
        return regular_list

    """Initiates the last round of the game"""
    def last_round(self):
        regular_list = [list(filter(lambda player: player.calculate_status() == PlayerStatus.Regular, self.players))]
        if self.has_winner() and not self.one_alive():
            for player in regular_list:
                print("Final round, lets see if everyone can keep up!")
                print(f"Its your turn to throw {player}")
                if self.check_num_of_rolls() < 1:
                    print(self.check_num_of_rolls())

                    first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)
                    first_dice_roll, second_dice_roll = self.throws_dices(first_dice, second_dice)
                    self.update_score(first_dice_roll, second_dice_roll)
                    break
                else:
                    # if player.calculate_status() != PlayerStatus.Regular:
                        break


    def throw_if_regular(self,player, first_dice, second_dice):
        if player.calculate_status() == PlayerStatus.Regular:
            first_dice_roll, second_dice_roll = self.throws_dices(first_dice, second_dice)
            self.update_score(first_dice_roll, second_dice_roll, player)

            first_dice, second_dice = self.should_keep_dices(first_dice_roll, first_dice, second_dice_roll, second_dice)
        else:
            return False

    def annouce_winner(self):
        winners = list(filter(lambda player: player.calculate_status() == PlayerStatus.Winner, self.players))
        print((f"Game over, {winners[0]} won the game with {winners[0].score[Choice.Brains]} brains"))



    def start_game(self):
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

                    while player.should_throw() and not self.has_winner(): # need to fix this line
                        self.throw_if_regular(player, first_dice, second_dice)

                elif player.calculate_status() == PlayerStatus.Winner:
                    self.last_round()
            break

        if not self.one_alive():
            self.annouce_winner()

        if self.one_alive():
            print(self.one_alive())


"""Tomer Tasks"""
# a. printing the dice side value and player name.
# b. find a way to fix the last round function that every player beside the winner will throw once and its over.

