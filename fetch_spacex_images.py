import requests
from saves_images_directory import saves_image
from check_url import get_checked_url
from fetch_image_name import get_file_extension
from argument_parsing import get_input_argument

IMAGES_PATH = "images2"
SPACEX_URL = "https://api.spacexdata.com/v5/launches"


if __name__ == '__main__':

    launche_id = get_input_argument().parse_args()

    if launche_id.input_argument is None:
        response_urls = get_checked_url(SPACEX_URL)
        if response_urls:
            for image_url in response_urls.json()[::-1]:
                original_image_url = image_url["links"]["flickr"]["original"]
                if original_image_url:
                    for image in original_image_url:
                        saves_image(
                            IMAGES_PATH,
                            get_file_extension(image),
                            requests.get(image).content)
                    break

    else:
        response_urls = get_checked_url('{}/{}'.format(
            SPACEX_URL, launche_id.input_argument))
        if response_urls:
            for image in response_urls.json()["links"]["flickr"]["original"]:
                saves_image(
                    IMAGES_PATH,
                    get_file_extension(image),
                    requests.get(image).content)
