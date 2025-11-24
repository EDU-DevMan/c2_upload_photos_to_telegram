import os
import argparse
from receiving_responses_site import receives_response_site
from fetch_file_name import exctracts_filename

IMAGES_PATH = "images"
SPACEX_URL = "https://api.spacexdata.com/v5/launches"


def returns_id():
    parser = argparse.ArgumentParser(
        prog='fetch_spacex_images.py',
        description="""Программа позволяет сохранить изображения,
        которые получены с запуска шатла SpaceX.""",
        epilog='____________________________',
    )
    parser.add_argument('id', nargs='?', default='6243adcaaf52800c6e919254',
                        help="""идентификатор запуска, представляет собой
                        буквенно-цифровой набор символов,
                        пример: 61e048ffbe8d8b66799018d1 .
                        Без аргумента применяется идентификатор последнего
                        запуска.
                        """)

    return parser


def main():

    os.makedirs(IMAGES_PATH, exist_ok=True)
    site_response = receives_response_site(
        '{}/{}'.format(SPACEX_URL, returns_id().parse_args().id)
    )

    try:
        image_links = site_response.json()["links"]["flickr"]["original"]
        for image_link in image_links:
            image = receives_response_site(image_link).content
            with open(
                f'{IMAGES_PATH}/{exctracts_filename(image_link)}',
                'wb'
            ) as file:
                file.write(image)

    except AttributeError as e:
        print(f"Невозможно получить атрибут: {e}")


if __name__ == '__main__':
    main()
