import os


def makes_directory(filename):
    return os.makedirs(filename, exist_ok=False)
