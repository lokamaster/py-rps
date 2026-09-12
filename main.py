import random
import time
from enum import StrEnum, auto


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


class RPS:
    def __init__(
        self,
        rules: dict[Move, dict[Move, Outcome]] = RULES,
    ) -> None:
        self.rules = rules

    def get_move(self) -> Move:
        return random.choice(list(Move))

    def get_user_move(self) -> Move:
        while (
            (move := input("Your move: ").lower())
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
        FIRST_TO = 3

        print("Welcome to Rock-Paper-Scissors")
        print("-"*20)
        print(f"Let's play first to {FIRST_TO}")
        print()
        win = 0
        loss = 0
        round_no = 0
        while max(win, loss) < FIRST_TO:
            round_no += 1
            print(f"Round number {round_no}")
            print(f"Current score {win} - {loss}")
            computer_move = self.get_move()
            user_move = self.get_user_move()
            outcome = self.determine_win(user_move, computer_move)
            if outcome == Outcome.WIN:
                win += 1
                print("You win!!")
            elif outcome == Outcome.LOSS:
                loss += 1
                print("You lose")
            elif outcome == Outcome.DRAW:
                print("Draw!")
            print()

        print("Game concluded")
        print(f"Result: {win} - {loss}")
        if win > loss:
            print("You won it all!!")
        else:
            print("You lost :( Better luck next time!")


def main():
    rps = RPS()
    rps.run()


if __name__ == "__main__":
    main()
