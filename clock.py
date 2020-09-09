import os
from apscheduler.schedulers.blocking import BlockingScheduler
from flaskapp.bots.create_tweet import tweet
import datetime

#Temporary (Set to False to post on main (non-test) account)
DEV=True

sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=.5)
# def timed_job():
#     print('This job is run every three minutes.')
#     api.update_status("hello")

if os.getenv("DEVELOPMENT") == "True":

    # RUN IN DEVELOPMENT
    print("BEFORE TWEET")

    time = datetime.datetime.now()
    @sched.scheduled_job('cron', day_of_week='*',
                         hour=time.hour,
                         minute=time.minute if time.second <= 50 else time.minute + 1
                         )
    def test():
        print("STARTING TWEET")
        tweet(time="Afternoon")
        print("TWEETED")
else:
    # RUN IN PRODUCTION
    @sched.scheduled_job('cron', day_of_week='*', hour=8)
    def morning():
        tweet(time="Morning")

    @sched.scheduled_job('cron', day_of_week='*', hour=16)
    def afternoon():
        tweet(time="Afternoon")


sched.start()
