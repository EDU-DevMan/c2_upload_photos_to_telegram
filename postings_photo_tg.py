import os
import random
import time
import telegram

from environs import Env
from argument_parsing import get_input_argument


FREQUENCY_MAXIMUM_PUBLICATION = 14400


if __name__ == '__main__':
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_TOKEN'))
    publication_frequency = get_input_argument().parse_args()

    while True:
        for root, dirs, files in os.walk("images/"):
            random.shuffle(files)
            for image in files:
                bot.send_document(chat_id=env('TELEGRAM_CHANNAL'),
                                  document=open('images/{}'.format(image),
                                                'rb'))
                if publication_frequency.launch is None:
                    time.sleep(FREQUENCY_MAXIMUM_PUBLICATION)
                else:
                    time.sleep(int(publication_frequency.launch))
