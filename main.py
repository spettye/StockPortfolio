# -*- coding: utf-8 -*-
#API key: LIUW6C1L18053KXE

import requests
import json



# requesting data from the api
#data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=LIUW6C1L18053KXE')
#print(data.status_code)
# returns data in json format
#print(data.json())

print('##########################')
print("Welcome to Stock Portfolio - where you can get all the data on the company you choose")
print('##########################')


company_name = input('Enter the name of the company whose ticker symbol you would like to know: ')
company_search = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+company_name+'&apikey=LIUW6C1L18053KXE')

print('Finding best results for the company that you entered: ')

best_results = company_search.json()['bestMatches']

for company in best_results:
    print('######################')
    print('Symbol: ' + company['1. symbol'])
    print('Name: ' + company['2. name'])
    print('Type: ' + company['3. type'])
    print('Region: ' + company['4. region'])
    print('Market Opens at: ' + company['5. marketOpen'])
    print('Market Closes at: ' + company['6. marketClose'])
    print('Timezone: ' + company['7. timezone'])
    print('Currency: ' + company['8. currency'])
    print('Match Score based on result: ' + company['9. matchScore'])
    print('$$$$$$$$$$$$$$$$$$$$$$')
    

company_symbol = input('Now that you have got the company you are looking for, enter its symbol to get the data you want with respect to it: ')
print('Data you are requesting for the company is: ')
data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+company_symbol+'&apikey=LIUW6C1L18053KXE')
# returns data in json format
pretty_json = json.dumps(json.loads(data.content), indent=2)
print(pretty_json)