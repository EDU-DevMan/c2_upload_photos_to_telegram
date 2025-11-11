import argparse


def get_number_images():
    parser = argparse.ArgumentParser()
    parser.add_argument('nums', nargs='?', default=5,
                        help="""Скрипт fetch_nasa_images.py на вход может
                        принять один аргумент - число, пример:
                        fetch_nasa_images.py 50 ,
                        где 50 - количество изображений, которые будут
                        сохранены.
                        Скрип без аргумента сохранит 5 изображенний.
                        """)

    return parser
