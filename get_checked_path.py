import requests
from requests.exceptions import HTTPError


def checked_path(url, num_phots='', *api):
    try:
        if api and num_phots:
            payload = {'count': num_phots, 'api_key': api}
            response = requests.get('{}'.format(url), params=payload)
            response.raise_for_status()
            return response
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
            print(f"🛑 Доступ запрещен{url}")
            print(f"Ошибка: {e}")
            return None            
        else:
            print(f"⚠️ Другая HTTP ошибка: {e}")
            raise
    except Exception as e:
        print(f"🚫 Общая ошибка: {e}")
        return None