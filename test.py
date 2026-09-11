import unittest
from unittest.mock import patch

from main import RPS


class TestCode(unittest.TestCase):
    def test_computer_choice_valid(self):
        valid = ["rock", "paper", "scissors"]
        app = RPS()

        actual = app.get_move()

        self.assertTrue(actual in valid)

    @patch("builtins.input")
    def test_user_input_must_bevalid(self, mock_input):
        valid = ["rock", "paper", "scissors"]
        mock_input.side_effect = ["", "wrong", " ", "paper", "wrong"]
        app = RPS()

        actual = app.get_user_move()

        self.assertTrue(actual in valid)

    def test_outcome_win(self):
        first = "rock"
        second = "scissors"
        app = RPS()
        expected = "win"

        actual = app.determine_win(first, second)
        
        self.assertEqual(expected, actual)

    def test_outcome_lossn(self):
        first = "rock"
        second = "paper"
        app = RPS()
        expected = "loss"

        actual = app.determine_win(first, second)
        
        self.assertEqual(expected, actual)

    def test_outcome_draw(self):
        first = "rock"
        second = "rock"
        app = RPS()
        expected = "draw"

        actual = app.determine_win(first, second)
        
        self.assertEqual(expected, actual)
