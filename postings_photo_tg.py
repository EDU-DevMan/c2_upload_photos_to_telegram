import os
import sys
import random
import time
import telegram

from environs import Env
from argument_parsing import get_argument_command_line


PUBLICATIONS_ALARM = 14400


if __name__ == '__main__':
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_API'))
    namespace = get_argument_command_line().parse_args(sys.argv[1:])

    while True:
        for root, dirs, files in os.walk("images/"):
            random.shuffle(files)
            for image in files:
                bot.send_document(chat_id=env('TELEGRAM_CHANNAL'),
                                  document=open(
                                      'images/{}'.format(image), 'rb'))
                if namespace.launch is None:
                    time.sleep(PUBLICATIONS_ALARM)
                else:
                    time.sleep(int(namespace.launch))
