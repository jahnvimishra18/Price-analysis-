# Product Pricing Analysis Tool

Welcome to the Product Pricing Analysis Tool! This tool is designed to help small business owners track their product prices compared to market trends, so they can make smarter pricing decisions.

## Project Overview

This project takes product data from a CSV file, compares it to market prices, and generates useful insights to guide pricing strategies.

## What's Inside

10EQS-Evaluation/
│-- data/
│   ├── products.csv       # Provided product data
│   ├── market_prices.json # Mocked market price data
│-- src/
│   ├── analysis.py        # Main script for analysis
│   ├── utils.py           # Helper functions
│-- .env.example           # Sample environment variable file
│-- README.md              # Setup guide (this file!)
│-- requirements.txt       # Dependencies
│-- report.md              # Generated insights

## Getting Started

Follow these simple steps to get up and running:

1. Clone the Repository

git clone <repo-link>
cd 10EQS-Evaluation

2. Install the Necessary Packages

Make sure you have Python installed, then run:

pip install -r requirements.txt

3. Run the Analysis

## To analyze your product prices, just run:

python src/analysis.py data/products.csv

This will compare your prices with market conditions and provide insights.

## What You'll Get

1. report.md - A summary of your pricing insights.

2. data/processed_products.csv - A CSV with price comparisons and recommendations.

3. price_comparison.png - A visual comparison of your prices vs market prices.

## What's in the Report?

The generated report.md will include:

1. Any data quality issues found

2. A summary of cleaned data

3. Market price comparisons

4. Business insights and recommendations

# Product Pricing Report

## Insights

- Organic Coffee Beans (1lb) is priced at $14.99 while the market price is $15.50. Suggested Action: Increase Price.
- Premium Green Tea (50 bags) is priced at $8.99 while the market price is $9.50. Suggested Action: Increase Price.

## Visualization

You'll get an easy-to-understand bar chart comparing your prices with market rates. The chart is saved as price_comparison.png.

## Known Limitations

1. The market prices are from a mock dataset, so for real analysis, update market_prices.json with actual values.

2. The tool assumes clean data; if your input has unexpected formats, adjustments may be needed.

# Estimated Time Breakdown

## Time Required

Setting up the environment - 15 mins

Data cleaning and processing - 20 mins

Generating insights - 15 mins

Creating visuals - 10 mins

## Future Improvements

1. We have ideas to make this even better:

2. Connect to live market data APIs.

3. Build a web interface for easier data management.

4. Add automated alerts when price trends change.

## License

This project is licensed under the MIT License.
