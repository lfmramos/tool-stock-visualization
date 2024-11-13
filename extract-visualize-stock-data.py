import yfinance as yf # Import the yfinance library for fetching stock data
import pandas as pd # Import the pandas library for data manipulation
import requests # Import the requests library for making HTTP requests
from bs4 import BeautifulSoup # Import the BeautifulSoup library for parsing HTML
import plotly.graph_objects as go # Import the Plotly library for creating data visualizations
from plotly.subplots import make_subplots # Import the Plotly subplots function

# Ignore all warnings
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def make_graph(stock_data, revenue_data, stock):
    """
    Function to create a combined plot of stock price and revenue data.
    
    Parameters:
    stock_data (pandas.DataFrame): DataFrame containing the stock price data
    revenue_data (pandas.DataFrame): DataFrame containing the revenue data
    stock (str): The name of the stock
    """
    # Create a figure with two subplots (one for share price and one for revenue)
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing=.3)
    
    # Filter the data to only include records up to a specific date
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    
    # Add the stock price data to the first subplot
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), 
                             y=stock_data_specific.Close.astype("float"), 
                             name="Share Price"), 
                  row=1, col=1)
    
    # Add the revenue data to the second subplot
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), 
                             y=revenue_data_specific.Revenue.astype("float"), 
                             name="Revenue"), 
                  row=2, col=1)
    
    # Set the x-axis and y-axis titles for the subplots
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    
    # Update the layout of the figure
    fig.update_layout(showlegend=False,
                      height=900,
                      title=stock,
                      xaxis_rangeslider_visible=True)
    
    # Display the figure
    fig.show()