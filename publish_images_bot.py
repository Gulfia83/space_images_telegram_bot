import telegram
from dotenv import load_dotenv
import os
import random
import argparse


def publish_image(token, chat_id, folder_name, image_name):
    if not image_name:
        folder_path, folder_names, image_names = next(os.walk(folder_name))
        image_to_publish = random.choice(image_names)

    else:
        image_to_publish = image_name
  
    image_path = os.path.join(folder_name, image_to_publish)
    bot = telegram.Bot(token)
    with open(image_path, 'rb') as image_path:
        bot.send_document(chat_id=chat_id, document=image_path)


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    parser = argparse.ArgumentParser(description='Receive folder with images (default value "images") and image name')
    parser.add_argument('--folder_name', help='Name of folder with images', default='images')
    parser.add_argument('--image_name', help='Name of image to publish')
    args = parser.parse_args()
    folder_name = args.folder_name
    image_name = args.image_name

    publish_image(token, chat_id, folder_name, image_name)


    
