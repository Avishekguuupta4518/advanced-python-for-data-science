import schedule
import time
from datetime import datetime

def write_file():
    with open("schedule.txt", "w") as f:
        f.write(f"Hello! The time is {datetime.now()}")
        
schedule.every(1).minutes.do(write_file)

while True:
    schedule.run_pending()
    time.sleep(1)