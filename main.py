from send_message import send_sms

from datetime import datetime, time
import time as t
import pytz

def is_market_open():
    local_tz = pytz.timezone("America/Vancouver")
    now = datetime.now(local_tz).time()
    
    market_open = time(6,30)
    market_close = time(13,0)

    return market_open <= now <= market_close

def is_final_alert():
    local_tz = pytz.timezone("America/Vancouver")
    now = datetime.now(local_tz).time()

    return time(13,0) <= now < time(13,1)

def run_script():
    while True:
        if is_market_open() or is_final_alert():
            print("Market is open, sending update")
            send_sms()
        else:
            print("Market is closed.")

        print("sleeping for an hour")
        t.sleep(3600)

run_script()

