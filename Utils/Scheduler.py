import schedule
import time
import Bots.mainBot as main

def job():
    main.runBot()

#schedule.every().wednesday.at("17:12").do(job)
schedule.every().tuesday.at("00:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
