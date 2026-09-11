import random
from enum import StrEnum, auto


class ValidMove(StrEnum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()


class Outcome(StrEnum):
    WIN = auto()
    LOSS = auto()
    DRAW = auto()


class RPS:
    def get_move(self) -> ValidMove:
        return random.choice(list(ValidMove))

    def get_user_move(self) -> ValidMove:
        while (
            (move := input("Your move: ").lower())
            not in list(ValidMove)
        ):
            print("Choose a valid move. Rock, paper or scissors")
        return ValidMove(move)

    def determine_win(
        self,
        first: ValidMove,
        second: ValidMove
    ) -> Outcome:
        if first == second:
            return Outcome.DRAW
        elif (
            (first == ValidMove.ROCK and second == ValidMove.SCISSORS)
            or 
            (first == ValidMove.SCISSORS and second == ValidMove.PAPER)
            or
            (first == ValidMove.PAPER and second == ValidMove.ROCK)
        ):
            return Outcome.WIN
        else:
            return Outcome.LOSS
    
    def run(self) -> None:
        computer_move = self.get_move()
        user_move = self.get_user_move()
        outcome = self.determine_win(user_move, computer_move)
        if outcome == Outcome.WIN:
            print("You win!!")
        elif outcome == Outcome.LOSS:
            print("You lose")
        elif outcome == Outcome.DRAW:
            print("Draw!")


def main():
    rps = RPS()
    rps.run()


if __name__ == "__main__":
    main()
