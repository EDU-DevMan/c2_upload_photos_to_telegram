import requests
import os
from requests.exceptions import HTTPError
import argparse
import sys
from saves_images_directory import saves_image
from urllib.parse import urlparse, unquote


PATH_IMAGES = "images"
URLS_SPACEX = "https://api.spacexdata.com/v5/launches"


def get_checked_path(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response

    except HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Страница не найдена: {url}")
            print(f"Ошибка: {e}")
            return None
        else:
            print(f"⚠️ Другая HTTP ошибка: {e}")
            raise
    except Exception as e:
        print(f"🚫 Общая ошибка: {e}")
        return None


def get_launch_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch', nargs='?')

    return parser

def returns_file_extension(url):

    return unquote(os.path.split(urlparse(url).path)[1])


if __name__ == '__main__':

    parser = get_launch_id()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.launch is None:
        response_launches = get_checked_path(URLS_SPACEX)
        if response_launches:
            for jpg_url in response_launches.json()[::-1]:
                if jpg_url["links"]["flickr"]["original"]:
                    for image in jpg_url["links"]["flickr"]["original"]:
                        image_name = returns_file_extension(image)

                        saves_image(
                            PATH_IMAGES, 
                            image_name, 
                            requests.get(image).content)
                    break

    else:
        namespace_launches = get_checked_path('{}/{}'.format(
            URLS_SPACEX, namespace.launch))
        if namespace_launches:
            for img_num, img in enumerate(
                    namespace_launches.json()["links"]["flickr"]["original"]):

                saves_image(
                    PATH_IMAGES, img_num, requests.get(img).content)
