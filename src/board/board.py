import random
import pprint
from src.dice.choice import Choice
from src.rules import Rules
from src.dice.dice import Dice
from src.player.player import Player
from src.player.player_status import PlayerStatus
import time


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
        """Iterates inside the players to check if their status is regular """
        while True:
            for player in self.players:
                if player.calculate_status() == PlayerStatus.Regular:
                    return PlayerStatus.Regular     # <--- returns true or false depend on the outcome
                else:
                    print(self.has_winner(), self.all_dead())
                    return self.has_winner() and self.all_dead()

    def throws_dices(self, first_dice, first_dice_roll, second_dice, second_dice_roll, player):
        self.sleep()
        print(first_dice)
        self.sleep()
        print(first_dice_roll)
        self.sleep()

        print(second_dice)
        self.sleep()
        print(second_dice_roll)
        self.sleep()

    def update_score(self,first_dice_roll, second_dice_roll, player):
        player.increase_score([first_dice_roll, second_dice_roll])
        self.sleep()
        player.print_score()
        self.sleep()
        player.increase_roll()


    def start_game(self):
        winning_score = 13
        while not self.has_winner() or len(self.players) > 1:
            if self.one_alive():    # this is ugly and need to be fixed, only used to understand the problem
                print(f"Game over, {player} Won the game!")
                break


            else:
                for player in self.players: # needs to change to while because after all players are iterated it will finish the game even though it might not be finished
                    """Need to figure out how to change this loop to achieve the same effect and for the
                    dices to change if the player decides to roll again"""

                    first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)
                    first_dice_roll, second_dice_roll = first_dice.roll(), second_dice.roll()

                    """Puts a win condition for the game """
                    brain_count = player.score[Choice.Brains]
                    if brain_count >= winning_score:
                        print(f"{player} Wins! with {brain_count} Brains!")
                        return

                    """Resets the player number of rolls if he decides not to throw again"""
                    player.number_of_rolls = 0


                    while not self.one_alive():
                        """If the number of rolls is not equal to 0,he can choose whether to throw again or not"""
                        if player.number_of_rolls != 0:
                            self.sleep()
                            print("Do you want to throw again? (y/n)")
                            decision = input()
                            if decision == 'y':
                                self.throws_dices(first_dice, second_dice, first_dice_roll, second_dice_roll, player)
                                self.update_score(first_dice_roll, second_dice_roll, player)
                            elif decision == 'n':
                                self.sleep()
                                print("Let's move on to the next player then")
                                break

                        else:
                            """If the number of throws is equal to 0, the player has no choice but to throw"""
                            self.sleep()
                            print(f"Its your turn to throw {player}")
                            self.sleep()
                            print("are you ready to throw? (y/n)")
                            decision = input()
                            if decision == 'y':
                                self.throws_dices(first_dice, second_dice, first_dice_roll, second_dice_roll, player)
                                self.update_score(first_dice_roll, second_dice_roll, player)

                            elif decision == 'n':
                                print("hahaha you have no choice")
                                self.throws_dices(first_dice, second_dice, first_dice_roll, second_dice_roll, player)
                                self.update_score(first_dice_roll, second_dice_roll, player)
                            else:
                                """Raises a valueerror message that tells the player he has to input y or n"""
                                raise ValueError(' Please respond only in y or n')




"""-------------------------------------------------- PROBLEMS --------------------------------------------------"""
"""New Problems"""
# 1. if the player reaches 3 or more shotguns the while loop continues only on the same dead person <-- FIXED
# 2. the number of rolls doesn't reset. <--- FIXED
# 3. the dices stay the same when he decided to roll again.
# 4. if one player is alive need to end the game and announce a winner <--- FIXED
# 5. Find a way to clean the choices functions <--- FIXED
# 6. Find a way to change the first for loop --> it will solve the 3rd problem
# 7. find a way to access the key of score <---- FIXED

"""Tomer Tasks"""
# a. After the turn ask if you want to continue otherwise break the loop <--- DONE?
# b. Check if he can keep one of the dices
# c. Let him choose if to keep
# d. Generate new dices if needed.

# f. Print the player score -> need a new function that returns the player score <-- DONE?

# e. If we got out of the while it means either all dead or there is a winner which means we should say it
# g. If we have a winner, give all other players last round -> refactor the while above to a function that gets the players from outside


board = Board()
board.start_game()