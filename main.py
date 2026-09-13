import random
import sys
from enum import StrEnum, auto

from app import art


class Move(StrEnum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class Outcome(StrEnum):
    WIN = auto()
    LOSS = auto()
    DRAW = auto()


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


# Ansi Escape Sequences
ALT_BUFFER_ON = "\x1b[?1049h"
ALT_BUFFER_OFF = "\x1b[?1049l"
CURSOR_SHOW = "\x1b[?25h"
CURSOR_HIDE = "\x1b[?2hl"
CURSOR_HOME = "\x1b[H"
CLEAR_SCREEN = "\x1b[2J"


class Terminal:
    def __enter__(self):
        # Change to alt buffer and hide curso
        sys.stdout.write(ALT_BUFFER_ON + CLEAR_SCREEN + CURSOR_HIDE)
        sys.stdout.flush()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Restore terminal
        sys.stdout.write(CURSOR_SHOW + ALT_BUFFER_OFF)
        sys.stdout.flush()

    def draw(self, frame: str) -> None:
        sys.stdout.write(CURSOR_HOME + CLEAR_SCREEN + frame)
        sys.stdout.flush()


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
        while (
            (move := input("Your move: ").lower().strip())
            not in list(Move)
        ):
            print("Choose a valid move. Rock, paper or scissors")
        return Move(move)

    def determine_win(
        self,
        first: Move,
        second: Move,
    ) -> Outcome:
        return self.rules[first][second]

    def run(self) -> None:
        # Game constants
        first_to = 3

        welcome = (
            art.LOGO + "\n"
            +"Welcome to Rock-Paper-Scissors\n"
            + "-"*20 + "\n"
            + f"Let's play first to {first_to}\n"
        )

        win = 0
        loss = 0
        round_no = 0
        result = ""
        # Main gameplay loop
        with Terminal() as app:
            while max(win, loss) < first_to:
                round_no += 1
                round_info = (
                    f"Round number {round_no}\n"
                    + f"Current score {win} - {loss}\n"
                )
                app.draw(
                    welcome
                    + result
                    + round_info
                )

                # Get moves
                computer_move = self.get_move()
                user_move = self.get_user_move()
                outcome = self.determine_win(user_move, computer_move)

                # Print result to terminal
                result = (
                    "="*20 + "\n"
                    + "Your pick\n"
                    + user_move.capitalize() + "\n"
                    + self.art[user_move] + "\n"
                    + "Computer picks\n"
                    + computer_move.capitalize() + "\n"
                    + self.art[computer_move] + "\n"
                    + "="*20 + "\n"
                )
                if outcome == Outcome.WIN:
                    win += 1
                    result += "You win!!\n"
                elif outcome == Outcome.LOSS:
                    loss += 1
                    result += "You lose\n"
                elif outcome == Outcome.DRAW:
                    result += "Draw!\n"

                app.draw(
                    welcome
                    + result
                )

            end_result = (
                "Game concluded\n"
                + f"Result {win} - {loss}\n"
            )
            if win > loss:
                end_result += "You won it all!!\n"
            else:
                end_result += "You lost :( Better luck next time!\n"
            app.draw(
                welcome
                + result
                + end_result
            )
            input("press ENTER to quit")


def main():
    rps = RPS()
    rps.run()


if __name__ == "__main__":
    main()
