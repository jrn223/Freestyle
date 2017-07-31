import os
import sendgrid
from sendgrid.helpers.mail import * # source of Email, Content, Mail, etc.

from pandas_datareader import data
from datetime import date, timedelta

#Stock data for Apple, Amazon, Activision Blizzard, Hologic Inc, Ligand Pharmaceuticals Inc, Microsoft, Ferrari, T. Rowe Price, Tesla, Vivint Solar Inc

symbols = ['AAPL', 'AMZN', 'ATVI', 'HOLX', 'LGND', 'MSFT', 'RACE', 'TROW', 'TSLA', 'VSLR']
data_source = 'google'
start = str(date.today() - timedelta(days=2))
end = str(date.today())

response = data.DataReader(symbols, data_source, start, end)

daily_closing_prices = response.ix["Close"]

print(daily_closing_prices)

# AUTHENTICATE

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

sg = sendgrid.SendGridAPIClient(apikey = SENDGRID_API_KEY)

# COMPILE REQUEST PARAMETERS

subject = "Hello World from the SendGrid Python Library!"
my_email = Email("jrn223@stern.nyu.edu")
from_email = my_email
to_email = my_email
content = Content("text/plain", "Hello, Email!")
mail = Mail(from_email, subject, to_email, content)

# ISSUE REQUEST

response = sg.client.mail.send.post(request_body=mail.get())

# PARSE RESPONSE

print(response.status_code)
print(response.body)
print(response.headers)
