import requests
from dotenv import load_dotenv
import os
from urllib.parse import urlsplit, unquote
import argparse
from common_scripts import download_image, get_extension


def fetch_nasa_apod(token, count_images):
    url_api_nasa = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': token,
        'count': count_images
    }
    response = requests.get(url_api_nasa, params=params)
    response.raise_for_status()

    for number, image in enumerate(response.json()):
        download_image(
            url=image['url'], 
            path=f'images/nasa_apod{number}{get_extension(image["url"])}'
            )


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']

    parser = argparse.ArgumentParser(description='Receive count of images, default value 3')
    parser.add_argument('--count', default=3, type=int, help='How many images to download')
    args = parser.parse_args()
    count_images = args.count

    os.makedirs('images', exist_ok=True)
    
    fetch_nasa_apod(token, count_images)
