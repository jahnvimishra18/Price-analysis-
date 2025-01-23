import sys
import pandas as pd
from utils import read_product_data, get_market_price
import matplotlib.pyplot as plt

def analyze_products(file_path):
    df = read_product_data(file_path)

    # Fetch market prices for all products
    df['market_price'] = df['product_name'].apply(get_market_price)

    # Calculate price differences and identify pricing insights
    df['price_difference'] = df['market_price'] - df['our_price']
    df['recommendation'] = df.apply(
        lambda row: 'Increase Price' if row['our_price'] < row['market_price'] else 'Consider Discount',
        axis=1
    )

    # Saving data
    df.to_csv('data/processed_products.csv', index=False)

    # Generate report
    generate_report(df)

    # Generate visualization
    plot_price_comparison(df)
    
 #Generate a business insights report
def generate_report(df):
   
    with open('report.md', 'w') as report:
        report.write("# Product Pricing Report\n\n")
        report.write("## Insights\n\n")
        for _, row in df.iterrows():
            if row['market_price']:
                report.write(f"- {row['product_name']} is priced at ${row['our_price']} "
                             f"while the market price is ${row['market_price']}. "
                             f"Suggested Action: {row['recommendation']}\n")
            else:
                report.write(f"- No market price data found for {row['product_name']}\n")

    print("Analysis complete. Check report.md for details.")
#Generate visualization comparing our prices to market prices
def plot_price_comparison(df):
    
    df.dropna(subset=['market_price'], inplace=True)
    bar_width = 0.35
    index = range(len(df))

    plt.figure(figsize=(12, 7))
    plt.bar(index, df["our_price"], bar_width, label="Our Price", color='royalblue')
    plt.bar([i + bar_width for i in index], df["market_price"], bar_width, label="Market Price", color='orangered')

    plt.xlabel('Products')
    plt.ylabel('Price (USD)')
    plt.title('Comparison of Our Price vs Market Price')
    plt.xticks([i + bar_width / 2 for i in index], df["product_name"], rotation=30, ha="right")
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.savefig("price_comparison.png")
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/analysis.py data/products.csv")
    else:
        analyze_products(sys.argv[1])
