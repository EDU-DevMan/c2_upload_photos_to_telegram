import os
import random
import time
import telegram

from environs import Env
from telegram_argument_parsing import get_frequency_max_publication

IMAGES_PATH = "images"


if __name__ == '__main__':
    env = Env()
    env.read_env()
    chat_id = env('TELEGRAM_CHANNAL')

    bot = telegram.Bot(token=env('TELEGRAM_TOKEN'))
    publication_frequency = get_frequency_max_publication().parse_args()

    while True:
        for root, dirs, images in os.walk(IMAGES_PATH):
            random.shuffle(images)
            for image in images:
                with open('{}/{}'.format(IMAGES_PATH, image), 'rb') as image:
                    bot.send_document(chat_id, image)
                time.sleep(int(publication_frequency.frequency))
