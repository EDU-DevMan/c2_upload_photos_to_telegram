import telegram
from environs import Env


if __name__ == '__main__':
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_API'))

    bot.send_message(text="Привет, я photoBOT_NASA!",
                     chat_id=env('TELEGRAM_CHANNAL'))
