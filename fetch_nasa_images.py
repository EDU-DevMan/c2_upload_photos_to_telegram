import requests
import sys
from environs import Env
from saves_images_directory import saves_image
from check_url import get_checked_url
from get_image_name import returns_file_extension
from argument_parsing import get_argument_command_line

PATH_IMAGES = "images"
URL_NASA = "https://api.nasa.gov/planetary/apod"
PHOTOS_FOR_PUBLICATION = 40


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_api = env('NASA_API')
    number_photos = get_argument_command_line().parse_args(sys.argv[1:])

    if get_checked_url(URL_NASA, PHOTOS_FOR_PUBLICATION, nasa_api):
        if number_photos.launch is None:
            for url in get_checked_url(URL_NASA, PHOTOS_FOR_PUBLICATION,
                                       nasa_api).json():
                img_name = returns_file_extension(url["url"])
                saves_image(
                    PATH_IMAGES, img_name, requests.get(url["url"]).content)
        else:
            for url in get_checked_url(URL_NASA,
                                       int(number_photos.launch),
                                       nasa_api).json():
                img_name = returns_file_extension(url["url"])
                saves_image(
                    PATH_IMAGES, img_name, requests.get(url["url"]).content)
