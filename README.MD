#  Telegram bot for uploading space photos

This project contains several scripts for downloading images from NASA's Astronomy Picture of the Day (APOD), NASA's Earth Polychromatic Imaging Camera (EPIC), and recent SpaceX launches. Downloaded images can be published in the Telegram channel on demand or at a certain frequency. The utility script `common_scripts.py` contains utility functions for creating folders, getting file extensions, and formatting the epic NASA date.

## Installation

1. Obtain your NASA API key at [https://api.nasa.gov/](https://api.nasa.gov/).
2. Get your Telegram API key by creating a new bot using [BotFather](https://core.telegram.org/bots#botfather).
3. Clone the repository and create a `.env` file in the project root directory with the following content:

`NASA_API_TOKEN=your_nasa_api_token`\
`TELEGRAM_BOT_TOKEN=your_telegram_bot_token`\
`FREQUENSY_OF_PUBLICATION=hours`
`TELEGRAM_CHAT_ID=your telegram chat_id`


4. Python3 must be installed on your computer. Then use `pip` (or `pip3` if there is a conflict with Python2) to install the dependencies:

`pip install -r requirements.txt`


## Usage

### 1. Script `fetch_nasa_apod_images.py`

This script downloads images from NASA's Astronomy Picture of the Day (APOD) and saves them to the local `'images'' folder. If there is no such folder, it creates it.

#### Functions

- `fetch_nasa_apod(token, count_images)`: The main script function that accepts the following parameters:
 - `token`: Your NASA API key.
 - `count`: Number of images to upload (default: 3). The script downloads a random selection of images if the number is not specified.

#### Launch

The script can be run from the console using the command:

`python fetch_nasa_apod_images.py [--count COUNT]`


#### Arguments

- `--count COUNT:` (optional) Number of images to upload. By default, 3 images are loaded.

This script imports and uses functions from separate scripts as follows:

- It uses the `download_image` function from the `common_scripts.py` script to save downloaded images.
- To get the file extension, it uses the `get_extension` function from the `common_scripts.py` script.


### 2. Script `fetch_nasa_epic_images.py`

This script downloads images from NASA's Earth Polychromatic Imaging Camera (EPIC) and saves them to the local `'images'' folder. If there is no such folder, it creates it.

#### Functions

- `fetch_nasa_epic(token)`: The main script function that accepts the following parameters:
 - `token`: Your NASA API key.

#### Launch

The script can be run from the console using the command:

`python fetch_nasa_epic_images.py`

#### Arguments

This script does not accept command line arguments.

This script imports and uses functions from separate scripts as follows:

- It uses the `download_image` function from the `common_scripts.py` script to save downloaded images.
- To get the date from NASA EPIC `get_date_from_epic` from the script `common_scripts.py`.


### 3. Script `fetch_spacex_images.py`

This script downloads images associated with the latest SpaceX launch or specified launch and saves them to the local `'images'` folder. If there is no such folder, it creates it.

#### Functions

- `fetch_spacex_images(launch_id=None)`: The main script function that accepts the following parameters:
 - `launch_id`: (optional) The ID of the SpaceX launch for which images need to be loaded. If not specified, images from the last run will be loaded.

#### Launch

The script can be run from the console using the command:

`python fetch_spacex_images.py [--id LAUNCH_ID]`

#### Arguments

- `--id LAUNCH_ID`: (optional) The ID of the SpaceX launch for which images need to be loaded. If not specified, images from the last run will be loaded.

This script imports and uses functions from separate scripts as follows:

- It uses the `download_image` function from the `common_scripts.py` script to save downloaded images.


### 4. Script `fetch_all_images.py`

This script combines the functionality of the `fetch_spacex_images.py`, `fetch_nasa_apod_images.py` and `fetch_nasa_epic_images.py` scripts. It downloads images from SpaceX, NASA APOD and NASA EPIC and saves them to a local ``images'` folder. If there is no such folder, it creates it.

#### Launch

The script can be run from the console using the command:

`python fetch_all_images.py [--id LAUNCH_ID] [--count COUNT]`

#### Arguments
- `--id LAUNCH_ID`: (optional) The ID of the SpaceX launch for which images need to be loaded. If not specified, images from the last run will be loaded.
- `--count COUNT`: (optional) Number of NASA APOD images to load. If not specified, the default value of 3 will be used.

This script imports and uses functions from separate scripts as follows:

- `fetch_spacex_images(args.id)` from the `fetch_spacex_images.py` script.
- `fetch_nasa_apod(token, args.count)` from the `fetch_nasa_apod_images.py` script.
- `fetch_nasa_epic(token)` from the `fetch_nasa_epic_images.py` script.


### 5. Script `publish_images_bot.py`

This script publishes one image to a specified Telegram channel. The image can be selected randomly from a folder or specified by name.

#### Functions

- `publish_image(token, chat_id, folder_name, image_name)`: The main script function that accepts the following parameters:
 - `token`: Your Telegram API token.
 - `chat_id`: Unique identifier of the Telegram channel in which the image will be published.
 - `folder_name`: (optional) The name of the folder containing the images. If not specified, `images` will be used by default.
 - `image_name`: (optional) Name of the image to post. If not specified, a random image from the folder will be published.

#### Launch

The script can be run from the console using the command:

`python publish_images_bot.py [--folder_name FOLDER_NAME] [--image_name IMAGE_NAME]`

#### Arguments

- `--folder_name FOLDER_NAME`: (optional) The name of the folder containing the images. If not specified, the default folder name 'images' will be used.
- `--image_name IMAGE_NAME`: (optional) Name of the image to post. If not specified, a random image from the folder will be published.


### 6. Script `autopublish_images_bot.py`

This script publishes images to a specified Telegram channel at specific intervals. Images are randomly selected from the folder and published at a specified frequency.

#### Functions

- `autopublish_images(token, chat_id, folder_name, frequensy_of_publication)`: The main script function that accepts the following parameters:
 - `token`: Your Telegram API token.
 - `chat_id`: Unique identifier of the Telegram channel in which the images will be published.
 - `folder_name`: Name of the folder containing the images. The default is `images`.
 - `frequensy_of_publication`: Publication frequency in hours. By default, once every 4 hours. The frequency can be changed in the `.env` file.

#### Launch

The script can be run from the console using the following command:

`python autopublish_images_bot.py [--folder_name FOLDER_NAME]`

#### Arguments

- `--folder_name` Name of the folder containing the images. The default is `images`.

### 7. Script `common_scripts.py`

This script contains helper functions that are used in several other scripts. It is not intended to be run directly, but is imported and used by other scripts.

#### Functions

- `download_image(url, path)`: Downloads images and saves to the specified folder.
 - `url`: link to the image.
 - `path`: path to save the image.
- `get_extension(url)`: Retrieves and returns the file extension from the given image URL.
 - `url`: Image URL.
 - `get_date_from_epic(date)`: changes the date format to year/month/day/

### How to use

The functions of this script can be imported into other scripts and used as needed. For example, to import and use the `download_image` function, you can add the following line to the beginning of another script:

`from common_scripts import download_image`

Because `common_scripts.py` is a collection of utility functions, there are no command line arguments or specific instructions for running it directly.


## Objective of the project

The code was written for educational purposes in an online course for web developers [dvmn.org](https://dvmn.org/)