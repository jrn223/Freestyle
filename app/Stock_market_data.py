# for email functionality, credit @s2t2
import os
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

# for day of week
import datetime

# to query Google stock data
from pandas_datareader import data
from datetime import date, timedelta

#for sorting biggest gains to biggest losses
import operator

stock_data = []

#Stock data for Apple, Amazon, Activision Blizzard, Hologic Inc, Ligand Pharmaceuticals Inc, Microsoft, Ferrari, T. Rowe Price, Tesla, Vivint Solar Inc
symbols = ['AAPL', 'AMZN', 'ATVI', 'HOLX', 'LGND', 'MSFT', 'RACE', 'TROW', 'TSLA', 'VSLR']
data_source = 'google'

day_of_week = datetime.datetime.today().weekday()
# print(day_of_week) tested day of week functionality working

monday = [0]
other_weekdays = [1,2,3,4]

if day_of_week in monday:
    start = str(date.today() - timedelta(days=3))
    end = str(date.today())

elif day_of_week in other_weekdays:
    start = str(date.today() - timedelta(days=1))
    end = str(date.today())

response = data.DataReader(symbols, data_source, start, end)

daily_closing_prices = response.ix["Close"]

print(daily_closing_prices)

def stock_data_builder (ticker_symbol):
    stock = {}
    stock["ticker"] = ticker_symbol
    stock["today_close"] = daily_closing_prices.iloc[1][ticker_symbol]
    stock["previous_day_close"] = daily_closing_prices.iloc[0][ticker_symbol]
    stock["difference"] = stock["today_close"] - stock["previous_day_close"]
    stock_data.append(stock)

for ticker in symbols:
    stock_data_builder(ticker)

products_gain_loss_order = sorted(stock_data, key=lambda x: int(x["difference"]), reverse=True)

print(products_gain_loss_order)

# AUTHENTICATE

# SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
#
# sg = sendgrid.SendGridAPIClient(apikey = SENDGRID_API_KEY)
#
# # COMPILE REQUEST PARAMETERS
#
# subject = "Hello World from the SendGrid Python Library!"
# my_email = Email("jrn223@stern.nyu.edu")
# from_email = my_email
# to_email = my_email
# content = Content("text/plain", "Hello, Email!")
# mail = Mail(from_email, subject, to_email, content)
#
# # ISSUE REQUEST
#
# response = sg.client.mail.send.post(request_body=mail.get())
#
# # PARSE RESPONSE
#
# print(response.status_code)
# print(response.body)
# print(response.headers)
