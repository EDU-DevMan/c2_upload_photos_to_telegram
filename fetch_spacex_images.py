import requests
import sys
from saves_images_directory import saves_image
from check_url import get_checked_url
from get_image_name import returns_file_extension
from argument_parsing import get_argument_command_line

PATH_IMAGES = "images"
URL_SPACEX = "https://api.spacexdata.com/v5/launches"


if __name__ == '__main__':

    launche_id = get_argument_command_line().parse_args(sys.argv[1:])

    if launche_id.launch is None:
        response_urls = get_checked_url(URL_SPACEX)
        if response_urls:
            for image_url in response_urls.json()[::-1]:
                original_image_url = image_url["links"]["flickr"]["original"]
                if original_image_url:
                    for image in original_image_url:
                        saves_image(
                            PATH_IMAGES,
                            returns_file_extension(image),
                            requests.get(image).content)
                    break

    else:
        response_urls = get_checked_url('{}/{}'.format(
            URL_SPACEX, launche_id.launch))
        if response_urls:
            for image in response_urls.json()["links"]["flickr"]["original"]:
                saves_image(
                    PATH_IMAGES,
                    returns_file_extension(image),
                    requests.get(image).content)
