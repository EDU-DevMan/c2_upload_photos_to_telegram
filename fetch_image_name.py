import os
from urllib.parse import urlparse, unquote


def get_file_extension(url):

    parsed_url = urlparse(url).path
    splited_url = os.path.split(parsed_url)
    file_extension = unquote(splited_url[1])

    return file_extension
