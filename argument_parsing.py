import argparse


def get_input_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_argument', nargs='?')

    return parser
