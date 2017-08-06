# Freestyle project
For jrn223 Freestyle project

# Prerequisites
Follow the Setup Guide (https://github.com/s2t2/example-email-app-py/blob/master/SETUP.md) to obtain and configure credentials for using the SendGrid service to send email. And for configuring a machine to run this application.

# Installation

Install Python 3

Download the source code:

```shell
git clone https://github.com/jrn223/Freestyle.git
cd Freestlye/app/
```

#### Install package dependencies
pip install -r requirements.txt

##### Usage
python Stock_market_data.py

###### Deploying
Run the application on a Heroku server created during the setup process. 

###### Notes

The daily email is scheduled to be sent at 4:30 pm every day. You can also run the app in your command line, but it will only work after the market closes at 4 pm. It does however take into account the fact that the market is closed on the weekends.

For an example of the email that is sent, see the Stock Market Updates! file in the artifcats folder.
