![alt text](https://github.com/EDU-DevMan/c2_upload_photos_to_telegram/blob/main/space_01.JPG?raw=true)

# О проекте

 - В проекте реализован функционал скачивания фотографий планеты Земля, запусков
космических аппаратов, а также множество других фотографий, посвященных космосу с
web-сайтов nasa и spaceX;

- реализован функционал публикации скаченные фотографии в Ваш Телеграмм канал. 

⚠️ Просьба учитывать следующую информацию:

```Due to the lapse in federal government funding, NASA is not updating this website.
We sincerely regret this inconvenience.

⚠ Please Note: The Earth API has been archived and replaced with Earthdata GIBS API.
Please update your bookmarks or projects as needed.```

## Работать с проектом:

### Установка

1) Скачать код [программы](https://github.com/EDU-DevMan/c2_upload_photos_to_telegram)

2) Перейти в директорию с файлами проекта

3) Создать виртуальное окружение

 - выполнить команду ```python3 -m venv --copies .venv```

 - добвить в .gitignore `.venv`

 - активировать виртуальное окружение

 [Подробная инструкция](https://dvmn.org/encyclopedia/pip/pip_virtualenv/)

4) Установить зависимости

 - выполнить команду ```pip install -r requirements.txt```

5) Создать файл .env и добавить следующие данные:

NASA_API = "XXX"

[Как получить NASA_API](https://api.nasa.gov/)

TELEGRAM_API = "XXX:YYYYY"

[Как регистрировать бота](https://way23.ru/регистрация-бота-в-telegram.html)

[Отец ботов](https://telegram.me/BotFather)

TELEGRAM_CHANNAL = "@XXX"

### Запуск

1) Cкачиваем фотографии с сайта SpaseX

Выполните команду:

```python.exe fetch_spacex_images.py```

В директории с проектом будет создана новая деректория ``images`` с фотографиями
последних запусков

2) Cкачиваем фотографии с сайта NASA

Выполните команду:

```python.exe fetch_nasa_images.py```

В директории с проектом будет создана новая деректория ``images`` с фотографиями
космоса.

🙄 По-умолчанию скачивается 40 фотографий, но вы можете скачивать необходимое количество
фотографий:

Выполните команду:
```python.exe fetch_nasa_images.py 10```

🙂 В результате будет скачено 10 фотографий.

Возможные ошибки, которые могут возникать при работе (возможные решения):

❌ Страница не найдена

❗ Решение:

Проверти доступность сайтов:

``https://api.nasa.gov/``

``https://api.spacexdata.com/v5/launche``


🛑 Доступ запрещен

❗ Решение:

Вернитеся к шагу `Как получить NASA_API`

⚠️ Другая HTTP ошибка

См. TODO

🚫 Общая ошибка

❗ Решение:

Проверти корректность ссылок на web сайты:

``URL_NASA`` (fetch_nasa_images.py)

``URL_SPACEX`` (fetch_spacex_images.py)

# TO DO

1) Добавить функционал скачивания фотографий с директорию с именем, 
которое можно ввести самостоятельно;

2) Добавить более расширенную обработку ошибок, при недоступности сайтов;

3) Расширеть скачивания фотографий с тематических (про космос) сайтов;

4) ...
