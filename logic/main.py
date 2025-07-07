from logic.send_message import send_sms

import datetime
import time
import pytz

MARKET_OPEN = datetime.time(6, 30)
MARKET_CLOSE = datetime.time(13, 0)
LOCAL_TZ = pytz.timezone("America/Vancouver")


def is_market_open():
    now = datetime.datetime.now(LOCAL_TZ).time()
    today = datetime.datetime.now(LOCAL_TZ).weekday()
    if today < 5:
         return MARKET_OPEN <= now <= MARKET_CLOSE
    else:
         return False

def run_script():
        if is_market_open():
            print("Market is open, sending update")
            # send_sms()
        else:
            print("Market is closed")



