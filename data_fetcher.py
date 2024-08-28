import requests
from dotenv import load_dotenv
import os
import pandas as pd
import requests_cache


def fetch(symbol):
    load_dotenv()
    api_key = os.getenv("API_KEY")

    session = requests_cache.CachedSession('api_cache', expireexpire_after=300) # Cache expires after 5 minutes

    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=5min&apikey={api_key}'

    try:
        response = session.get(url, timeout=3)
        response.raise_for_status() # raises error

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
        return df

    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
    except requests.exceptions.ConnectionError as errc:
        print ("Connection Error:",errc)
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
        # TODO add retries
    except requests.exceptions.RequestException as err:
        print ("Request Error",err)

    # TODO add rate limit handling if 5000 limit ever exceeded