import argparse


def get_number_images():
    parser = argparse.ArgumentParser(prog='NASA argument parsing',
                                     description="""Программа возвращает
                                     один аргумент* командной строки в скрипт
                                     fetch_nasa_images.py .
                                     *Аргумент - число изображений, которые
                                     можно сохранить.
                                     Подробности работы читайте в README""",
                                     epilog='____________________________')
    parser.add_argument('nums', nargs='?', default=5,
                        help="""Пример запуска:
                        fetch_nasa_images.py 50 ,
                        будут сохранены 50 изображений.
                        Скрип без аргумента сохранит 5 изображений.
                        """)

    return parser
