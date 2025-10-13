import os
import requests
from requests.exceptions import HTTPError
from urllib.parse import urlparse, unquote
from environs import Env
from saves_images_directory import saves_image


PATH_IMAGES = "images"
URLS_SPACEX = "https://api.nasa.gov/planetary/apod"
NUMBER_PHOTOS = 2


def get_checked_path(url, api):
    payload = {'count': NUMBER_PHOTOS, 'api_key': api}

    try:
        response = requests.get('{}'.format(url), params=payload)
        response.raise_for_status()
        return response

    except HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Страница не найдена: {url}")
            print(f"Ошибка: {e}")
            return None
        elif e.response.status_code == 403:
            print(f"🛑 Доступ запрещен, проверти API: {url}")
            print(f"Ошибка: {e}")
            return None            
        else:
            print(f"⚠️ Другая HTTP ошибка: {e}")
            raise
    except Exception as e:
        print(f"🚫 Общая ошибка: {e}")
        return None


def returns_file_extension(url):

    return unquote(os.path.split(urlparse(url).path)[1])


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_api = env('NASA_API')

    if get_checked_path(URLS_SPACEX, nasa_api):
        for url in get_checked_path(URLS_SPACEX, nasa_api).json():
            img_name = returns_file_extension(url["url"])
            saves_image(
                PATH_IMAGES, img_name, requests.get(url["url"]).content)



