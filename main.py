# -*- coding: utf-8 -*-
#API key: LIUW6C1L18053KXE

import requests
import json
from prettytable import PrettyTable

# All user interested portfolio stocks will be stored here.
userPortfolio =[]

'''
    Function: Print Introduction Element of the program.
'''
def introduction():    
    # Introduction
    print('#####################################################################################################')
    print("\tWelcome to Stock Portfolio - where you can get all the data on the company you choose")
    print('#####################################################################################################')






'''
    Function: Returns the ticker symbol of the company that the user is looking for. 
    Input:    Takes the name of the company that the user is looking for
    Output:   Returns the ticker symbol of the company.
'''
def getTickerSymbol():
    count_companies = 0
    
    # Getting ticker symbol for company whose data the user wants            
    company_name = input('Enter the name of the company whose ticker symbol you would like to know: ')
    company_search = requests.get('https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords='+company_name+'&apikey=LIUW6C1L18053KXE')
    print('\n\n\n\t Finding best results for the company that you entered: ')
    best_results = company_search.json()['bestMatches']
        
    # Tabulating company symbol data using PrettyTable
    s = PrettyTable(['Sl.No','Symbol','Name', 'Type', 'Region','Currency','Match Score'])
    for company in best_results:
        count_companies+=1
        s.add_row([count_companies,company['1. symbol'], company['2. name'], company['3. type'], company['4. region'], company['8. currency'], company['9. matchScore']])    
    print(s)
    




'''
    Function: Allows to get a day by day record of the company that the user is interested in knowing about
    Input:    Takes the ticker symbol of the company that user is interested in
    Output:   Data includes open, high, low, close and volume information about the company
'''
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



'''
    Function: Determine the user's choice in order to proceed with the application.
    Input:    Selection that the user is interested in
'''
def getUserChoice():
    print("\n\n\nWhat are you interested in doing:")
    # Each print statement includes the choice available to the user as well as
    # the command, in brackets, in order to trigger it.
    print('1. Add Stocks to Portfolio (add)')
    print('2. Delete Stocks from Portfolio (delete)')
    print('3. Update stock price in Portfolio (update)')
    print('4. Generate Portfolio Report (report)')
    print('5. Search for a company profile (search)')
    print('6. Search for a company ticker symbol (ticker)')
    print('7. Quit (quit)')
    
    choice = input('Enter your choice: ')
    return choice



'''
    Function: Based on user choice, passes control over of the program to the respective function
    Input:    Takes in the user selection choice
    Output:   Passing over control to different methods depending on the user selected choice
'''
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
       print("\nIncorrect input entered. Please enter your choice again!")
        


