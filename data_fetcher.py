import requests
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
api_key = os.getenv("API_KEY")

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'
r = requests.get(url)
data = r.json()