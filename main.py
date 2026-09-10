import random

VALID_MOVES = ["rock", "paper", "scissors"]


def get_move() -> str:
    return random.choice(VALID_MOVES)


def get_user_move() -> str:
    while (move := input("Your move: ").lower()) not in VALID_MOVES:
        print("Choose a valid move. Rock, paper or scissors")
    return move


def main():
    computer_move = get_move()
    user_move = get_user_move()

    if computer_move == user_move:
        print("Draw!")
    elif (
        (computer_move == "rock" and user_move == "scissors")
        or (computer_move == "scissors" and user_move == "paper")
        or (computer_move == "paper" and user_move == "rock")
    ):
        print("You lose")
    else:
        print("You win!!")


if __name__ == "__main__":
    main()
