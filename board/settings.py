from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


MBTA_API_KEY = os.getenv('MBTA_API_KEY')
BASE_URL = os.getenv('BASE_URL')
