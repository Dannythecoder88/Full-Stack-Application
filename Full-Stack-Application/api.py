#Backend API Integration

import requests
# Allows us to use .get or .pull functions, thus allowing us to get data from the api being used
import json
# Allows us to convert json strings (usually from an API) into something python can use like a dictionary
import os
# Allows us to access other files in the operating system
from dotenv import load_dotenv
# Allows us to use infornation from our .env file (suually api keys)
import yfinance as yf
#Imports from a public api that doesnt need a key and allows us to gather data from yahoo finance
import pandas as pd
import plotly.graph_objects as go


load_dotenv()
# Allows us to import the iunfo from our .env file
API_KEY = os.getenv("Exchange_Rate_API")
# Allows us to access our operating system through our os import, and get info from out .env file using our dotenv import and this then accesses our API key within the .env and lets it be turned into a variable so it is seceret when being pushed to github and doesn't show the actual key

class API:
# Creates a class called API
    def __init__(self):
# This is a function within a class (method) and allows us to call our attributes using the "self" and replacing it with whatever variable you set the class to be equal to (ex. "api = API()") this allows us to call an attribute below using the variable api (ex. api.get_conversion_rates)
        self.api_key = API_KEY
# This is an attribute of the API class allows us to store the api key within it
        self.base_url = "https://v6.exchangerate-api.com/v6/"
# This is an attribute that stores the base part of the api url, whil will later on come together to form thw whole url so we can access the api through the url itself
        self.base_currency = "USD"
# This is an attribute that stores the base currency we will be using in our app and in our api
        self.api_url = f"{self.base_url}{self.api_key}/latest/{self.base_currency}"
# This brinbgs together the previous attributes above, and puts them together to forma proper url for the api we are using, thus allowing us to access our api with the url that includes the api key which allows us to get data and use it in our application

    def get_conversion_rates(self):
# This is a method (function within a class)
        response = requests.get(self.api_url)
# This allows us to make a request to the api url using a .get call, which allows us to access information from the api being used and it stores it in a variable called response
        response_json = json.loads(response.text)
# This converts the JSON string (response.text), which contains raw data from the API, into a Python dictionary (response_json)
        return response_json['conversion_rates']
# This accesses the response_json dictionary that was parssed from the original json string(parsed means taken friom/edited, in this case editted into a python dictionary) and allows us to access the specific values stored within "conversion_rates" that was in the api's information, which gets us the conversion rates for the many different currencies in the API itself

#whats below didn't work becuase api.get_conversion_rates.keys() worked better and was simpler to incorporate because the key was the currency and what was stored within it was the conversion rates
    # def get_conversion_currency(self):
    #     response = requests.get(self.api_url)
    #     response_json = json.loads(response.text)
    #     return response_json['conversion_rates']['currency']
        
api = API()
#stores the call to the API class in a variable called api
conversion_rates = api.get_conversion_rates()
# This calls the 'get_conversion_rates' method on the 'api' object.
# It runs the function defined inside the API class and returns the conversion rates from the API.

# Inside the class, 'self' refers to the current object (in this case, 'api').
# When we call 'api.get_conversion_rates()', Python automatically passes 'api' as 'self' to the method.
# So, 'self' is not a normal variable; it represents the instance (the specific object).
# This allows the method to access or change the object's data and call other methods.

#_______________________________________________________________________________________________________

class STOCK:
#Creates a class called STOCK
    def __init__(self):
# This is a function within a class (method) and allows us to call our attributes using the "self" and replacing it with whatever variable you set the class to be equal to (ex. "api = API()") this allows us to call an attribute below using the variable api (ex. api.get_conversion_rates)
        self.available_stocks = []
# Creates an empty list called self.available stocks (Not needed anymore)
    def get_stock_price_usd(self, ticker):
    # Defines a method inside the class that takes two parameters:
    # 'self', which represents the instance (the object calling the method),
    # and 'ticker', a variable that specifies the stock symbol to look up (like "AAPL").
    # This method will use 'ticker' to access stock price data from the Yahoo Finance API.
        stock = yf.Ticker(ticker)
# Creates a yfinance Ticker object/variable (stock) for the given stock symbol, which is referred to as a 'ticker' (ex. AAPL for Apple)
        return stock.info.get("regularMarketPrice")
# Allows us to get the market prices for the particular stock ticker we chose (ex. if we eneter AAPL, we would get the price of a stock of Apple)
    def get_company_name(self, ticker):
# Defines a method inside the class that takes two parameters:
    # 'self', which represents the instance (the object calling the method),
    # and 'ticker', a variable that specifies the stock symbol to look up (like "AAPL").
    # This method will use 'ticker' to access stock price data from the Yahoo Finance API.
        stock = yf.Ticker(ticker)
# Creates a yfinance Ticker object/variable  (stock) for the given stock symbol, which is referred to as a 'ticker' (ex. AAPL for Apple)    
        return stock.info.get("longName")
# This allows is to access the name of the stock we chose by acessing the yfinance api
   
#_______________________________________________________________________________________________________

pd.options.plotting.backend = "plotly"

class GRAPH:
    def __init__(self):
        pass
    def get_company_history(self, ticker, period):
        stock = yf.Ticker(ticker)
        return stock.history(period=period)

    def generate_chart(self, df, chart_type, title="Stock Trends"):
        if chart_type == 'Standard':
            return df.plot.line(title=title)
        fig = go.Figure(go.Candlestick(
            x=df.index,
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close']
        ))
        fig.update_layout(title=title)
        return fig

#_______________________________________________________________________________________________________

class TABLE():
    def generate_table(self, ticker, title="Info"):
        stock = yf.Ticker(ticker)
        info = stock.info

        fields = {
            "Long Name": info.get("longName"),
            "Sector": info.get("sector"),
            "Industry": info.get("industry"),
            "Country": info.get("country"),
            "City": info.get("city"),
            "State": info.get("state"),
            "Website": info.get("website"),
            "Currency": info.get("currency"),
            "Market Cap": info.get("marketCap"),
            "Regular Market Price": info.get("regularMarketPrice")
        }

        labels = list(fields.keys())
        values = list(fields.values())

        fig = go.Figure(data=[go.Table(
            header=dict(values=["Field", "Value"],
                fill_color='blue',
                align='left'),
            cells=dict(values=[labels, values],
                fill_color='black',
                align='left'))
        ])
        fig.update_layout(title=title)
        return fig










# stock = STOCK()
# history = stock.get_company_history('AAPL')
# print(history)

# class LOGIC:
#     def __init__(self):
#         self.available_stocks = [] 

#     def get_math(self, ticker):
#         stock = yf.Ticker(ticker)
#         return stock.info.get("regularMarketPrice")
































# print(conversion_rates)
# print(api.get_conversion_currency("AED"))
        
# response = requests.get("https://v6.exchangerate-api.com/v6/API_KEY/latest/USD")

# response_json = json.loads(response.text)

# d = response_json['conversion_rates']['USD']
# d_num = int(d)

# c = response_json['conversion_rates']['AED']
# converstion_number = float(c)

# print(d_num*converstion_number)
