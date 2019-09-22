# -*- coding: utf-8 -*-
#API key: LIUW6C1L18053KXE

import requests
import json
from prettytable import PrettyTable

userPortfolio =[]


def introduction():    
    # Introduction
    print('#####################################################################################################')
    print("\tWelcome to Stock Portfolio - where you can get all the data on the company you choose")
    print('#####################################################################################################')


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
    temp = []
    dictlist = []
    
    # Getting company data based on the ticker symbol
    company_symbol = input('Enter the symbol of the company whose data you would like to get: ')
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



def getUserChoice():
    print("\n\n\nWhat are you interested in doing:")
    print('1. Add Stocks to Portfolio (add)')
    print('2. Delete Stocks from Portfolio (delete)')
    print('3. Update stock price in Portfolio (update)')
    print('4. Generate Portfolio Report (report)')
    print('5. Search for a company profile (search)')
    print('6. Search for a company ticker symbol (ticker)')
    print('7. Quit (quit)')
    
    choice = input('Enter your choice: ')
    return choice


def userChoiceResponse(userChoice):
   if(userChoice=="search"):
       getCompanyData() 
   elif(userChoice=="add"):
       addPortfolioStocks()
   elif(userChoice=='delete'):
       removePortfolioStocks()
   elif(userChoice=='update'):
       updateStockPrice()
   elif(userChoice=='ticker'):
       getTickerSymbol()
   elif(userChoice=="report"):
       generateUserPortfolio()
   elif(userChoice=='quit'):
       print('\n\n\t\t\t\t Thank you for choosing our application! We hope to see you again!!!')
   else:
       print("Incorrect input entered. Please enter your choice again!")
        

def addPortfolioStocks():
    temp = []
    dictlist = []
    
    getTickerSymbol()
    userTickerSymbol = input('Enter the ticker symbol of the company that you want to add to the portfolio: ')   
    companySearchData = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ userTickerSymbol+'&interval=5min&apikey=LIUW6C1L18053KXE')     
    
    #print(companySearchData.json()['Time Series (5min)'])
    
    # Gets the latest value of the company to add it to the portfolio
    for key,value in companySearchData.json()['Time Series (5min)'].items():
        temp = [key,value]
        dictlist.append(temp)
    print(dictlist[0][1]['4. close'])
    
    latest = float(dictlist[0][1]['4. close'])
    purchase = float(input('At that price did you purchase the stock: '))
    noShares = float(input('How many shares did you purchase: '))
    value = round((latest * noShares), 2)
    percentage = round((((latest - purchase) / purchase) * 100), 2)
    
    userPortfolio.append([userTickerSymbol, noShares, purchase, latest, value, percentage])
    print('User Portfolio: ')
    print(userPortfolio)
    #print(type(float(purchase)))
    #print(type(float(noShares)))


def removePortfolioStocks():
    removeStockTicker = input('Enter company ticker symbol whose stock you would like to delete from the portfolio: ')
    length = len(userPortfolio)
    i=0
    count=0
    
    # only deletes first instance of the stock and not all instances
    while(i<length):
    	if(userPortfolio[i][0]==removeStockTicker):
            userPortfolio.remove(userPortfolio[i])
            count+=1	
            length = length -1 # as an element is removed so decrease the length by 1 
            continue # run loop again to check element at same index, when item removed next item will shift to the left
    	i = i+1
    
    if(count>0):
        print('All instances of the stocks with the ticker symbol '+ removeStockTicker +' that were found in the portfolio have been removed.')
    else:
        print('No instance of the stock with ticker symbol ' + removeStockTicker + ' were found in the portfolio.')
    
    print(userPortfolio)

            
# updates only first instance of the company
def updateStockPrice():
    updateStockTicker = input('Enter the company ticker symbol whose stock price you want to update: ')
    for company in userPortfolio:
        if(company[0]==updateStockTicker):
            updateStockPrice = float(input('Enter the updated stock price: '))
            updateStockNumber = float(input('Enter the updated stock share number: '))
            company[1] = updateStockNumber
            company[2] = updateStockPrice
    
    print(userPortfolio)
    

# generates user's portfolio report
def generateUserPortfolio():
    print('\n\n\t\t\t\t Your User Portfolio Report Is: ')
    companyCount = 0
    # Tabulating user Portfolio Data
    table = PrettyTable(['Sl.No','Company Symbol', 'Shares','Purchased At', 'Latest Price', 'Value', 'Gain/Loss Percentage'])
    for company in userPortfolio:
        companyCount+=1
        #print(values[1])
        table.add_row([companyCount, company[0], company[1], company[2], company[3], company[4], company[5]])
    print(table)




def main():
    #code starts executing from here
    #print("Hello World!")
   # getUserChoice()
   userChoice = ''
   introduction()
   while(userChoice!='quit'):
       userChoice = getUserChoice().lower()
       userChoiceResponse(userChoice)
   
   #print('User choice is: ' + userChoice)

if __name__=="__main__":
    main()