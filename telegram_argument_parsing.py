import argparse


def get_frequency_max_publication():
    parser = argparse.ArgumentParser(prog='Telegram argument parsing',
                                     description="""Программа возвращает
                                     один аргумент* командной строки в скрипт
                                     postings_photo_tg.py .
                                     *Аргумент - число(время в секундах),
                                     указывает с какой периодичностью будет
                                     публиковаться изображение в вашем
                                     telegram канале.
                                     Подробности работы читайте в README""",
                                     epilog='____________________________')
    parser.add_argument('frequency', nargs='?', default=10,
                        help="""Пример запуска:
                        postings_photo_tg.py 60 .
                        Новое изображение будет публиковаться
                        один раз в минуту.
                        Скрипт можно запускать без аргумента -
                        новое изображение будет публиковаться
                        один раз в 4 часа.
                        """)

    return parser
