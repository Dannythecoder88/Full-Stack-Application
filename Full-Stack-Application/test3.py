import requests 
import json

response = requests.get("https://api.polygon.io/v3/reference/dividends?apiKey=aGq_7paKv6vFr1rRG59gaypSOpXorYWp")

response_json = json.loads(response.text)

#doesn'y fetch first letter as seen in integration .py, but instead since cash_amount is contained in a string, [#] fetches where within the string it is, if not put before the cash_amount an error would occur.

#GPT RESPONSE: response_json['results'] → a list

# response_json['results'][0] → the first dictionary in that list

# response_json['results'][0]['cash_amount'] → gets "cash_amount" from that dictionary


# print(response_json['results'][2]['pay_date'])

pretty_print = json.dumps(response_json, indent=4)
print(pretty_print)