import telegram
from environs import Env


if __name__ == '__main__':
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_API'))

    bot.send_document(chat_id=env('TELEGRAM_CHANNAL'),
                      document=open('images/hoag_hubble_960.jpg', 'rb'))
