#API key: LIUW6C1L18053KXE

import requests
# requesting data from the api
data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&apikey=LIUW6C1L18053KXE')
print(data.status_code)
# returns data in json format
print(data.json())
