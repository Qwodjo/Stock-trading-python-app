import requests # requests module for making the api call
import os # os module for getting the environment variables
from dotenv import load_dotenv
load_dotenv()
import csv

POLYGON_API_KEY = os.getenv("POLYGON_API_KEY") # get the polygon api key from the environment variables

print(POLYGON_API_KEY)

LIMIT = 1000
url = f"https://api.polygon.io/v3/reference/tickers?market=stocks&active=true&order=asc&limit={LIMIT}&sort=ticker&apiKey={POLYGON_API_KEY}"
response = requests.get(url) # get the response from the url

tickers = []    # list of tickers

data = response.json() 
     # get the data from the response
for ticker in data ['results']:      # loop through the tickers
    tickers.append(ticker)   

    while 'next_url' in data: 
        print('requesting next page', data['next_url'])
        response = requests.get(data['next_url'] + f"&apiKey={POLYGON_API_KEY}")
        data = response.json()
        print(data)
        if 'error' in data:
            print(f"API Error: {data['error']}")
            break
        if 'results' not in data:
            print("No results in response, stopping.")
            break
        for ticker in data['results']:
            tickers.append(ticker)

print(len(tickers))      # print the list of tickers
   

example_ticker = {'ticker': 'PDT', 
'name': 'John Hancock Premium Dividend Fund', 
'market': 'stocks', 
'locale': 'us', 
'primary_exchange': 'XNYS', 
'type': 'FUND', 
'active': True, 
'currency_name': 'usd', 
'cik': '0000855886', 
'composite_figi': 'BBG000C2YBC6', 
'share_class_figi': 'BBG001S6DZY4', 
'last_updated_utc': '2025-09-15T06:04:58.61556849Z'}

# After fetching all tickers
csv_filename = 'tickers.csv'
fieldnames = [
    'ticker', 'name', 'market', 'locale', 'primary_exchange', 'type', 'active',
    'currency_name', 'cik', 'composite_figi', 'share_class_figi', 'last_updated_utc'
]
with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for ticker in tickers:
        # Only write the fields present in fieldnames
        row = {key: ticker.get(key, '') for key in fieldnames}
        writer.writerow(row)
print(f"Wrote {len(tickers)} tickers to {csv_filename}")
  