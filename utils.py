import requests
from auth import data
import os

DATA_FOLDER = os.path.join(os.path.dirname(__file__),'data')



def get_data_full(day=1):
    print(DATA_FOLDER)
    if not os.path.exists(os.path.join(DATA_FOLDER,
                                       'full',
                                       str(day))):
        url = f"https://adventofcode.com/2024/day/{day}/input"
        cookies = {
            "session": data
        }
        response = requests.get(url, cookies=cookies)

        with open(os.path.join(DATA_FOLDER,
                               'full',
                               str(day)), 'w') as f:
            f.write(response.text)

        with open(os.path.join(DATA_FOLDER,
                               'test',
                               str(day)), 'w') as f:
            f.write(response.text)