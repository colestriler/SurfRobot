import os
from datetime import datetime
import calendar
from flaskapp.bots.collect_data import get_surf_data
import time
import secrets
from flaskapp import create_app, db
from flaskapp.models import Report
from flaskapp.bots.config_class import API
import tweepy

api_class = API()
api = api_class.create_api()
surf_data = get_surf_data()

locations = []
datas = []
for location, data in surf_data.items() :
    locations.append(location)
    datas.append(data)

length_locations = len(locations)



def tweet():
    # DELETE ALL PREVIOUS TWEETS IF USING TESTING ACOUNT
    # if api_class.delete_all:
    #     for status in tweepy.Cursor(api.user_timeline).items():
    #         api.destroy_status(status.id)

    today = datetime.today()
    dow = calendar.day_name[today.weekday()]
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    reports = []

    if today.hour <= 12:
        time = "Morning"
    else:
        time = "Afternoon"

    first_tweet = f"""🏄🏽‍♂️ {time} surf report for {dow} at {current_time}:
    """
    api.update_status(first_tweet)

    for i in range(length_locations):
        previous_tweet = api.user_timeline(id = api.me().id, count = 1)[0]
        if datas[i]['condition'] == "poor":
            cond_emoji = "❌"
        elif datas[i]['condition'] == "poor to fair":
            cond_emoji = "⚠️"
        else:
            cond_emoji = "✅"
        tweet = f"""{locations[i]} ({time}):

{cond_emoji}Condition: {datas[i]['condition']}
{"🌊"}Wave height: {datas[i]['wave_height']}
{"🌙"}Tide: {datas[i]['tide']}
{"💨"}Wind: {datas[i]['wind']}
{"🌡"}Water temp: {datas[i]['H20temp']}℉
{"🌞"}Outside Weather: {datas[i]['weather']}℉
{"🌅"}First Light: {datas[i]['first_light'].strftime("%H:%M")}
{"🌌"}Last Light: {datas[i]['last_light'].strftime("%H:%M")}
        """
        # {"🧭"}
        # Swells: {datas[i]['swells'][0]},
        # {datas[i]['swells'][1]}

        api.update_status(tweet, in_reply_to_status_id = previous_tweet.id)


        report = Report(
            date=now,
            location=locations[i],
            condition=datas[i]['condition'],
            wave_height=datas[i]['wave_height'],
            tide=datas[i]['tide'],
            wind=datas[i]['wind'],
            # swells = db.Column(db.String(), nullable=True),
            weather=datas[i]['weather'],
            h20_temp=datas[i]['H20temp']
        )
        reports.append(report)

    # Adding To Database
    app = create_app()
    with app.app_context():
    # ctx.push()
        for report in reports:
            db.session.add(report)
            db.session.commit()
    # ctx.pop()





