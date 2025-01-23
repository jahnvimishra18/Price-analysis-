import pandas as pd
import json

def read_product_data(file_path):
    #read and clean product data from CSV
    df = pd.read_csv(file_path)

    # Clean up and handle missing data
    df['our_price'] = pd.to_numeric(df['our_price'].astype(str).str.replace('$', ''), errors='coerce')
    df['current_stock'] = pd.to_numeric(df['current_stock'].replace('out of stock', '0'), errors='coerce')
    df.fillna({'our_price': 0, 'current_stock': 0, 'restock_threshold': 0}, inplace=True)

    return df

def get_market_price(product_name):
    #Fetch product price from mocked external source (JSON file)
    with open('data/market_prices.json', 'r') as f:
        market_prices = json.load(f)

    return market_prices.get(product_name, None)
