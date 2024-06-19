import os
import argparse
from dotenv import load_dotenv
from fetch_spacex_images import fetch_spacex_images
from fetch_nasa_apod_images import fetch_nasa_apod
from fetch_nasa_epic_images import fetch_nasa_epic


if __name__ == "__main__":
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']

    os.makedirs('images', exist_ok=True)

    parser = argparse.ArgumentParser(description='Receive SpaceX launch ID (default value "latest") and count of images (default value 3)')
    parser.add_argument('--id', default='latest', help='ID of the SpaceX launch.')
    parser.add_argument('--count', default=3, type=int, help='How many pictures to download')
    args = parser.parse_args()

    fetch_spacex_images(args.id)
    fetch_nasa_apod(token, args.count)
    fetch_nasa_epic(token)