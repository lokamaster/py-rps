"""RPS terminal game.

Standard game of RPS, played in terminal in best to N fashion.
"""

from app.rps import RPS


def main():
    rps = RPS()
    rps.run()


if __name__ == "__main__":
    main()
