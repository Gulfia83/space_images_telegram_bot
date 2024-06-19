import telegram
from dotenv import load_dotenv
import os
import random
import argparse


def public_images(token, chat_id, folder_name, image_name):
    if image_name is None:
        folder_path, folder_names, image_names = next(os.walk(folder_name))
        image_to_publish = random.choice(image_names)

    else:
        image_to_publish = image_name
  
    image_path = os.path.join(folder_name, image_to_publish)
    bot = telegram.Bot(token)
    bot.send_document(chat_id=chat_id, document=open(image_path, 'rb'))


if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']

    parser = argparse.ArgumentParser()
    parser.add_argument('--folder_name', help='Name of folder with images', default='images')
    parser.add_argument('--image_name', help='Name of image to publish', default=None)
    args = parser.parse_args()
    folder_name = args.folder_name
    image_name = args.image_name

    public_images(token, chat_id, folder_name, image_name)


    
