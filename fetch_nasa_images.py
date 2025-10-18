import requests
import sys
from environs import Env
from saves_images_directory import saves_image
from get_checked_path import checked_path
from get_image_name import returns_file_extension
from launch_id_spacex import get_launch_id


PATH_IMAGES = "images"
URL_NASA = "https://api.nasa.gov/planetary/apod"
NUMBER_PHOTOS = 40


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_api = env('NASA_API')
    namespace = get_launch_id().parse_args(sys.argv[1:])

    if checked_path(URL_NASA, NUMBER_PHOTOS, nasa_api):
        if namespace.launch is None:
            for url in checked_path(URL_NASA, NUMBER_PHOTOS, nasa_api).json():
                img_name = returns_file_extension(url["url"])
                saves_image(
                    PATH_IMAGES, img_name, requests.get(url["url"]).content)
        else:
            for url in checked_path(URL_NASA,
                                    int(namespace.launch), nasa_api).json():
                img_name = returns_file_extension(url["url"])
                saves_image(
                    PATH_IMAGES, img_name, requests.get(url["url"]).content)
