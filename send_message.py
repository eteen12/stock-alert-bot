import smtplib
from stock_prices import get_stock_info, format_stock_info
import os
from dotenv import load_dotenv

load_dotenv()

FROM = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")
TO = os.getenv("TO_PHONE")

def send_sms():

    message = f"""\
    From: {FROM}
    To: {TO}
    Subject: Stock Alert

    {format_stock_info()}
    """
    

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(FROM, PASSWORD)
            response = server.sendmail(FROM, TO, message)
            if not response:
                print("✅ SMS sent successfully!")
            else:
                print("❌ Failed to send SMS:", response)
    except Exception as e:
        print("❌ Error occurred while sending SMS:", str(e))

