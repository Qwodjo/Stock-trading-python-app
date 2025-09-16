# Stock Trading Python App

This Python application allows you to fetch and save stock ticker data from the Polygon.io API. It is designed for anyone interested in analyzing or working with up-to-date stock market data in a convenient CSV format.

## What does this app do?
- Connects to the Polygon.io API to retrieve all active stock tickers in the US market.
- Handles API pagination automatically, so you get the complete list of tickers.
- Saves the ticker data to a CSV file (`tickers.csv`) with a clear, consistent schema.
- The CSV output includes fields such as ticker symbol, company name, market, exchange, type, and more.

## Features
- **Automated Data Fetching:** No manual downloads—just run the script and get the latest tickers.
- **CSV Export:** Data is saved in a standard CSV file for easy use in Excel, Python, or other tools.
- **Environment Variable Support:** Securely manage your Polygon API key using a `.env` file.
- **Error Handling:** The script will notify you if you hit API rate limits or if your API key is missing.

## Requirements
- Python 3.8 or higher
- `requests` library
- `python-dotenv` library
- A Polygon.io API key (free or paid, depending on your needs)

## How to Use
1. Install the required Python packages:
   ```sh
   pip install -r requirements.txt
   ```
2. Create a `.env` file in the project directory and add your Polygon API key:
   ```env
   POLYGON_API_KEY=your_api_key_here
   ```
3. Run the script:
   ```sh
   python data.py
   ```
4. After running, check for `tickers.csv` in your project folder. This file will contain all the fetched ticker data.

## Output Schema
The CSV file will have the following columns:
- ticker
- name
- market
- locale
- primary_exchange
- type
- active
- currency_name
- cik
- composite_figi
- share_class_figi
- last_updated_utc

## Notes
- Be aware of Polygon.io's API rate limits. If you exceed your quota, the script will stop and notify you.
- This app is ideal for personal, educational, or research use.

## License
This project is provided for educational and personal use.
