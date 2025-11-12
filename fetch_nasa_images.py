import os
import requests
from environs import Env
from site_responses import receives_response_site
from fetch_file_name import exctracts_filename_extension
from nasa_argument_parsing import get_number_images

IMAGES_PATH = "images"
NASA_URL = "https://api.nasa.gov/planetary/apod"


if __name__ == '__main__':
    env = Env()
    env.read_env()

    os.makedirs(IMAGES_PATH, exist_ok=True)

    nasa_token = env('NASA_TOKEN')
    image_numbers = get_number_images().parse_args()

    checked_link = receives_response_site(NASA_URL, image_numbers.nums,
                                          nasa_token)

    if checked_link:
        for link_img in receives_response_site(NASA_URL,
                                               int(image_numbers.nums),
                                               nasa_token).json():
            with open('{}/{}'.format(IMAGES_PATH,
                                     exctracts_filename_extension(
                                         link_img["url"])), 'wb') as file:
                file.write(requests.get(link_img["url"]).conten)
