from openai.types.responses import response
import yfinance as yf
import os
from dotenv import load_dotenv
import openai




# ticker = yf.Ticker("AAPL") 

# price = ticker.info['regularMarketPrice']
# name = ticker.info['longName']
# sector = ticker.info['sector']
# history = ticker.history(period='1mo')

# print("Name:", name)
# print("Price (USD):", price)
# print("Sector:", sector)
# print("history:", history)

# print(ticker.info)



load_dotenv()

API_KEY2 = os.getenv("OPENAI_API")


client = openai.OpenAI(api_key=API_KEY2)

response = client.responses.create(
    model='gpt-4.1',
    input="tell me a story in 500 characters"
)
print(response)