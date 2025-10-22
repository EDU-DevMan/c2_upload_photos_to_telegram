import argparse


def get_argument_command_line():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch', nargs='?')

    return parser
