import requests
import argparse
import sys
from saves_images_directory import saves_image
from get_checked_path import checked_path
from urllib.parse import urlparse, unquote
from get_image_file_name import returns_file_extension


PATH_IMAGES = "images"
URLS_SPACEX = "https://api.spacexdata.com/v5/launches"


def get_launch_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch', nargs='?')

    return parser


if __name__ == '__main__':

    parser = get_launch_id()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.launch is None:
        response_launches = checked_path(URLS_SPACEX)
        if response_launches:
            for image_url in response_launches.json()[::-1]:
                if image_url["links"]["flickr"]["original"]:
                    for image in image_url["links"]["flickr"]["original"]:
                        image_name = returns_file_extension(image)

                        saves_image(
                            PATH_IMAGES, 
                            image_name, 
                            requests.get(image).content)
                    break

    else:
        namespace_launches = checked_path('{}/{}'.format(
            URLS_SPACEX, namespace.launch))
        if namespace_launches:
            for image in namespace_launches.json()["links"]["flickr"]["original"]:
                image_name = returns_file_extension(image)
                saves_image(
                    PATH_IMAGES, image_name, requests.get(image).content)
