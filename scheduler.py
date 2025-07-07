from freezegun import freeze_time
from schedule import every, repeat, run_pending
import schedule
import datetime
import schedule
import time
from logic.main import run_script, is_market_open

# @repeat(every(1).second)
@freeze_time("2025-07-07 13:00:00")
def test_at_close():
    schedule.every().day.at("13:00").do(run_script)
    schedule.run_pending()

@freeze_time("2025-07-06 13:00:00")
def test_on_weekend():
    print(is_market_open())

test_at_close()

# schedule.every().day.at("13:00").do(run_script)
while True:
    run_pending()
    time.sleep(1)