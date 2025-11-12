import argparse


def get_launch_id():
    parser = argparse.ArgumentParser(prog='SPACEX argument parsing',
                                     description="""Программа возвращает
                                     один аргумент* командной строки в скрипт
                                     fetch_spacex_images.py .
                                     *Аргумент - id запуска , из которого
                                     будут выбраны изображения для сохранения.
                                     Подробности работы читайте в README""",
                                     epilog='____________________________')
    parser.add_argument('launche', nargs='?', default='',
                        help="""Пример запуска:
                        fetch_spacex_images.py 61e048ffbe8d8b66799018d1 ,
                        Скрипт можно запускать без аргумента - будут сохранены
                        изображения от последнего запуска.
                        """)

    return parser
