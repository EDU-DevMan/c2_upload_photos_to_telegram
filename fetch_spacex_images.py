import requests
import sys
from saves_images_directory import saves_image
from get_checked_path import checked_path
from get_image_name import returns_file_extension
from launch_id import get_launch_id


PATH_IMAGES = "images"
URLS_SPACEX = "https://api.spacexdata.com/v5/launches"


if __name__ == '__main__':

    namespace = get_launch_id().parse_args(sys.argv[1:])

    if namespace.launch is None:
        response_launches = checked_path(URLS_SPACEX)
        if response_launches:
            for image_url in response_launches.json()[::-1]:
                if image_url["links"]["flickr"]["original"]:
                    for image in image_url["links"]["flickr"]["original"]:
                        image_name = returns_file_extension(image)

                        saves_image(
                            PATH_IMAGES, 
                            image_name, 
                            requests.get(image).content)
                    break

    else:
        namespace_launches = checked_path('{}/{}'.format(
            URLS_SPACEX, namespace.launch))
        if namespace_launches:
            for image in namespace_launches.json()["links"]["flickr"]["original"]:
                image_name = returns_file_extension(image)
                saves_image(
                    PATH_IMAGES, image_name, requests.get(image).content)
