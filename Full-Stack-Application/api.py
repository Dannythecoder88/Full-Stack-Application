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
import openai


load_dotenv()
# Allows us to import the iunfo from our .env file
API_KEY = os.getenv("Exchange_Rate_API")
API_KEY2 = os.getenv("OPENAI_API")
# Allows us to access our operating system through our os import, and get info from out .env file using our dotenv import and this then accesses our API key within the .env and lets it be turned into a variable so it is seceret when being pushed to github and doesn't show the actual key

#________________________________________________________________________________________________
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
# Sets Plotly as the default plotting backend for Pandas' built-in .plot() functions.



class GRAPH:
# Creates class called GRAPH
    def __init__(self):
        pass
    def get_company_history(self, ticker, period):
# Creates a method (function within a class) with to arguments (ticker and period)
# Ticker = stock symbol (ex. AAPL, MSFT)
# Period = how much historical data of stock trends you want
        stock = yf.Ticker(ticker)
# Initializes the ticker object from the yfinance (yf) library, thus allowing you to pull data for that stock ticker
        return stock.history(period=period)
# This calls the history() method (part of the yfinance library such as ticker.info, etc), and this method allows us to get the desired historical data such as stock trends for the specific desired time period that is chosen in the front end
    def generate_chart(self, df, chart_type, title="Stock Trends"):
# Creates a method with 3 arguments (df = dataframe), (chart_type = selected type of chart from frontend, and title = the title of the graph and has a default title of stock trends if no company is inputted)
        if chart_type == 'Standard':
# If the chart type chosen is standard then do as follows:
            return df.plot.line(title=title)
# Return a plot line graph from the plotly library that contains the information from the dataframe (which is the company that you previously chose in the front end, and this gets the history of te company chosen over the time period chosen)
# Ex of data frame in frontend: history = graph.get_company_history(stock_selection, time), which calls the history function and gets the company history for that time period chosen
        elif chart_type == 'CandleStick': 
# Else, if the chart type chosen is CandleStick, return as fullows:
            fig = go.Figure(go.Candlestick(
# Creates the full interactive candlestick chart, and go.Candlestick plots stock data using datafram columns which stores then info needed
                x=df.index,
# Sets the x-acis values to the index of the data frame, usually a measure over time on stock trends (uses the history variable in the front end as displayed above and gets the time fron the dataframe within the history variable)
                open=df['Open'],
# Sets the opening price for each candlestick, which comes from the 'Open' column of the dataframe
                high=df['High'],
# Sets the highest price for each candlestick, which comes from the 'High' column of the dataframe
                low=df['Low'],
# Sets the lowest price for each candlestick, which comes from the 'Low' column of the dataframe
                close=df['Close']
# Sets the closing price for each candlestick, which comes from the 'Close' column of the dataframe

            ))
# Wraps all the candlestick data in a Plotly Figure object called 'fig'. This object holds the full chart and is the variable it is all stored in which canbe seen in the first line of 

            fig.update_layout(title=title)
# Updates the layout of the chart to include a title.

            return fig
# Returns the completed Plotly figure object so it can be displayed elsewhere (ex. in Streamlit)

#_______________________________________________________________________________________________________

class TABLE():
# Creates a class called TABLE
    def generate_table(self, ticker, title="Info"):
# Creates a method that has two arguments (ticker takes the ticker for the company, and title creates a title, and if no company is inputted, a defaul title is used which is called info)
        stock = yf.Ticker(ticker)
# Initializes the ticker object from the yfinance (yf) library, thus allowing you to pull data for that stock ticker
        info = stock.info
