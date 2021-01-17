import discord
import yfinance as yf
import datetime
import sys
import yahoo_fin.stock_info as si
from yahoo_fin import options 
from discord.ext import commands
import urllib.request
from googlesearch import search
import pandas as pd
import pytz
import dateutil.relativedelta


client = commands.Bot(command_prefix = "$")

global userinput

@client.event
async def on_ready():
    print('Bot is ready')

#Will return the live stock price for a users given input
@client.command( description = "Type $Price (ticker) to get the price of a stock", pass_context = True, aliases=['PRICE','price','PRice','PRIce'])
async def Price (ctx, userinput):
    userinput
    #Checks to see if the users ticker is on the NASDAQ
    try:
        tickers = si.get_live_price(userinput)
       # query = "yahoo Finance" + userinput
        #for i in search(query, tld="co.in", num=1, stop=1, pause=2):
          #  print(i) 
       # await ctx.send (f'The live price of {userinput} is ${round(tickers, 2)} per share {i}')
        await ctx.send (f'The live price of {userinput.upper()} is ${round(tickers, 5)} per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')
    except (AssertionError, KeyError):
        await ctx.send(f"Sorry that ticker {userinput.upper()} does not exist. This bot is only made for tickers on the nasdaq")

#the command to show the one day change in a stock price
@client.command( description = "Type $DiffD (Ticker) to get the dollar and percentage change of a stock for one day", pass_context = True, aliases=['diffd','Diffd','DiFFD', 'DIFFD', 'DIffd', 'DIFfd'])
async def DiffD(ctx,userinput):
    userinput
    try:
        userinput 
        time = datetime.datetime.now()
        negDay = datetime.timedelta(days=1)
        Yesterday = time - negDay
        
        
        #For if the command is ran on the weekend or a US holiday
        if time.weekday() == 6 or time.weekday() == 5:
            negDaySaturday = datetime.timedelta(days=2)
            YesterdaySaturday = time - negDaySaturday
        
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            YesterdayPrice = si.get_data(userinput, start_date=YesterdaySaturday, end_date=YesterdaySaturday)

            #ollecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfYesterdayPrice = pd.DataFrame(YesterdayPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalYesterdayPrice = dfYesterdayPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalYesterdayPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalYesterdayPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} in one day is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}') 
            
        
        #After Hours Monday
        elif Yesterday.weekday() == 6:
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            YesterdayPrice = si.get_data(userinput, start_date=Yesterday, end_date=Yesterday)

            #ollecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfYesterdayPrice = pd.DataFrame(YesterdayPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalYesterdayPrice = dfYesterdayPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalYesterdayPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalYesterdayPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} in one day is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')        
    
        else:
            
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            YesterdayPrice = si.get_data(userinput, start_date=Yesterday, end_date=Yesterday)

            #ollecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfYesterdayPrice = pd.DataFrame(YesterdayPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalYesterdayPrice = dfYesterdayPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalYesterdayPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalYesterdayPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} in one day is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')
        
    except (AssertionError, KeyError):
        await ctx.send(f"Sorry that ticker {userinput.upper()} does not exist. This bot is only made for tickers on the nasdaq")

    
    
    
