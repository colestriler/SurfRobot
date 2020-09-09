import os
from apscheduler.schedulers.blocking import BlockingScheduler
from flaskapp.bots.create_tweet import tweet



sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=.5)
# def timed_job():
#     print('This job is run every three minutes.')
#     api.update_status("hello")


if os.getenv("DEVELOPMENT") == "True":
    # RUN IN DEVELOPMENT
    print("BEFORE TWEET")
    @sched.scheduled_job('cron', day_of_week='*', hour=16, minute=21)
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
