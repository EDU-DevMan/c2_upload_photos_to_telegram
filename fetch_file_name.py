import os
from urllib.parse import urlparse


def exctracts_filename(url):

    parsed_url = urlparse(url).path
    splited_url = os.path.split(parsed_url)[1]

    return splited_url
