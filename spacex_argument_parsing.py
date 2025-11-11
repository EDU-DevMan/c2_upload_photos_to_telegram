import argparse


def get_launch_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('launche', nargs='?', default='',
                        help="""Скрипт fetch_spacex_images.py на вход может
                        принять только один аргумент - id запуска, пример:
                        fetch_spacex_images.py 61e048ffbe8d8b66799018d1 ,
                        где 61e048ffbe8d8b66799018d1 - id запуска.
                        Скрипты можно запускать без аргумента.
                        Подробности читать в README.
                        """)

    return parser
