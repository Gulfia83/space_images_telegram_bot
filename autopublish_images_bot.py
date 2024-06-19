import telegram
from dotenv import load_dotenv
import os
import random
import argparse
import time


def autopublish_images(token, chat_id, folder_name, frequensy_of_publication):
    while True:
        folder_path, folder_names, image_names = next(os.walk(folder_name))
        random.shuffle(image_names)

        for image_to_publish in image_names:
            image_path = os.path.join(folder_name, image_to_publish)
            bot = telegram.Bot(token)
            with open(image_path, 'rb') as image_path:
                bot.send_document(chat_id=chat_id, document=image_path)

            time.sleep(int(frequensy_of_publication) * 60 * 60)

if __name__ == '__main__':
    load_dotenv()
    token = os.environ['TELEGRAM_BOT_TOKEN']
    chat_id = os.environ['TELEGRAM_CHAT_ID']
    frequensy_of_publication = os.environ['FREQUENSY_OF_PUBLICATION']

    parser = argparse.ArgumentParser(description='receive name of the folder with images, default name "images"')
    parser.add_argument('--folder_name', help='Name of folder with images', default='images')
    args = parser.parse_args()
    folder_name = args.folder_name

    autopublish_images(token, chat_id, folder_name, frequensy_of_publication)
