import os


def makes_directory(filename):
    try:
        return os.makedirs(filename, exist_ok=True)
    except FileExistsError:
        return filename
