# Stock Visualization Tool

This Python script creates a combined plot of stock price and revenue data for a given stock.

## Features

- Fetches stock price and revenue data from online sources
- Generates a dual-axis plot showing historical stock price and revenue
- Allows customization of the date range for the data
- Provides a clean and visually appealing data visualization

## Dependencies

The script requires the following Python libraries:

- `yfinance`: for fetching stock data
- `pandas`: for data manipulation
- `requests`: for making HTTP requests
- `BeautifulSoup`: for parsing HTML
- `plotly`: for creating the data visualization

You can install the required packages using pip:

```
pip install yfinance pandas requests beautifulsoup4 plotly
```

## Usage

1. Import the `make_graph` function from the script:

   ```python
   from stock_visualization import make_graph
   ```

2. Fetch the stock and revenue data:

   ```python
   stock_data = yf.download("AAPL", start="2016-01-01", end="2021-06-14")
   revenue_data = pd.read_csv("apple_revenue.csv")
   ```

3. Call the `make_graph` function with the data:

   ```python
   make_graph(stock_data, revenue_data, "Apple Inc.")
   ```

   This will generate a combined plot of the stock price and revenue data for Apple Inc.

## Example Output

The script will display a figure with two subplots:

1. Historical Share Price
2. Historical Revenue

The figure will include the following features:

- X-axis: Date
- Y-axis (left): Stock Price ($US)
- Y-axis (right): Revenue ($US Millions)
- Interactive zoom and pan functionality

## Contributing

If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