# Pulls the .info function from the yfinance library, allowing us to pull information of the specific stock chosen, and it is stored in the variable 'info'
        fields = {
# Creates a dictionary contining the following, that is stored in a variable called fields
            "Long Name": info.get("longName"),
# Creates a key named 'Long Name' that has data from the yfinance library containing the full name of the company chosen
            "Sector": info.get("sector"),
# Creates a key named 'Sector' that has data from the yfinance library containing the sector of business that the company is associated with/in
            "Industry": info.get("industry"),
# Creates a key named 'Industry' that has data from the yfinance library containing the industry that the company chosen is associated with/in
            "City": info.get("city"),
# Creates a key named 'City' that has data from the yfinance library containing the  city the company is from
            "State": info.get("state"),
# Creates a key named 'State' that has data from the yfinance library containing the state the company is from
            "Website": info.get("website"),
# Creates a key named 'Website' that has data from the yfinance library containing the website that you can access the company from
            "Currency": info.get("currency"),
# Creates a key named 'Currency' that has data from the yfinance library containing the currency the company uses
            "Market Cap": info.get("marketCap"),
# Creates a key named 'Market Cap' that has data from the yfinance library containing the Market Cap of the company chosen
            "Regular Market Price": info.get("regularMarketPrice")
# Creates a key named 'Regular Market Price' that has data from the yfinance library containing the price a share of the company sells for 
        }

        labels = list(fields.keys())
# Takes all the keys (labels) from the fields dictionary and turn them into a list so I can use them in my chart
        values = list(fields.values())
# Takes all the values within the keys (values) from the fields dictionary and turn them into a list so I can use them in the chart
        fig = go.Figure(data=[go.Table(
# Creates a new Plotly figure that contains a table within the variable fig, that has everything that follows within the table itself:
            header=dict(values=["Field", "Value"],
# Names the columns, the first column is "Field", and the second is "Value"
                fill_color='blue',
# Fills the header row of the table with a blue background
                align='left'),
# Aligns the header text to the left
            cells=dict(values=[labels, values],
# Sets the contents of the table, by row, to have the first row contain the list of all the keys within the dictionary (Market Cap:, Currency:)
# Then sets the second row to be the values within each key, which pulls from the list made above called values, thus allowing each key to correspond to each value within it in a table (Ex. Market Cap: 3 Tirllion- the 3 Trillion is the value within the key that is being explain right now)
                fill_color='black',
# Sets the rows background color to be black
                align='left'))
# Aligns the text within each row to be to the left
        ])
        fig.update_layout(title=title)
# Updates the layout of the table to include a title
        return fig
# Returns the completed Plotly figure object so it can be displayed elsewhere (ex. in Streamlit)

#________________________________________________________________________________________________


class LOGIC:
    def __init__(self):
        pass 

    def usd_to_currency(self, amount, rate):
       return amount * rate
    def stock_to_shares(self,  stock_amount_usd, price1 ):
        return stock_amount_usd/price1
        
#________________________________________________________________________________________________

class AI:
    def __init__(self):
        pass 
    def get_ai_response(self, user_input):
        client = openai.OpenAI(api_key=API_KEY2)

        response = client.responses.create(
            model='gpt-4.1',
            input=[
                {
                    "role": "assistant",
                    "content": "You are a smart, confident Wall Street stock analyst who only responds to questions related to stock markets, currency conversion, or businesses that have a ticker in the yfinance library(stock tickers). You give moderate sized/long, professional answers with occasional references to market trends or ticker symbols. If a question is not related to stock, a bussiness that has a ticker (stock ticker), or currency, respond only with: \"Not a stock, business, or currency related question."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )
        return response.output_text

#________________________________________________________________________________________________



















# stock = STOCK()
# history = stock.get_company_history('AAPL')
# print(history)




# print(conversion_rates)
# print(api.get_conversion_currency("AED"))
        
# response = requests.get("https://v6.exchangerate-api.com/v6/API_KEY/latest/USD")

# response_json = json.loads(response.text)

# d = response_json['conversion_rates']['USD']
# d_num = int(d)

# c = response_json['conversion_rates']['AED']
# converstion_number = float(c)

# print(d_num*converstion_number)
