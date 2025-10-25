import argparse


def get_input_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_argument', nargs='?',
                        help="""Скрипт fetch_spacex_images.py на вход может
                        принять один аргумент - id запуска, пример:
                        fetch_spacex_images.py 61e048ffbe8d8b66799018d1 .
                        Скрипт fetch_nasa_images.py на вход может принять
                        один аргумент - число изображений, пример:
                        fetch_nasa_images.py 50 .
                        Скрипт postings_photo_tg.py на вход может принять
                        один аргумент - число (мин.) - частота публикации,
                        пример: postings_photo_tg.py 60 .
                        Скрипты можно запускать без аргумета.
                        Подробно читать в README.)
                        """)

    return parser
