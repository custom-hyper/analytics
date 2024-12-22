import pandas as pd
import time
import yfinance as yf

def fetch_yahoo_details(symbol):
    """
    Fetches all available details for a single symbol using Yahoo Finance.
    """
    try:
        stock = yf.Ticker(symbol)
        info = stock.info  # Retrieves all available details
        return info
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Load symbols from CSV file (assumes 'symbol' column in lowercase)
symbols_df = pd.read_csv('US_stock_symbols.csv')

# Ensure all symbols are in lowercase
symbols_df['symbol'] = symbols_df['symbol'].str.lower()

# Check if the DataFrame is empty
if symbols_df.empty:
    print("No symbols found in the CSV file.")
else:
    # Create a list to store detailed data
    detailed_data = []

    # Total symbols to process
    total_symbols = len(symbols_df)
    print(f"Total symbols to process: {total_symbols}")

    # Loop through all symbols, but stop after 5 symbols
    for index, row in symbols_df.iterrows():
        if index >= total_symbols:  # Stop after processing 5 rows
            break
        
        symbol = row['symbol']
        print(f"Processing symbol {index + 1}/{total_symbols}: {symbol}")
        
        details = fetch_yahoo_details(symbol)
        if details:
            # Append details to the list
            detailed_data.append(details)
            print(f"Successfully fetched data for {symbol}")

        # Show progress
        print(f"Progress: {index + 1}/{total_symbols} rows processed.")

        # Pause to avoid throttling (adjust if needed based on your experience)
        time.sleep(1)

    # Save detailed data to a CSV file
    if detailed_data:
        detailed_df = pd.DataFrame(detailed_data)
        output_file = 'us_symbols_with_all_details_yahoo_limited.csv'
        detailed_df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    else:
        print("No data fetched, CSV not created.")
