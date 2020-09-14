import os
from apscheduler.schedulers.blocking import BlockingScheduler
from flaskapp.bots.create_tweet import tweet
from flaskapp.bots.follow_users import follow
import datetime


sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=.5)
# def timed_job():
#     print('This job is run every three minutes.')
#     api.update_status("hello")

# -------------------------------------------------------------------------

if os.getenv("DEVELOPMENT") == "True":

    # # RUN IN DEVELOPMENT
    print("BEFORE TWEET")

    time = datetime.datetime.now()
    @sched.scheduled_job('cron', day_of_week='*',
                         hour=time.hour,
                         minute=time.minute,
                         second=time.second + 12
                         )
    def test():
        print("STARTING TWEET")
        tweet()

        print("TWEETED")

# --------------------------------------------------------------------------
# RUN IN DEVELOPMENT
#     print("BEFORE FOLLOWING")
#
#     time = datetime.datetime.now()
#     @sched.scheduled_job('cron', day_of_week='*',
#                          hour=time.hour,
#                          minute=time.minute,
#                          second=time.second + 12
#                          )
#     def test():
#         print("START FOLLOWING")
#         follow()
#         print("FOLLOWED")


#-------------------------------------------------------------------------------
else:
    # RUN IN PRODUCTION
    @sched.scheduled_job('cron', day_of_week='*', hour=9)
    def morning():
        tweet()
        follow()

    @sched.scheduled_job('cron', day_of_week='*', hour=17, minute=1)
    def afternoon():
        tweet()



sched.start()
