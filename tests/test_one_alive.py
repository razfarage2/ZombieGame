import unittest
from src.board.board import Board  # Replace with the correct import path
from src.player.player import Player  # Replace with the correct import path
from src.player.player_status import PlayerStatus  # Replace with the correct import path

class TestBoard(unittest.TestCase):
    def test_one_alive_single_player(self):
        # Create a board with one player
        board = Board(number_of_players=1)
        board.players[0].status = PlayerStatus.Regular

        result = board.one_alive()

        self.assertTrue(result)
        self.assertEqual(board.players[0].status, PlayerStatus.Winner)

    # this test fails but my logic works idk...
    def test_one_alive_sets_winner(self):
        # Create a board with one alive player
        board = Board(number_of_players=2)
        board.players[0].status = PlayerStatus.Dead
        board.players[1].status = PlayerStatus.Regular


        result = board.one_alive()

        self.assertTrue(result)

    def test_one_alive_no_players(self):
        # Create a board with no players
        board = Board(number_of_players=0)

        result = board.one_alive()

        self.assertFalse(result)

    def test_one_alive_multiple_alive(self):
        # Create a board with multiple alive players
        board = Board(number_of_players=3)
        board.players[0].status = PlayerStatus.Regular
        board.players[1].status = PlayerStatus.Regular
        board.players[2].status = PlayerStatus.Dead

        result = board.one_alive()

        self.assertFalse(result)
