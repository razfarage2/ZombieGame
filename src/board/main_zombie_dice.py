import random
import pprint
from rules import Rules
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


    """Ideally it filters out the alive players to 1 but substracting
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

    def start_game(self):
            while not self.has_winner() or not self.one_alive():
                if self.one_alive():    # this is ugly and to be fixed, only used to understand the problem
                    print(f"game over")
                    break
                else:
                    for player in self.players: # needs to change to while because after all players are iterated it will finish the game even though it might not be finished
                        """idk its working with the for loop, the game doesnt end"""
                        first_dice, second_dice = random.choice(self.dices), random.choice(self.dices)
                        first_dice_roll, second_dice_roll = first_dice.roll(), second_dice.roll()
                        """Resets the player number of rolls if he decides not to throw again"""
                        player.number_of_rolls = 0
                        """ Found this 8 lines to be useless so,
                        I comment them for now"""
                        # if player.calculate_status() == PlayerStatus.Dead:
                        #     print("dead")
                        #     breakxs
                        # elif player.calculate_status() == PlayerStatus.Winner:
                        #     print("winner")
                        #     break
                        # else:
                        #     pass
                        """Decided to clean up the look of this function a bit so made them into a function,
                            still need to find a way to get them outside of the start_game function"""
                        def no_choice(self):
                            self.sleep()
                            print("hahaha you have no choice")
                            self.sleep()
                            print(first_dice)
                            self.sleep()
                            print(first_dice_roll)
                            self.sleep()

                            print(second_dice)
                            self.sleep()
                            print(second_dice_roll)
                            self.sleep()
                            player.increase_score([first_dice_roll, second_dice_roll])
                            self.sleep()
                            player.print_score()
                            self.sleep()
                            player.increase_roll()

                        def decision_Yes(self):
                            self.sleep()
                            print(first_dice)
                            self.sleep()
                            print(first_dice_roll)
                            self.sleep()

                            print(second_dice)
                            self.sleep()
                            print(second_dice_roll)
                            self.sleep()
                            player.increase_score([first_dice_roll, second_dice_roll])
                            self.sleep()
                            player.print_score()
                            self.sleep()
                            player.increase_roll()

                        def Throws_again(self):
                            self.sleep()
                            print(first_dice)
                            self.sleep()
                            print(first_dice_roll)
                            self.sleep()

                            print(second_dice)
                            self.sleep()
                            print(second_dice_roll)
                            self.sleep()
                            player.increase_score([first_dice_roll, second_dice_roll])
                            self.sleep()
                            player.print_score()
                            self.sleep()
                            player.increase_roll()
                            self.sleep()

                        """my simple solution to get me out of the while loop."""
                        if not self.one_alive():
                            """checks the status of the player"""
                            while player.calculate_status() == PlayerStatus.Regular:
                                print(f"{player} and {player.calculate_status()}")
                                """If the number of rolls is not equal to 0 and he is not dead or a winner,
                                    he can choose whether to throw again or not"""
                                if player.number_of_rolls != 0 and player.calculate_status() == PlayerStatus.Regular:
                                    self.sleep()
                                    print("Do you want to throw again? (y/n)")
                                    decision = input()
                                    if decision == 'y':
                                        Throws_again(self)
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
                                        decision_Yes(self)

                                    elif decision == 'n':
                                        no_choice(self)
                                    else:
                                        """Raises a valueerror message that tells the player he has to input y or n"""
                                        raise ValueError(' Please respond only in y or n')
                        elif player.calculate_status() == PlayerStatus.Dead:
                            print("You died, you cant roll again")
                            break

                    """New Problems"""
                    # 1. if the player reaches 3 or more shotguns the while loop continues only on the same dead person <-- changed the while loop to be true only if regular # FIXED?
                    # 2. the number of rolls doesn't reset. <--- FIXED
                    # 3. the dices stay the same when he decided to roll again.
                    # 4. if one player is alive need to end the game and announce a winner <--- half FIXED ends the game but doesn't announce the winner
                    # 5. Find a way to clean the choices functions
                    # 6. Find a way to change the first for loop --> it will solve the 3rd problem

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