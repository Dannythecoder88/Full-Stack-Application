import requests

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/c23c29d5c2e3e6c4fef36f9a/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
		