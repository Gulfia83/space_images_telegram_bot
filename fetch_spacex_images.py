import requests
import os
import argparse
from common_scripts import download_image


def fetch_spacex_images(launch_id=None):
    if launch_id==None:
        url_api_spaceX = 'https://api.spacexdata.com/v5/launches/latest'
        response = requests.get(url_api_spaceX)
        response.raise_for_status()
        links = response.json()['links']['flickr']['original']
  
        for number, link in enumerate(links):
            path = f'images/spaceX{number}.jpeg'
            
            download_image(link, path)

    else:
        url_api_spaceX = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        response = requests.get(url_api_spaceX)
        response.raise_for_status()
        links = response.json()['links']['flickr']['original']
  
        for number, link in enumerate(links):
            path = f'images/spaceX{number}.jpeg'
            
            download_image(link, path)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--id', help='ID Spacex launch')
    args = parser.parse_args()
    

    try:
        os.makedirs('images')
    except FileExistsError:
        pass
    fetch_spacex_images(args.id)

if __name__ == '__main__':
    main()

