import os
import argparse
from receiving_responses_site import receives_response_site
from fetch_file_name import exctracts_filename_extension

IMAGES_PATH = "images"
SPACEX_URL = "https1://api.spacexdata.com/v5/launches"


def returns_id():
    parser = argparse.ArgumentParser(
        prog='fetch_spacex_images.py',
        description="""Программа позволяет сохранить изображения,
        которые получены с запуска шатла SpaceX.""",
        epilog='____________________________',
    )
    parser.add_argument('id', nargs='?', default='',
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
        response_json = site_response.json()
        if returns_id().parse_args().id:
            for link_image in response_json["links"]["flickr"]["original"]:
                filename = exctracts_filename_extension(link_image)
                with open('{}/{}'.format(IMAGES_PATH,
                                         filename), 'wb') as file:
                    file.write(receives_response_site(link_image).content)
        else:
            for last_link_image in response_json[::-1]:
                last_link = last_link_image["links"]["flickr"]["original"]
                if last_link:
                    for link_image in last_link:
                        filename = exctracts_filename_extension(link_image)
                        with open('{}/{}'.format(IMAGES_PATH,
                                                 filename), 'wb') as file:
                            file.write(
                                receives_response_site(link_image).content
                            )
                    break

    except AttributeError:
        print("URL недоступен!")


if __name__ == '__main__':
    main()
