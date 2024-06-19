import requests
from dotenv import load_dotenv
import os
import datetime
from common_scripts import download_image, get_date_from_epic


def fetch_nasa_epic(token):
    url_nasa_epic = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': token,
    }
    response = requests.get(url_nasa_epic, params=params)
    response.raise_for_status()
    
    for number, image in enumerate(response.json()):
        date_epic = get_date_from_epic(image['date'])
        image_name = image['image']
        url_image = f'https://api.nasa.gov/EPIC/archive/natural/{date_epic}/png/{image_name}.png?api_key={token}'
        
        download_image(
            url=url_image, 
            path=f'images/epic{number}.png'
        )

def main():
    load_dotenv()
    token = os.environ['NASA_API_TOKEN']

    try:
        os.makedirs('images')
    except FileExistsError:
        pass

    fetch_nasa_epic(token)

if __name__ == "__main__":
    main()