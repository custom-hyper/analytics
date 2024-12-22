import requests
import pandas as pd

# Replace with your Alpha Vantage API key
API_KEY = "YOUR API KEY"
BASE_URL = 'https://www.alphavantage.co/query'

def get_all_us_symbols():
    """
    Fetches all stock symbols listed in US exchanges using Alpha Vantage's "Listing Status" endpoint.
    """
    params = {
        'function': 'LISTING_STATUS',
        'apikey': API_KEY
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        from io import StringIO
        data = StringIO(response.text)
        df = pd.read_csv(data)
        return df  # Returns all symbols from the CSV response
    else:
        print("Error fetching data:", response.text)
        return None

# Fetch all US symbols
symbols_df = get_all_us_symbols()
if symbols_df is not None:
    # Display first few rows
    print(symbols_df[['symbol', 'name', 'exchange']].head())
    
    # Save to CSV file
    output_file = 'us_stock_symbols.csv'
    symbols_df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")
