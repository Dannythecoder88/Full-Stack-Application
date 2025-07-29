import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/API_KEY/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
		