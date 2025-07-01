# Stock Alert Bot
#### COMPLETELY FREE NO PAID 3rd PARTIES

A Python script that sends you hourly SMS updates (offline with your own server, instructions coming soon) with the latest stock prices during market hours, plus a final alert after market close.
Made to run 24/7 and notify you via SMS using Gmail’s SMTP and your carrier’s SMS gateway. 

## Features

- Fetches real time stock data using yfinance
- Sends SMS alerts via Gmail SMTP and your phone's SMS gateway so you can get updates with no wifi

## Req's

- yfinance
- pytz
- python-dotenv

## Setup

1. Clone the repo
2. Create and activate a virtual environment
   - `python3 -m venv venv`
   - `source venv/bin/activate  # Linux/macOS`
3. Install deps
   - `pip install -r requirements.txt`
4. Create a .env file in the root folder with the following vars
   - `EMAIL=your@email.com`
   - `EMAIL_PASSWORD=your_gmail_app_password`
   - `TO_PHONE=your_number_sms_gateway`
  
   - To generate an app password for Gmail, see <a href="https://support.google.com/accounts/answer/185833" >Googles guide</a>
   - The phone number should be in format 17785551234@msg.carrier.com
   - I use koodo so it goes to @msg.telus.com

## Usage

run the script to start sending alerts: `python main.py`

## Notes

For what ever reason, SMTP does not like tickers with a "." example BAM.TO has,
to be changed to BAMTO. SMS delivery depends on your carrier's SMS gateway and probaly 
has limitations on message delivery ect.
