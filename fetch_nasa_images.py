import os
import requests
from environs import Env
from check_url import get_checked_url
from fetch_image_name import get_file_extension
from nasa_argument_parsing import get_nums_image

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"


if __name__ == '__main__':
    env = Env()
    env.read_env()

    os.makedirs(IMAGES_PATH, exist_ok=True)

    nasa_token = env('NASA_TOKEN')
    image = get_nums_image().parse_args()

    checked_url = get_checked_url(NASA_URL, image.nums_image, nasa_token)

    if checked_url:
        for image_url in get_checked_url(NASA_URL, int(image.nums_image),
                                         nasa_token).json():
            with open('{}/{}'.format(IMAGES_PATH,
                                     get_file_extension(
                                         image_url["url"])), 'wb') as file:
                file.write(requests.get(image_url["url"]).conten)
