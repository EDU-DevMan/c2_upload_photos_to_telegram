import os
import argparse
from environs import Env
from receiving_responses_site import receives_response_site
from fetch_file_name import exctracts_filename

IMAGES_PATH = "images"
NASA_URL = "https1://api.nasa.gov/planetary/apod"


def returns_an_integer():
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
        returns_an_integer().parse_args().int,
        nasa_token
    )

    try:
        for image_link in site_response:
            image = receives_response_site(image_link["url"]).content
            with open(
                f'{IMAGES_PATH}/{exctracts_filename(image_link["url"])}',
                'wb'
            ) as file:
                file.write(image)

    except TypeError as e:
        print(f"Невозможно получить итерируемый объект: {e}")


if __name__ == '__main__':
    main()
