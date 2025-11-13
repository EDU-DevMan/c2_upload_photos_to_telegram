import os
import requests
import argparse
from environs import Env
from receiving_responses_site import receives_response_site
from fetch_file_name import exctracts_filename_extension

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"


def returns_number_images():
    parser = argparse.ArgumentParser(description="""Программа возвращает
                                     один аргумент* командной строки в скрипт
                                     fetch_nasa_images.py .
                                     *Аргумент - число изображений, которые
                                     можно сохранить.
                                     Подробности работы читайте в README""",
                                     epilog='____________________________')
    parser.add_argument('number', nargs='?', default=5, type=int,
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

    os.makedirs(IMAGES_PATH, exist_ok=True)
    site_response = receives_response_site(
        NASA_URL,
        returns_number_images().parse_args().number,
        nasa_token
        )

    try:
        for link_img in site_response:
            with open('{}/{}'.format(IMAGES_PATH,
                                     exctracts_filename_extension(
                                         link_img["url"])), 'wb') as file:
                file.write(requests.get(link_img["url"]).content)

    except AttributeError:
        pass


if __name__ == '__main__':
    main()
