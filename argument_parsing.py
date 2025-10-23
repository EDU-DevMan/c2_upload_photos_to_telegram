import argparse


def get_argument_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_argument', nargs='?')

    return parser
