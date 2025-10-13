import argparse


def get_launch_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch', nargs='?')

    return parser