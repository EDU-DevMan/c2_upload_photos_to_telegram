import requests
import os
from requests.exceptions import HTTPError
import argparse
import sys


PATH_IMAGES = "images"
URLS_SPACEX = "https://api.spacexdata.com/v5/launches"


def creates_folder(filename):
    try:
        return os.makedirs(filename, exist_ok=True)
    except FileExistsError:
        return filename


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


def downloads_image(path, img_num, img):
    with open('{}/{}'.format(path,
                             "spacex_{}.jpg".format(img_num)
                             ), 'wb') as file:
        file.write(img)


def get_launch_id():
    parser = argparse.ArgumentParser()
    parser.add_argument('launch', nargs='?')

    return parser


if __name__ == '__main__':

    if not os.path.exists(PATH_IMAGES):
        creates_folder(PATH_IMAGES)

    parser = get_launch_id()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.launch is None:
        response_launches = get_checked_path(URLS_SPACEX)
        if response_launches:
            for jpg_url in response_launches.json()[::-1]:
                if jpg_url["links"]["flickr"]["original"]:
                    for img_num, img in enumerate(
                            jpg_url["links"]["flickr"]["original"]):

                        downloads_image(
                            PATH_IMAGES, img_num, requests.get(img).content)
                    break

    else:
        namespace_launches = get_checked_path('{}/{}'.format(
            URLS_SPACEX, namespace.launch))
        if namespace_launches:
            for img_num, img in enumerate(
                    namespace_launches.json()["links"]["flickr"]["original"]):

                downloads_image(
                    PATH_IMAGES, img_num, requests.get(img).content)
