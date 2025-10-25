import os
from urllib.parse import urlparse, unquote


def get_file_extension(url):

    return unquote(os.path.split(urlparse(url).path)[1])
