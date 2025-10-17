import telegram
from environs import Env


if __name__ == '__main__':
    env = Env()
    env.read_env()

    bot = telegram.Bot(token=env('TELEGRAM_API'))

    print(bot.get_me())
