import datetime
import time
import pytz
import schedule
from logic.main import run_market_check

LOCAL_TZ = pytz.timezone("America/Vancouver")

MARKET_OPEN = datetime.time(6, 30)
MARKET_CLOSE = datetime.time(13, 0)

def market_job():
    now = datetime.datetime.now(LOCAL_TZ)
    today = now.weekday()
    current_time = now.time()

    if today >= 5:
        print(f"Its currently the weekend, skipping jobs.")
    else:
        run_market_check(now)

schedule.every(1).hour.do(market_job)
schedule.every().day.at("13:00").do(market_job)

while True:
    schedule.run_pending()
    time.sleep(1)