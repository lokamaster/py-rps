import unittest
from unittest.mock import patch

from main import get_move, get_user_move


class TestCode(unittest.TestCase):
    def test_computer_choice_valid(self):
        valid = ["rock", "paper", "scissors"]

        actual = get_move()

        self.assertTrue(actual in valid)

    @patch("builtins.input")
    def test_user_input_must_bevalid(self, mock_input):
        valid = ["rock", "paper", "scissors"]
        mock_input.side_effect = ["", "wrong", " ", "paper", "wrong"]

        actual = get_user_move()

        self.assertTrue(actual in valid)
