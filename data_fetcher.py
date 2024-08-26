import requests
from dotenv import load_dotenv
import os
import pandas as pd
import requests_cache

load_dotenv()
api_key = os.getenv("API_KEY")

session = requests_cache.CachedSession('api_cache', expireexpire_after=300) # Cache expires after 5 minutes

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey={api_key}'

response = session.get(url)
data = response.json()

time_series_data = data['Time Series (5min)']
df = pd.DataFrame.from_dict(time_series_data, orient='index') # dict keys are row indexes
df.columns = ['Open', 'High', 'Low', 'Close', 'Volume'] # rename columns
df.index = pd.to_datetime(df.index) # convert index to datetime
df = df.astype({
    'Open': 'float',
    'High': 'float',
    'Low': 'float',
    'Close': 'float',
    'Volume': 'int'
}) # convert prices and volume types
print(df)