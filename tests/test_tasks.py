import unittest

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

class Game:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def get_highest_scoring_player(self):
        return max(self.players, key=lambda player: player.score)

class TestPlayerComparison(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player1 = Player("Alice", 100)
        self.player2 = Player("Bob", 85)
        self.player3 = Player("Charlie", 120)
        self.game.add_player(self.player1)
        self.game.add_player(self.player2)
        self.game.add_player(self.player3)

    def test_highest_scoring_player(self):
        highest_scorer = self.game.get_highest_scoring_player()
        self.assertEqual(highest_scorer.name, "Charlie")
        self.assertEqual(highest_scorer.score, 120)

    def test_player_comparison(self):
        players_sorted = sorted(self.game.players, key=lambda player: player.score, reverse=True)
        self.assertEqual(players_sorted[0].name, "Charlie")
        self.assertEqual(players_sorted[1].name, "Alice")
        self.assertEqual(players_sorted[2].name, "Bob")

if __name__ == '__main__':
    unittest.main()