import os
import random
import time
import telegram

from environs import Env
from telegram_argument_parsing import get_frequency_max_publication


if __name__ == '__main__':
    env = Env()
    env.read_env()
    chat_id = env('TELEGRAM_CHANNAL')

    bot = telegram.Bot(token=env('TELEGRAM_TOKEN'))
    publication_frequency = get_frequency_max_publication().parse_args()

    while True:
        for root, dirs, files in os.walk("images/"):
            random.shuffle(files)
            for image in files:
                bot.send_document(chat_id,
                                  document=open(
                                      'images/{}'.format(image), 'rb'))
                time.sleep(int(publication_frequency.frequency))
