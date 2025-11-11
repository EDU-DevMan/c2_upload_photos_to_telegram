import os
import requests
from check_url import get_checked_url
from fetch_image_name import get_file_extension
from spacex_argument_parsing import get_launch_id

IMAGES_PATH = "images"
SPACEX_URL = "https://api.spacexdata.com/v5/launches"


if __name__ == '__main__':

    os.makedirs(IMAGES_PATH, exist_ok=True)

    launche = get_launch_id().parse_args()
    url = get_checked_url('{}/{}'.format(SPACEX_URL, launche.launch_id))

    if url:
        if launche.launch_id:
            for image_url in url.json()["links"]["flickr"]["original"]:
                with open('{}/{}'.format(IMAGES_PATH,
                                         get_file_extension(
                                             image_url)), 'wb') as file:
                    file.write(requests.get(image_url).content)

        else:
            for image_url in url.json()[::-1]:
                original_image_url = image_url["links"]["flickr"]["original"]
                if original_image_url:
                    for image in original_image_url:
                        with open('{}/{}'.format(IMAGES_PATH,
                                                 get_file_extension(
                                                     image)), 'wb') as file:
                            file.write(requests.get(image).content)
                    break
