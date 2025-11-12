import os
import requests
from site_responses import receives_response_site
from fetch_image_name import get_file_extension
from spacex_argument_parsing import get_launch_id

IMAGES_PATH = "images"
SPACEX_URL = "https://api.spacexdata.com/v5/launches"


if __name__ == '__main__':

    os.makedirs(IMAGES_PATH, exist_ok=True)

    launch_id = get_launch_id().parse_args()
    checked_link = receives_response_site('{}/{}'.format(SPACEX_URL,
                                                         launch_id.launche))

    if checked_link:
        if launch_id.launche:
            for link_img in checked_link.json()["links"]["flickr"]["original"]:
                with open('{}/{}'.format(IMAGES_PATH,
                                         get_file_extension(
                                             link_img)), 'wb') as file:
                    file.write(requests.get(link_img).content)

        else:
            for last_link_img in checked_link.json()[::-1]:
                last_link = last_link_img["links"]["flickr"]["original"]
                if last_link:
                    for link_img in last_link:
                        with open('{}/{}'.format(IMAGES_PATH,
                                                 get_file_extension(
                                                     link_img)), 'wb') as file:
                            file.write(requests.get(link_img).content)
                    break
