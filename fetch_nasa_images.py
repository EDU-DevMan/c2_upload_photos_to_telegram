import requests
import sys
from environs import Env
from saves_images_directory import saves_image
from check_url import get_checked_url
from get_image_name import returns_file_extension
from argument_parsing import get_argument_command_line

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"
PHOTOS_MAXIMUM_NUMBER = 40


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_api = env('NASA_API')
    photos_number = get_argument_command_line().parse_args(sys.argv[1:])

    if get_checked_url(NASA_URL, PHOTOS_MAXIMUM_NUMBER, nasa_api):
        if photos_number.launch is None:
            for url in get_checked_url(NASA_URL, PHOTOS_MAXIMUM_NUMBER,
                                       nasa_api).json():
                img_name = returns_file_extension(url["url"])
                saves_image(
                    IMAGES_PATH, img_name, requests.get(url["url"]).content)
        else:
            for url in get_checked_url(NASA_URL,
                                       int(photos_number.launch),
                                       nasa_api).json():
                img_name = returns_file_extension(url["url"])
                saves_image(
                    IMAGES_PATH, img_name, requests.get(url["url"]).content)
