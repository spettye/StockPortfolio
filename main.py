# -*- coding: utf-8 -*-
#API key: LIUW6C1L18053KXE

import requests
import json
from prettytable import PrettyTable

temp = []
dictlist = []

def introduction():    
    # Introduction
    print('#####################################################################################')
    print("Welcome to Stock Portfolio - where you can get all the data on the company you choose")
    print('#####################################################################################')


def getTickerSymbol():
    count_companies = 0
    
    # Getting ticker symbol for company whose data the user wants            
    company_name = input('Enter the name of the company whose ticker symbol you would like to know: ')
    company_search = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+company_name+'&apikey=LIUW6C1L18053KXE')
    print('\n\n\n\t Finding best results for the company that you entered: ')
    best_results = company_search.json()['bestMatches']
        
    # Tabulating company symbol data
    s = PrettyTable(['Sl.No','Symbol','Name', 'Type', 'Region','Currency','Match Score'])
    for company in best_results:
        count_companies+=1
        s.add_row([count_companies,company['1. symbol'], company['2. name'], company['3. type'], company['4. region'], company['8. currency'], company['9. matchScore']])    
    print(s)

def getCompanyData():
    count = 0
    
    # Getting company data based on the ticker symbol
    company_symbol = input('Now that you have got the company you are looking for, enter its symbol to get the data you want: ')
    print('\n\t Data you are requesting for the company with ticker symbol '+ company_symbol +' is: ')
    data = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+company_symbol+'&apikey=LIUW6C1L18053KXE')
    #print("$$$$$$$$ Data: $$$$$$$")
       
    # data contains all the important information about the company. data.json() converts that data into json format.
    #print(data.json())
    pretty_json = json.dumps(json.loads(data.content), indent=2) # returns data in json format
    #print(pretty_json)
    #print(data.json()['Time Series (Daily)'].items())
       
    # Converting json data into a list data 
    for key,value in data.json()['Time Series (Daily)'].items():
        temp = [key,value]
        dictlist.append(temp)
       
    # Tabulating company data
    t = PrettyTable(['Sl.No','Date','Open', 'High', 'Low', 'Close', 'Volume'])
    for values in dictlist:
        count+=1
        #print(values[1])
        t.add_row([count,values[0], values[1]['1. open'], values[1]['2. high'], values[1]['3. low'], values[1]['4. close'], values[1]['5. volume']])
    print(t)


def main():
    #code starts executing from here
    #print("Hello World!")
    getTickerSymbol()
    getCompanyData()

if __name__=="__main__":
    main()