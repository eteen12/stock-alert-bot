from send_message import send_sms
from datetime import datetime, time as dt_time
import time
import pytz

local_tz = pytz.timezone("America/Vancouver")

def is_market_open(now):
    market_open = dt_time(6, 30)
    market_close = dt_time(13, 0)
    return market_open <= now.time() < market_close

def is_final_alert(now):
    return now.time() == dt_time(13, 0)

def run_script():
    while True:
        now = datetime.now(local_tz)

        if is_market_open(now) or is_final_alert(now):
            print(f"Market is open, sending update")
            send_sms()
        else:
            print(f"Market is closed. Waiting...")
        
        time.sleep(3600)

run_script()