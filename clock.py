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
    @sched.scheduled_job('cron', day_of_week='*', hour=13, minute=7)
    def test():
        print("STARTING TWEET")
        tweet()
        print("TWEETED")
else:
    # RUN IN PRODUCTION
    @sched.scheduled_job('cron', day_of_week='*', hour=8)
    def morning():
        tweet()

    @sched.scheduled_job('cron', day_of_week='*', hour=16)
    def afternoon():
        tweet()


sched.start()
