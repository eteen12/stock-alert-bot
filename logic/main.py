from logic.send_message import send_sms
import datetime
import pytz

MARKET_OPEN = datetime.time(6, 30)
MARKET_CLOSE = datetime.time(13, 0)
LOCAL_TZ = pytz.timezone("America/Vancouver")

def is_market_open(now_dt=None):
    if now_dt is None:
        now = datetime.datetime.now(LOCAL_TZ).time()
        today = datetime.datetime.now(LOCAL_TZ).weekday()

    now = now_dt.time()
    today = now_dt.weekday()
    
    if today < 5:
         return MARKET_OPEN <= now <= MARKET_CLOSE
    else:
         return False

def run_market_check(now_dt=None):
        if is_market_open(now_dt):
            print("Market is open, sending update")
            send_sms()
        else:
            print("Market is closed \n")



