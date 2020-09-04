from apscheduler.schedulers.blocking import BlockingScheduler
from flaskapp.bots.create_tweet import tweet



sched = BlockingScheduler()

# @sched.scheduled_job('interval', minutes=.5)
# def timed_job():
#     print('This job is run every three minutes.')
#     api.update_status("hello")


@sched.scheduled_job('cron', day_of_week='mon-fri', hour=13, minute=47)
def test():
    tweet()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=6)
def morning():
    tweet()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=16)
def afternoon():
    tweet()


sched.start()