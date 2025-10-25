import requests
import sys
from environs import Env
from saves_images_directory import saves_image
from check_url import get_checked_url
from get_image_name import returns_file_extension
from argument_parsing import get_input_argument

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"
PHOTOS_MAXIMUM_NUMBER = 40


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_token = env('NASA_TOKEN_API')
    photos_number = get_input_argument().parse_args(sys.argv[1:])

    checked_url = get_checked_url(NASA_URL, PHOTOS_MAXIMUM_NUMBER, nasa_token)

    if checked_url:
        if photos_number.input_argument is None:
            for url in checked_url.json():
                image_name = returns_file_extension(url["url"])
                saves_image(
                    IMAGES_PATH, image_name, requests.get(url["url"]).content)
        else:
            for image_url in get_checked_url(NASA_URL,
                                             int(photos_number.input_argument),
                                             nasa_token).json():
                image_name = returns_file_extension(image_url["url"])
                saves_image(
                    IMAGES_PATH, image_name, requests.get(
                        image_url["url"]).content)
