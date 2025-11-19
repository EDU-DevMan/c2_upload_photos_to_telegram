import requests
from requests.exceptions import HTTPError


def receives_response_site(url, photos_number='', *token):
    try:
        if token and photos_number:
            payload = {'count': photos_number, 'nasa_token': token}
            response = requests.get('{}'.format(url), params=payload)
        else:
            response = requests.get(url)

        response.raise_for_status()
        return response

    except HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Страница не найдена: {url}")
            print(f"Ошибка: {e}")
            return None
        elif e.response.status_code == 403:
            print(f"🛑 Доступ запрещен {url}")
            print(f"Ошибка: {e}")
            return None
        else:
            print(f"⚠️ Другая HTTP ошибка: {e}")
            raise
    except requests.exceptions.InvalidSchema as e:
        print(f"🚫Ошибка подключения к {url}: {e}")
        return None
