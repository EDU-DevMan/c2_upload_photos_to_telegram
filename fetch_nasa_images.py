import requests
from environs import Env
from saves_images_directory import saves_image
from check_url import get_checked_url
from fetch_image_name import get_file_extension
from nasa_argument_parsing import get_nums_image

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"


if __name__ == '__main__':
    env = Env()
    env.read_env()

    nasa_token = env('NASA_TOKEN')
    image = get_nums_image().parse_args()

    checked_url = get_checked_url(NASA_URL, image.nums_image, nasa_token)

    if checked_url:
        for image_url in get_checked_url(NASA_URL,
                                         int(image.nums_image),
                                         nasa_token).json():
            image_name = get_file_extension(image_url["url"])
            saves_image(IMAGES_PATH, image_name,
                        requests.get(image_url["url"]).content)
