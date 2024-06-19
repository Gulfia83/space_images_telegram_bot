import requests
import os
from urllib.parse import urlsplit, unquote
import datetime
    

def download_image(url, path, params=None):
    response = requests.get(url, params=params)
    response.raise_for_status()
    with open(path, 'wb') as file:
        file.write(response.content)


def get_extension(url):
    parsed_url = urlsplit(url)
    path = unquote(parsed_url.path)
    file_extension = os.path.splitext(path)[1]
    return file_extension


def get_date_from_epic(date):
    only_date = date.split(' ')[0]
    only_date = datetime.datetime.fromisoformat(only_date)
    date_epic = only_date.strftime('%Y/%m/%d')
    return date_epic


