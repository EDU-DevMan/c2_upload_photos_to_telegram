import requests
import os
from requests.exceptions import HTTPError


PATH_IMAGES = "images"
URLS = [
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg",
    ]


def creates_folder(filename):
    try:
        return os.makedirs(filename, exist_ok=True)
    except FileExistsError:
        return filename


def get_checked_path(url):
    try:
        headers = {'User-Agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        return response.content

    except HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Страница не найдена: {url}")
            print(f"Ошибка: {e}")
            return None
        else:
            print(f"⚠️ Другая HTTP ошибка: {e}")
            raise  # Перебрасываем другие HTTP ошибки
    except Exception as e:
        print(f"🚫 Общая ошибка: {e}")
        return None


def downloads_image(path, url):
    with open('{}/{}'.format(path, "HST-SM4.jpeg"), 'wb') as file:
        file.write(url)


def main():
    if not os.path.exists(PATH_IMAGES):
        creates_folder(PATH_IMAGES)

    if URLS:
        for image_save in URLS:
            if get_checked_path(image_save):
                downloads_image(PATH_IMAGES, get_checked_path(image_save))


if __name__ == '__main__':
    main()
