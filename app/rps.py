"""Main game class."""

import random

from . import art
from .models import Move, Outcome
from .terminal import Terminal

RULES = {
    Move.ROCK: {
        Move.ROCK: Outcome.DRAW,
        Move.PAPER: Outcome.LOSS,
        Move.SCISSORS: Outcome.WIN,
    },
    Move.PAPER: {
        Move.ROCK: Outcome.WIN,
        Move.PAPER: Outcome.DRAW,
        Move.SCISSORS: Outcome.LOSS,
    },
    Move.SCISSORS: {
        Move.ROCK: Outcome.LOSS,
        Move.PAPER: Outcome.WIN,
        Move.SCISSORS: Outcome.DRAW,
    },
}

ART = {
    Move.ROCK: art.ROCK,
    Move.PAPER: art.PAPER,
    Move.SCISSORS: art.SCISSORS,
}


class RPS:
    def __init__(
        self,
        rules: dict[Move, dict[Move, Outcome]] = RULES,
        art: dict[Move, str] = ART,
    ) -> None:
        self.rules = rules
        self.art = art

    def get_move(self) -> Move:
        return random.choice(list(Move))

    def get_user_move(self) -> Move:
        while (move := input("Your move: ").lower().strip()) not in list(
            Move
        ):
            print("Choose a valid move. Rock, paper or scissors")
        return Move(move)

    def determine_win(
        self,
        first: Move,
        second: Move,
    ) -> Outcome:
        return self.rules[first][second]

    def _build_welcome(self, first_to: int) -> str:
        return (
            art.LOGO
            + "\n"
            + "Welcome to Rock-Paper-Scissors\n"
            + "-" * 30
            + "\n"
            + f"Let's play first to {first_to}\n"
            + "-" * 30
            + "\n"
        )

    def _build_round_info(
        self, round_no: int, win: int, loss: int
    ) -> str:
        return (
            f"Round number {round_no}\n"
            + f"Current score {win} - {loss}\n"
        )

    def _build_result(
        self, user: Move, computer: Move, outcome: Outcome
    ) -> str:
        result = (
            "You pick "
            + user
            + "\n"
            + self.art[user]
            + "\n"
            + "Computer picks "
            + computer
            + "\n"
            + self.art[computer]
            + "\n"
        )
        if outcome == Outcome.WIN:
            result += "You win!!"
        elif outcome == Outcome.LOSS:
            result += "You lose"
        elif outcome == Outcome.DRAW:
            result += "Draw"
        result += "\n" + "-" * 30 + "\n"
        return result

    def _build_end(self, win: int, loss: int) -> str:
        end_result = "Game concluded\n" + f"Result {win} - {loss}\n"
        if win > loss:
            end_result += "You won it all!!\n"
        else:
            end_result += "You lost :( Better luck next time!\n"
        return end_result

    def run(self) -> None:
        # Game constants
        first_to = 3

        welcome = self._build_welcome(first_to)
        result = ""

        win = 0
        loss = 0
        round_no = 0
        # Main gameplay loop
        with Terminal() as app:
            while max(win, loss) < first_to:
                round_no += 1
                round_info = self._build_round_info(round_no, win, loss)
                app.draw(welcome + result + round_info)

                # Get moves
                computer = self.get_move()
                user = self.get_user_move()
                outcome = self.determine_win(user, computer)

                # Update score
                if outcome == Outcome.WIN:
                    win += 1
                elif outcome == Outcome.LOSS:
                    loss += 1

                result = self._build_result(user, computer, outcome)
                app.draw(welcome + result)

            end_result = self._build_end(win, loss)
            app.draw(welcome + result + end_result)
            input("press ENTER to quit")
