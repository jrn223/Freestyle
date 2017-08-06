# System Objectives
For 10 specified stocks, the system will pull daily prices and the change from the previous day’s close. It will sort the list by the biggest gains to the biggest losses, and email the list to me every day day after the market closes.  

## Information Inputs
Information inputs include:
•	Stock tickers
•	An HTTP response from the Google Finance API containing stock data
•	My email address
•	Email subject line 
•	An HTTP response from the SendGrid API confirming the action has been performed.

## Information Outputs
A daily email showing the stocks’ current price and change from the previous day’s close, sorted by the change from the previous day from biggest gains to biggest losses. 

### Notes
The daily email is scheduled to be sent at 4:30 pm every day. You can also run the app in your command line, but it will only work after the market closes at 4 pm. It does however take into account the fact that the market is closed on the weekends. 

For an example of the email that is sent, see the Stock Market Updates! file in the artifcats folder. 
