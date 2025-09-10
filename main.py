import requests
import os
import errno


PATH_IMAGES = "images"


def creates_folder(filename):
    try:
        return os.makedirs(filename, exist_ok=True)
    except FileExistsError:
        # directory already exists
        return filename


def downloads_image():
    url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

    headers = {'User-Agent':
               'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
               'AppleWebKit/537.36 (KHTML, like Gecko) '
               'Chrome/91.0.4472.124 Safari/537.36'}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.content


def main():
    if not os.path.exists(PATH_IMAGES):
        creates_folder(PATH_IMAGES)
    with open('{}/hubble.jpeg'.format(PATH_IMAGES), 'wb') as file:
        file.write(downloads_image())


if __name__ == '__main__':
    main()
