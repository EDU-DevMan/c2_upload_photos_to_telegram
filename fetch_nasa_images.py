import requests
from urllib.parse import urlparse, unquote
from environs import Env
from saves_images_directory import saves_image
from get_checked_path import checked_path
from get_image_file_name import returns_file_extension


PATH_IMAGES = "images"
URLS_SPACEX = "https://api.nasa.gov/planetary/apod"
NUMBER_PHOTOS = 2


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_api = env('NASA_API')

    if checked_path(URLS_SPACEX, NUMBER_PHOTOS, nasa_api):
        for url in checked_path(URLS_SPACEX, NUMBER_PHOTOS, nasa_api).json():
            img_name = returns_file_extension(url["url"])
            saves_image(
                PATH_IMAGES, img_name, requests.get(url["url"]).content)



