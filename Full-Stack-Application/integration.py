#API Integration
import requests 
import json

response = requests.get("https://v6.exchangerate-api.com/v6/c23c29d5c2e3e6c4fef36f9a/latest/USD")

response_json = json.loads(response.text)

c = response_json['conversion_rates']['CUP']
print(c)



#same as whats above
print(response_json['conversion_rates']['CUP'])

#can't fetch anyting and gets an error because conversion_rates is an entire dictionary of conversions, and not jusg a simple list so it can't get what you want and gets an error]
#print(response_json['conversion_rates'][1])

#still fetches first character of the string (originally USD, but now just fetches U, doesnt work with numbers,floats (number with decimal point ex. 3.14),integers (number without decimal point ex. 3), etc. but does work with lists, strings(this is a string. FYI: dictionaries are not subscriptable), etc.)
print(response_json['base_code'][0])

print(response_json['result'])

#0 fetches the first character of the string, should be monday and the date its next gonna update 
print(response_json['time_last_update_utc'][0])

for latest in response_json:
    if latest == 'conversion_rates':
        print(latest)

#makes better formatted json (foratting better)
pretty_print = json.dumps(response_json, indent=4)
print(pretty_print)

#if it has a squaree bracket [] before the {} brakcet you must doe [0] so that you are only in the root {} and from there you can call whatever you want inside the main function/dictionary
#print(f'') stands for a format string and shows formatting

G = response_json['base_code']

D = response_json['result']

#the 'f in the front of the string is for formatting and the {} with letters inside calls the letters above and puts them into the string
print(f'The current base code is {G} and the result of accessing the API is a {D}')