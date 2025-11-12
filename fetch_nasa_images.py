import os
import requests
import argparse
from environs import Env
from site_responses import receives_response_site
from fetch_file_name import exctracts_filename_extension

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"


def get_number_images():
    parser = argparse.ArgumentParser(prog='NASA argument parsing',
                                     description="""Программа возвращает
                                     один аргумент* командной строки в скрипт
                                     fetch_nasa_images.py .
                                     *Аргумент - число изображений, которые
                                     можно сохранить.
                                     Подробности работы читайте в README""",
                                     epilog='____________________________')
    parser.add_argument('number', nargs='?', default=5,
                        help="""Пример запуска:
                        fetch_nasa_images.py 50 ,
                        будут сохранены 50 изображений.
                        Скрип без аргумента сохранит 5 изображений.
                        """)

    return parser


def main():
    env = Env()
    env.read_env()

    nasa_token = env('NASA_TOKEN')
    checked_link = receives_response_site(
        NASA_URL,
        int(get_number_images().parse_args().number),
        nasa_token
        )

    os.makedirs(IMAGES_PATH, exist_ok=True)

    if checked_link:
        for link_img in checked_link:
            with open('{}/{}'.format(IMAGES_PATH,
                                     exctracts_filename_extension(
                                         link_img["url"])), 'wb') as file:
                file.write(requests.get(link_img["url"]).conten)


if __name__ == '__main__':
    main()
