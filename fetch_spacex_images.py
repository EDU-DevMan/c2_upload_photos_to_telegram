import os
import requests
from check_link import checks_image_link
from fetch_image_name import get_file_extension
from spacex_argument_parsing import get_launch_id

IMAGES_PATH = "images"
SPACEX_URL = "https://api.spacexdata.com/v5/launches"


if __name__ == '__main__':

    os.makedirs(IMAGES_PATH, exist_ok=True)

    launch_id = get_launch_id().parse_args()
    checked_link = checks_image_link('{}/{}'.format(SPACEX_URL,
                                                    launch_id.launch))

    if checked_link:
        if launch_id:
            for link_img in checked_link.json()["links"]["flickr"]["original"]:
                with open('{}/{}'.format(IMAGES_PATH,
                                         get_file_extension(
                                             link_img)), 'wb') as file:
                    file.write(requests.get(link_img).content)

        else:
            for original_link_img in checked_link.json()[::-1]:
                original_image_url = original_link_img["links"]["flickr"]["original"]
                if original_image_url:
                    for image in original_image_url:
                        with open('{}/{}'.format(IMAGES_PATH,
                                                 get_file_extension(
                                                     image)), 'wb') as file:
                            file.write(requests.get(image).content)
                    break
