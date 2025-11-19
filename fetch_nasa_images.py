import os
import argparse
from environs import Env
from receiving_responses_site import receives_response_site
from fetch_file_name import exctracts_filename

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"


def returns_int():
    parser = argparse.ArgumentParser(
        prog='fetch_nasa_images.py',
        description="""Программа позволяет сохранить изображения космических
        объектов, изображения из открытого космоса и т.д.,
        предоставляемые сайтом NASA""",
        epilog='____________________________',
    )
    parser.add_argument('int', nargs='?', default=5, type=int,
                        help="""целое число - обозначает количество
                        изображений, которые будут сохранены .
                        Без аргумента сохраняются 5 изображений.
                        """)

    return parser


def main():
    env = Env()
    env.read_env()

    nasa_token = env('NASA_TOKEN')

    os.makedirs(IMAGES_PATH, exist_ok=True)
    site_response = receives_response_site(
        NASA_URL,
        returns_int().parse_args().int,
        nasa_token
    )

    try:
        if returns_int().parse_args().int:
            for link_img in site_response:
                with open(
                    f'{IMAGES_PATH}/{exctracts_filename(link_img["url"])}',
                    'wb'
                ) as file:
                    file.write(
                        receives_response_site(link_img["url"]).content
                    )

    except TypeError:
        print("URL недоступен!")


if __name__ == '__main__':
    main()
