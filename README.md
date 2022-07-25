[![Board Status](https://dev.azure.com/pettyelnlsb/33d6211d-43a2-4815-bc78-00291eb6b790/6a2248c0-5d7a-4fbb-93bd-78270e404170/_apis/work/boardbadge/dab78722-258f-4a6e-9fb8-f4193c3021b5)](https://dev.azure.com/pettyelnlsb/33d6211d-43a2-4815-bc78-00291eb6b790/_boards/board/t/6a2248c0-5d7a-4fbb-93bd-78270e404170/Microsoft.RequirementCategory)
# StockPortfolio

Hi everyone! Welcome to Stock Portfolio - an application where you can track changes in stock prices and perform CRUD operations on a set of stocks that you can choose to add to your portfolio. 

This application was developed by [Stephen Pettye](https://github.com/spettye), Imad Basharat and [Akshay Mysore](https://github.com/Akshay199456).


## Steps to complete before running the application.


1. Currently using the [Alpha Advantage API](https://www.alphavantage.co/documentation/). In order to use this api, you will need to install the [package](https://alpha-vantage.readthedocs.io/en/latest/) gives easy instructions on using this api. Once you have it installed, you will need to register with the website in order to get an API key which is basically filling out the form at this [link](https://www.alphavantage.co/support/#api-key). 
				
							OR

2. Clone this repo and use the command 'git init' in order to install the dependencies.


You will now be able to use the API and can visit this [link](https://www.alphavantage.co/documentation/) to get the documentation on how to use the API

## Why this application

If you have ever had to deal with stocks and spend money trading, it becomes crucial to being able to manage and keep track of stocks that you have invested in order to maximize your profits. As a result, we decided to work upon this application to help us understand the inner workings of how companies maintain stock portfolios of their clients and how to improve performance with respect to it. 

## Features

Users of the application have the ability to perform multiple operations to the stocks/portfolio with the commands for each given within the bracket:

1. Add stocks to the portfolio (add).
2. Delete Stocks from Portfolio (delete).
3. Update stock price in Portfolio (update).
4. Generate Portfolio Report (report).
5. Search for a company profile (search).
6. Search for a company ticker symbol (ticker).

When the users of the application generate a portfolio report, they are also provided with bar and pie graphs that help them understand their stock portfolio better.

## Future Additions

While we have been happy with the work we put into the application, there are features which we were interested in adding into our application as well. However, as this was primarily a course project with a duration of 1.5 months, we were able only able to implement the fundamental features into our application. A list of possible future features that will be implemented into our application include:

1. Tracking performance (daily as well as historical)
2. Rebalancing (Obtaining original weightings of assets over time)
3. Portfolio optimization (generating the minimum variance portfolio)
4. Risk-adjusted metrics (Sharpe Ratio, Alpha, etc.)
5. Portfolio Fundamentals (Beta, P/E Ratio, Dividend Yield, etc.)
6. Graphing abilities (Correlation Heatmaps, etc.)
7. Geographical and industry exposure8.Reporting abilities (generate and automated daily fund report)
8. Adding filters so that users of the application only see options they are interested in.

If you have ideas that you think will improve our application, please leave us a feature request and we will get to work on it after careful evaluation.