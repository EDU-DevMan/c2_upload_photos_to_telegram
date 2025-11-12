import os
import requests
import argparse
from site_responses import receives_response_site
from fetch_file_name import exctracts_filename_extension

IMAGES_PATH = "images"
SPACEX_URL = "https://api.spacexdata.com/v5/launches"


def get_launch_id():
    parser = argparse.ArgumentParser(prog='SPACEX argument parsing',
                                     description="""Программа возвращает
                                     один аргумент* командной строки в скрипт
                                     fetch_spacex_images.py .
                                     *Аргумент - id запуска , из которого
                                     будут выбраны изображения для сохранения.
                                     Подробности работы читайте в README""",
                                     epilog='____________________________')
    parser.add_argument('launche', nargs='?', default='',
                        help="""Пример запуска:
                        fetch_spacex_images.py 61e048ffbe8d8b66799018d1 ,
                        Скрипт можно запускать без аргумента - будут сохранены
                        изображения от последнего запуска.
                        """)

    return parser


def main():

    checked_link = receives_response_site(
        '{}/{}'.format(SPACEX_URL, get_launch_id().parse_args().launche)
        )

    os.makedirs(IMAGES_PATH, exist_ok=True)

    if checked_link:
        if get_launch_id().parse_args().launche:
            for link_img in checked_link.json()["links"]["flickr"]["original"]:
                with open('{}/{}'.format(IMAGES_PATH,
                                         exctracts_filename_extension(
                                             link_img)), 'wb') as file:
                    file.write(requests.get(link_img).content)

        else:
            for last_link_img in checked_link.json()[::-1]:
                last_link = last_link_img["links"]["flickr"]["original"]
                if last_link:
                    for link_img in last_link:
                        with open('{}/{}'.format(IMAGES_PATH,
                                                 exctracts_filename_extension(
                                                     link_img)), 'wb') as file:
                            file.write(requests.get(link_img).content)
                    break


if __name__ == '__main__':
    main()