@client.command(description ="Type $Diffw (Ticker) to get the dollar and percentage change of a stock for one week", pass_context = True, aliases=['diffw','DiffW','DiFFW', 'DIFFW', 'DIffw', 'DIFfw'])
async def Diffw(ctx, userinput):
    userinput
    try:
        userinput 
        time = datetime.datetime.now()
        negDay = datetime.timedelta(days=7)
        pastWeek = time - negDay
        
        #For if the command is ran on the weekend or a US holiday
        if time.weekday() == 6 or time.weekday() == 5:
            negDaySaturday = datetime.timedelta(days=8)
            YesterdaySaturday = time - negDaySaturday
        
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            YesterdayPrice = si.get_data(userinput, start_date=YesterdaySaturday, end_date=YesterdaySaturday)
            print(dayPrice)
            print(YesterdayPrice)

            #ollecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfYesterdayPrice = pd.DataFrame(YesterdayPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalYesterdayPrice = dfYesterdayPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalYesterdayPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalYesterdayPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} in one week is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}') 
            
        
        #After Hours Monday
        elif pastWeek.weekday() == 6:
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            pastWeekPrice = si.get_data(userinput, start_date=pastWeek, end_date=pastWeek)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfpastWeekPrice = pd.DataFrame(pastWeekPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastWeekPrice = dfpastWeekPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastWeekPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastWeekPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one week is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')        
    
        else:
            
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            pastWeekPrice = si.get_data(userinput, start_date=pastWeek, end_date=pastWeek)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfPastWeekPrice = pd.DataFrame(pastWeekPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastWeekPrice = dfPastWeekPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastWeekPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastWeekPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one week is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')
        
    except (AssertionError, KeyError):
        await ctx.send(f"Sorry that ticker {userinput.upper()} does not exist. This bot is only made for tickers on the nasdaq")



@client.command(description ="Type $Diffw (Ticker) to get the dollar and percentage change of a stock for one month", pass_context = True, aliases=['diffm','DiffM','DiFFM, DIFFM, DIffm', 'DIffm'])
async def Diffm(ctx, userinput):
    userinput
    try:
        userinput 
        time = datetime.datetime.now()
        pastMonth = time - dateutil.relativedelta.relativedelta(months=1)

      #For if the command is ran on the weekend or a US holiday
        if time.weekday() == 6 or time.weekday() == 5:
           #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            pastMonthPrice = si.get_data(userinput, start_date=pastMonth, end_date=pastMonth)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfPastMonthPrice = pd.DataFrame(pastMonthPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastMonthPrice = dfPastMonthPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastMonthPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastMonthPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one month is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')        
        
        #After Hours Monday
        elif pastMonth.weekday() == 6:
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            pastMonthPrice = si.get_data(userinput, start_date=pastMonth, end_date=pastMonth)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfPastMonthPrice = pd.DataFrame(pastMonthPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastMonthPrice = dfPastMonthPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastMonthPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastMonthPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one month is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')        
    
        else:
            
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            pastMonthPrice = si.get_data(userinput, start_date=pastMonth, end_date=pastMonth)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfPastMonthPrice = pd.DataFrame(pastMonthPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastMonthPrice = dfPastMonthPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastMonthPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastMonthPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one month is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')
        
    except (AssertionError, KeyError):
        await ctx.send(f"Sorry that ticker {userinput.upper()} does not exist. This bot is only made for tickers on the nasdaq")
    
        
@client.command(description ="Type $Diffy (Ticker) to get the dollar and percentage change of a stock for year month", pass_context = True, aliases=['diffy','DiffY','DiFFY, DIFFY, DIffy', 'DIffy'])
async def Diffy(ctx, userinput):
    userinput
    try:
        userinput 
        time = datetime.datetime.now()
        negDay = datetime.timedelta(days=365)
        pastYear = time - negDay

      #For if the command is ran on the weekend or a US holiday
        if time.weekday() == 6 or time.weekday() == 5:
           #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            pastYearPrice = si.get_data(userinput, start_date=pastYear, end_date=pastYear)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfPastYearPrice = pd.DataFrame(pastYearPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastYearPrice = dfPastYearPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastYearPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastYearPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one year is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')        
        
        #After Hours Monday
        elif pastYear.weekday() == 6:
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            PastYearPrice = si.get_data(userinput, start_date=pastYear, end_date=pastYear)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfPastYearPrice = pd.DataFrame(pastYearPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastYearPrice = dfPastYearPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastYearPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastYearPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one year is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')        
    
        else:
            
            #Getting price 
            dayPrice = si.get_data(userinput, start_date=time, end_date=time)
            PastYearPrice = si.get_data(userinput, start_date=pastYear, end_date=pastYear)
            #collecting the data Frame
            dfDayPrice = pd.DataFrame(dayPrice)
            dfPastYearPrice = pd.DataFrame(PastYearPrice)
            #Getting the prices
            finalDayPrice = dfDayPrice.close[0]
            finalPastYearPrice = dfPastYearPrice.close[0]
            #Finding the change in price
            change = ((finalDayPrice - finalPastYearPrice) / finalDayPrice) *100
            priceChange = finalDayPrice - finalPastYearPrice
            #Printing the change
            await ctx.send (f'The change in {userinput.upper()} for one year is roughly {round(change, 2)}% or ${round(priceChange, 4)}  per share https://ca.finance.yahoo.com/quote/{userinput}?p={userinput}')
        
    except (AssertionError, KeyError):
        await ctx.send(f"Sorry that ticker {userinput.upper()} does not exist. This bot is only made for tickers on the nasdaq")
           
    
    
        
client.run("NzMxNjYwMjA5ODM1MjEyODgw.XwpRqw.gqp10Uqw-zkYmfLnHCZpCdtFF9g")
