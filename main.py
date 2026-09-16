"""RPS terminal game.

Standard game of RPS, played in terminal in best to N fashion.
"""

from app.rps import RPS
from app.parser import get_arguments


def main():
    args = get_arguments()
    rps = RPS()
    rps.run(args.rounds)


if __name__ == "__main__":
    main()