'''
    Function: Adds portfolio stocks that the user is interested in into his profile
    Input:    Takes in the ticker symbol of the company that the user is interested in
    Output:   Stock is added to the user's profile with important information about the company
'''
def addPortfolioStocks():
    temp = []
    dictlist = []
    
    # Providing the option to the user to determine the ticker symbol of the company that they are intersted in adding to their portfolio.
    getTickerSymbol()
    
    # Once they have the ticker symbol, we use that info to obtain the data for the company they are intersted in knowing about
    userTickerSymbol = input('Enter the ticker symbol of the company that you want to add to the portfolio: ')   
    companySearchData = requests.get('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ userTickerSymbol+'&interval=5min&apikey=LIUW6C1L18053KXE')     
    
    #print(companySearchData.json()['Time Series (5min)'])
    
    # Gets the latest value of the company to add it to the portfolio
    for key,value in companySearchData.json()['Time Series (5min)'].items():
        temp = [key,value]
        dictlist.append(temp)
    print('\nThe current stock price is: ' + dictlist[0][1]['4. close'])
    
    
    # We provide the latest stock price of the moment so that the user's stock portfolio is in real-time
    latest = float(dictlist[0][1]['4. close'])
    # Taking in the purchase value and number of shares from the user.
    purchase = float(input('At that price did you purchase the stock: '))
    noShares = float(input('How many shares did you purchase: '))
    # Running calculations to help the user out with their portfolio
    value = round((latest * noShares), 2)
    percentage = round((((latest - purchase) / purchase) * 100), 2)
    
    # Stock is then added to the user's portfolio to be tracked.
    userPortfolio.append([userTickerSymbol, noShares, purchase, latest, value, percentage])
    print('\n*** Stock has been successfully added to your portfolio! ***')
    #print('User Portfolio: ')
    #print(userPortfolio)
    #print(type(float(purchase)))
    #print(type(float(noShares)))


'''
    Function: Removes all instances of the stock from the user's portfolio depending on user's choice
    Input:    Takes in the company ticker symbol which the user wants to remove from the portfolio
    Output:   Stock is deleted from the user's stock portfolio if it exists there.
'''
def removePortfolioStocks():
    removeStockTicker = input('Enter company ticker symbol whose stock you would like to delete from the portfolio: ')
    length = len(userPortfolio)
    i=0
    count=0
    
    # deletes all instances of the stock
    while(i<length):
    	if(userPortfolio[i][0]==removeStockTicker):
            userPortfolio.remove(userPortfolio[i])
            count+=1	
            length = length -1 # as an element is removed so decrease the length by 1 
            continue # run loop again to check element at same index, when item removed next item will shift to the left
    	i = i+1
    
    if(count>0):
        print('\n*** All instances of the stocks with the ticker symbol '+ removeStockTicker +' that were found in the portfolio have been removed! ***')
    else:
        print('\n*** No instance of the stock with ticker symbol ' + removeStockTicker + ' were found in the portfolio! ***')
    
    #print(userPortfolio)

          
    
'''
    Function: Updates the first instance of the company stock in the portfolio
    Input:    Ticker symbol of the company whose stock price needs updating
    Output:   User portfolio now updated with the new stock price that the user purchased at
'''    
# updates only first(oldest) instance of the company stock in the portfolio
def updateStockPrice():
    found = False
    #print(userPortfolio)
    updateStockTicker = input('Enter the company ticker symbol whose stock price you want to update: ')
    for company in userPortfolio:
        if(company[0]==updateStockTicker): # if company is found, update the  price and share number for that stock.
            found = True
            updateStockPrice = float(input('Enter the updated stock price: '))
            updateStockNumber = float(input('Enter the updated stock share number: '))
            company[1] = updateStockNumber
            company[2] = updateStockPrice
            company[4] = round((company[3] * company[1]), 2)
            company[5] = round((((company[3] - company[2]) / company[2]) * 100), 2)
            break
    
    if(found == False):
        print('\n*** Stock could not be found with the ticker symbol provided! ***')
    else:
        print('\n*** Stock has been updated with the new price and share numbers! ***')
    

''' Function: Prints the User's Portfolio Report based on the stocks in their portfolio
    Output:   User's Stock Portfolio Report
'''
# generates user's portfolio report
def generateUserPortfolio():
    print('\n\n\t\t\t\t Your User Portfolio Report Is: ')
    companyCount = 0
    totalValue = 0
    totalGL = 0
    # Tabulating User Portfolio Data
    table = PrettyTable(['Sl.No','Company Symbol', 'Shares','Purchased At', 'Latest Price', 'Value', 'Gain/Loss Percentage'])
    #print("This is company: ")
    for company in userPortfolio:
        print(company)
        totalValue+=company[4]
        totalGL+=company[5]
        companyCount+=1
        #print(values[1])
        table.add_row([companyCount, company[0], company[1], company[2], company[3], company[4], company[5]])
    print(table)
    print("\n\n Number of companies in stock portfolio: "+ str(companyCount))
    print("\n Total Value of all stocks: " + str(totalValue))
    print("\n Total Gain/Loss Percentage: " + str(totalGL))




def main():
    #code starts executing from here
    #print("Hello World!")
   #getUserChoice()
   userChoice = ''
   introduction()
   # Keeps displaying the choices until user enters quit
   while(userChoice!='quit'):
       userChoice = getUserChoice().lower()
       userChoiceResponse(userChoice)
   
   #print('User choice is: ' + userChoice)

if __name__=="__main__":
    main()