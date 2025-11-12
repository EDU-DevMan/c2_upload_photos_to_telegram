import os
import random
import time
import telegram
import argparse

from environs import Env

IMAGES_PATH = "images"


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


def main():
    env = Env()
    env.read_env()
    chat_id = env('TELEGRAM_CHANNAL')

    bot = telegram.Bot(token=env('TELEGRAM_TOKEN'))

    while True:
        for root, dirs, images in os.walk(IMAGES_PATH):
            random.shuffle(images)
            for image in images:
                with open('{}/{}'.format(IMAGES_PATH, image), 'rb') as image:
                    bot.send_document(chat_id, image)
                time.sleep(int(get_frequency_max_publication().parse_args().frequency))


if __name__ == '__main__':
    main()
