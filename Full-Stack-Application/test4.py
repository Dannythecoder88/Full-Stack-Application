import yfinance as yf


ticker = yf.Ticker("AAPL") 

price = ticker.info['regularMarketPrice']
name = ticker.info['longName']
sector = ticker.info['sector']

print("Name:", name)
print("Price (USD):", price)
print("Sector:", sector)
