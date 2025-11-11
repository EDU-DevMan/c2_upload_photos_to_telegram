import argparse


def get_frequency_max_publication():
    parser = argparse.ArgumentParser()
    parser.add_argument('frequency', nargs='?', default=10,
                        help="""Скрипт postings_photo_tg.py на вход может
                        принять один аргумент - число (значение измеряется
                        в секундах),
                        пример: postings_photo_tg.py 60 - скрипт будет
                        публиковать изображение каждую минуту.
                        Скрипт можно запускать без аргумента.
                        Подробно читать в README.
                        """)

    return parser
