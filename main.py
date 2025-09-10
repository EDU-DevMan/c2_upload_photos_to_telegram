import requests


def main():
    url = 'https://yandex.ru'
    return requests.get(url)


if __name__ == '__main__':
    print(main())
