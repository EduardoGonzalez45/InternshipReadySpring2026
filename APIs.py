import requests
from dotenv import load_dotenv
import os

def apod_generator(url, unique_key):
    final_url = url + unique_key
    response = requests.get(final_url).json()
    return response