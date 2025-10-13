import requests
import sys
from saves_images_directory import saves_image
from get_checked_path import checked_path
from get_image_name import returns_file_extension
from launch_id_spacex import get_launch_id


PATH_IMAGES = "images"
URLS_SPACEX = "https://api.spacexdata.com/v5/launches"


if __name__ == '__main__':

    namespace = get_launch_id().parse_args(sys.argv[1:])

    if namespace.launch is None:
        response_urls = checked_path(URLS_SPACEX)
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
        response_urls = checked_path('{}/{}'.format(
            URLS_SPACEX, namespace.launch))
        if response_urls:
            for image in response_urls.json()["links"]["flickr"]["original"]:
                saves_image(
                    PATH_IMAGES,
                    returns_file_extension(image),
                    requests.get(image).content)
