# -*- coding: utf-8 -*-
#API key: LIUW6C1L18053KXE

import requests
import json

# library used to generate the table format for the data
from prettytable import PrettyTable

# libraries used to generate bar and pie graph
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.pyplot as pltpie
import matplotlib.pyplot as pltStockCount


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
    # Based on the choice entered by the user a particular method is called in order to 
    # perform that operation
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
        # company is a list that stores the company symbol, shares, purchased at, latest price, value and gain/loss percentage value respectively in that order.
        if(company[0]==updateStockTicker): # if company is found, update the  price and share number for that stock.
            found = True
            updateStockPrice = float(input('Enter the updated stock price: '))
            updateStockNumber = float(input('Enter the updated stock share number: '))
            company[1] = updateStockNumber
            company[2] = updateStockPrice
            
            # need to recalculate the new value and gain/loss percentage since price was updated
            company[4] = round((company[3] * company[1]), 2)
            company[5] = round((((company[3] - company[2]) / company[2]) * 100), 2)
            break
    
    if(found == False):
        print('\n*** Stock could not be found with the ticker symbol provided! ***')
    else:
        print('\n*** Stock has been updated with the new price and share numbers! ***')
 

'''
    Function: Plots the gain/loss percentage of each company saved in the user's portfolio in the form of a bar graph
    Input: Takes in the number of companies in portfolio, gain/loss percentage of each stock and the name of each of the stock saved
            the user's portfolio
    Output: Gain/Loss Index plotted in the form of bar graph
'''

def plotGainLossBarGraph(y_pos, performance, objects):
    # Giving the data to the graph for which it is to be plotted
        #align -> used to align the bar graph in the center
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    
    # Labeling the x and y axis as well giving the bar graph a title.
    plt.xlabel('Portfolio Stock companies')
    plt.ylabel('Gain/Loss Percentage')
    plt.title('Stock Portfolio Gain/Loss Index') 
    plt.show()   
 
 
    
    
'''
    Function: Plots the total value of each stock as a percentage value compared to the other stocks in the portfolio
    Input: Takes in the value of each company in the portfolio, name of each company in the portfolio and
            an array 'explode' that is used to offset each wedge of the pie chart
    Output: Portfolio Stock Value Percentage Divison for each stock in the portfolio in the form
            of a pie graph
'''
def plotValuePercentage(valueIndex, objects, explode):
    # Passing in parameteres to the pie chart in order to plot it
        # labels -> array of company ticker symbols
        # autopct -> Used to indicate the no of digits displayed after decimal point in the pie graph
        # shadow -> adds a shadow effect to the pie chart
        # startangle -> provides the start angle for the wedge of the pie chart
    pltpie.pie(valueIndex, explode=explode, labels=objects, autopct='%1.1f%%', shadow=True, startangle=90)
    pltpie.axis('equal')
    pltpie.title('Portfolio Stock Value Percentage Division')
    pltpie.tight_layout()
    
    # plotting the pie chart
    pltpie.show()




'''
    Function: Plots the count of each stock purchased by the user and in the portfolio as a 
              percentage division value
    Input: Takes in the count of each stock in the portfolio, name of each company in the 
            portfolio and an array 'explode' that is used to offset each wedge of the pie chart
    Output: Stock count as a percentage division value of each company in the portfolio in the
            form of a pie graph
'''
def plotStockCountPercentage(countIndex, objects, explode):
    # Passing in parameteres to the pie chart in order to plot it
        # labels -> array of company ticker symbols
        # autopct -> Used to indicate the no of digits displayed after decimal point in the pie graph
        # shadow -> adds a shadow effect to the pie chart
        # startangle -> provides the start angle for the wedge of the pie chart
    pltStockCount.pie(countIndex, explode=explode, labels=objects, autopct='%1.1f%%', shadow=True, startangle=90)
    pltStockCount.axis('equal')
    pltStockCount.title('Portfolio Stock Share Count Percentage Division')
    pltStockCount.tight_layout()
    
    # plotting the pie chart
    pltStockCount.show()
    
    



''' Function: Prints the User's Portfolio Report based on the stocks in their portfolio
    Output:   User's Stock Portfolio Report
'''
# generates user's portfolio report
def generateUserPortfolio():
    print('\n\n\t\t\t\t Your User Portfolio Report Is: ')
    companyCount = 0
    totalValue = 0
    totalGL = 0
    
    # Array variables
        # objects -> stores the company tocker symbol
        # performance -> stores the gain/loss percentage for each company in the portfolio
        # valueIndex -> stores the value of each company in the portfolio
        # explode -> array that is used to separate each of the wedges corresponding to the pie chart
        # countIndex -> array that stores stock count of each company in the portfolio
        # valueObject -> array that stores the company ticker symbol as well as the value of each
        #               company in the portfolio within the same string. Used for printing out
        #               the legend in the portfolio stock value percentage division
        # shareCountObject -> array that stores the company ticker symbol as well as the stock count of each
        #               company in the portfolio within the same string. Used for printing out
        #               the legend in the portfolio stock share count percentage division
    objects = []
    performance = []
    
    valueIndex = []
    explode = []
    
    countIndex=[]
    
    valueObject = []
    shareCountObject = []
    
    # Tabulating User Portfolio Data
    table = PrettyTable(['Sl.No','Company Symbol', 'Shares','Purchased At', 'Latest Price', 'Value', 'Gain/Loss Percentage'])
    #print("This is company: ")
    for company in userPortfolio:
        objects.append(company[0])
        
        # Storing the company ticker symbol along with the value and share count of each stock in portfolio
        # to be used as legend in the pie charts
        value = company[0] + "[" + str(company[4]) + "]"
        valueObject.append(value)
        share = company[0] + "["+ str(company[1]) +"]"
        shareCountObject.append(share)
        
        # Stores info on the gain/loss, value and share count of each stock in the portfolio
        performance.append(company[5])
        valueIndex.append(company[4])
        explode.append(0.1)
        countIndex.append(company[1])
        
        
        # Calulate the total gain/loss and totalValue of the stock portfolio
        totalValue+=company[4]
        totalGL+=company[5]
        companyCount+=1
        #print(values[1])
        table.add_row([companyCount, company[0], company[1], company[2], company[3], company[4], company[5]])
    print(table)
    
    # Generating bar and pie graph with respect to gain/loss percentage, value and stock count
    # percentage division of each stock in the portfolio.
    
    y_pos = np.arange(len(objects))
    
    # Only if there are companies in the portfolio should the graphs be generated
    if(len(objects) !=0 ):
        plotGainLossBarGraph(y_pos, performance, objects)
        plotValuePercentage(valueIndex, valueObject, explode)
        plotStockCountPercentage(countIndex, shareCountObject, explode)
    
    
    print("\n\n Number of companies in stock portfolio: "+ str(companyCount))
    print("\n Total Value of all stocks: " + str(round(totalValue,2)))
    print("\n Total Gain/Loss Percentage: " + str(round(totalGL,2)))
    
    




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