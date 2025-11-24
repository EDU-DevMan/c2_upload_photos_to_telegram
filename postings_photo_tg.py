import os
import random
import time
import telegram
import argparse

from environs import Env

IMAGES_PATH = "images"


def returns_an_integer():
    parser = argparse.ArgumentParser(
        prog='postings_photo_tg.py',
        description="""Программа позволяет публиковать изображения
        в Telegram канал""",
        epilog='____________________________',
    )
    parser.add_argument('int', nargs='?', default=14400, type=int,
                        help="""целое число - (время в секундах) - указывает
                        с какой периодичностью будет публиковаться изображение
                        в вашем telegram канале.
                        Без аргумента новое изображение будет публиковаться
                        один раз в 4 часа.
                        """)

    return parser


def main():
    env = Env()
    env.read_env()
    chat_id = env('TELEGRAM_CHANNAL')

    bot = telegram.Bot(token=env('TELEGRAM_TOKEN'))

    if returns_an_integer().parse_args().int:
        while True:
            for root, dirs, images in os.walk(IMAGES_PATH):
                random.shuffle(images)
                for image in images:
                    with open(f'{IMAGES_PATH}/{image}', 'rb') as image:
                        bot.send_document(chat_id, image)
                    time.sleep(returns_an_integer().parse_args().int)


if __name__ == '__main__':
    main()
