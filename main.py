# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
import pandas_datareader.data as web

start = input ("Enter start date Year, Month, Date :") 
end = input ("Enter end date Year, Month, Date :")

ticker = input ("Enter ticker symbol of stock :")

df = web.DataReader(ticker, "yahoo", start, end) 

print(df.head()) #prints the the first five rows from start date
