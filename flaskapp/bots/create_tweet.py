from datetime import datetime
import calendar
from os import environ
from flaskapp.bots.collect_data import get_surf_data
from flaskapp.bots.config import create_api

api = create_api()
surf_data = get_surf_data()

locations = []
datas = []
for location, data in surf_data.items() :
    locations.append(location)
    datas.append(data)

def tweet():
    today = datetime.today()
    dow = calendar.day_name[today.weekday()]
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    #{today.month}/{today.day}/{today.year}

    first_tweet = f"""🏄🏽‍♂️ Surf report for {dow} at {current_time}:
    """

    api.update_status(first_tweet)

    for i in range(len(locations)):

        previous_tweet = api.user_timeline(id = api.me().id, count = 1)[0]

        tweet = f"""{locations[i]}:

Condition: {datas[i]['condition']}
Wave height: {datas[i]['wave_height']}
Tide: {datas[i]['tide']}
Wind: {datas[i]['wind']}
Swells: {datas[i]['swells'][0]},
        {datas[i]['swells'][1]}
Water temp: {datas[i]['H20temp']}℉
Outside Weather: {datas[i]['weather']}℉
        """

        api.update_status(tweet, in_reply_to_status_id=previous_tweet.id)