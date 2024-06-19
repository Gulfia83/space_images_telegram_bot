import requests
import os
import argparse
from common_scripts import download_image


def fetch_spacex_images(launch_id='latest'):
        url_api_spaceX = f'https://api.spacexdata.com/v5/launches/{launch_id}'
        response = requests.get(url_api_spaceX)
        response.raise_for_status()
        links = response.json()['links']['flickr']['original']
  
        for number, link in enumerate(links):
            path = f'images/spaceX{number}.jpeg'
            
            download_image(link, path)

def main():
    parser = argparse.ArgumentParser(description="Takes spaceX launch ID, default value 'latest'")
    parser.add_argument('--id', default= 'latest',help='ID Spacex launch')
    args = parser.parse_args()
    
    os.makedirs('images', exist_ok=True)
    
    fetch_spacex_images(args.id)

if __name__ == '__main__':
    main()

