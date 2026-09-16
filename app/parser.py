import argparse


def get_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--rounds", default=3, type=int)
    return parser.parse_args()
