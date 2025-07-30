#Backend API Integration
import requests
import json
import os
from dotenv import load_dotenv
import yfinance as yf


load_dotenv()
API_KEY = os.getenv("Exchange_Rate_API")


class API:
    def __init__(self):
        self.api_key = API_KEY
        self.base_url = "https://v6.exchangerate-api.com/v6/"
        self.base_currency = "USD"
        self.api_url = f"{self.base_url}{self.api_key}/latest/{self.base_currency}"

    def get_conversion_rates(self):
        response = requests.get(self.api_url)
        #turns the string(response.text) into a dictionary(response_json)
        response_json = json.loads(response.text)
        return response_json['conversion_rates']
    
    # def get_conversion_currency(self):
    #     response = requests.get(self.api_url)
    #     response_json = json.loads(response.text)
    #     return response_json['conversion_rates']['currency']
        
api = API()
conversion_rates = api.get_conversion_rates()



# class STOCK:
#     def get_stock_price_usd(ticker):
#        stock = yf.Ticker(ticker)
#        return stock.info['regularMarketPrice']

class STOCK:
    def __init__(self):
        self.available_stocks = []

    def get_stock_price_usd(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.info.get("regularMarketPrice")
    def get_company_name(self, ticker):
            stock = yf.Ticker(ticker)
            return stock.info.get("longName")

class LOGIC:
    def __init__(self):
        self.available_stocks = []

    def get_math(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.info.get("regularMarketPrice")
































# print(conversion_rates)
# print(api.get_conversion_currency("AED"))
        
# response = requests.get("https://v6.exchangerate-api.com/v6/API_KEY/latest/USD")

# response_json = json.loads(response.text)

# d = response_json['conversion_rates']['USD']
# d_num = int(d)

# c = response_json['conversion_rates']['AED']
# converstion_number = float(c)

# print(d_num*converstion_number)
