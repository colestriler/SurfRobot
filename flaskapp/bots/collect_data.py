import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np
import re
import datetime
import requests


tmp_url = "https://www.surfline.com/surf-report/terra-mar-point/5842041f4e65fad6a77088a6"
tamarack = 'https://www.surfline.com/surf-report/tamarack/5842041f4e65fad6a7708837'
oside_pier_south_url = "https://www.surfline.com/surf-report/oceanside-pier-southside/584204204e65fad6a7709435"
oside_pier_north_url = "https://www.surfline.com/surf-report/oceanside-pier-northside/5842041f4e65fad6a7708835"
oside_harbor_north_url = "https://www.surfline.com/surf-report/oceanside-harbor-north-jetty/5842041f4e65fad6a7708832"
grandview_url = "https://www.surfline.com/surf-report/grandview/5842041f4e65fad6a770889f"
seaside_reef_url = "https://www.surfline.com/surf-report/seaside-reef/5842041f4e65fad6a77088b3"
d_street_url = "https://www.surfline.com/surf-report/d-street/5842041f4e65fad6a77088b7"
la_jolla_url = "https://www.surfline.com/surf-report/la-jolla-shores/5842041f4e65fad6a77088cc"
swamis_url = "https://www.surfline.com/surf-report/swami-s/5842041f4e65fad6a77088b4"
pacific_beach = 'https://www.surfline.com/surf-report/pacific-beach/5842041f4e65fad6a7708841'
beacons='https://www.surfline.com/surf-report/beacons/5842041f4e65fad6a77088a0'
moonlight='https://www.surfline.com/surf-report/moonlight-state-beach/5842041f4e65fad6a77088a3'
pipes = 'https://www.surfline.com/surf-report/pipes/5c008f5313603c0001df5318'
blacks='https://www.surfline.com/surf-report/blacks/5842041f4e65fad6a770883b'
windansea='https://www.surfline.com/surf-report/windansea/5842041f4e65fad6a770883c'
la_jolla_shores='https://www.surfline.com/surf-report/la-jolla-shores/5842041f4e65fad6a77088cc'
tourmaline='https://www.surfline.com/surf-report/old-man-s-at-tourmaline/5842041f4e65fad6a77088c4'
torrey_pines='https://www.surfline.com/surf-report/torrey-pines-state-beach/584204204e65fad6a7709994'
del_mar='https://www.surfline.com/surf-report/del-mar/5d7687fdb4c559000112e666'
san_elijo='https://www.surfline.com/surf-report/san-elijo-state-beach/5842041f4e65fad6a77088b8'


urls = [
    beacons,
    blacks,
    d_street_url,
    del_mar,
    grandview_url,
    la_jolla_url,
    moonlight,
    oside_harbor_north_url,
    oside_pier_north_url,
    oside_pier_south_url,
    pacific_beach,
    pipes,
    san_elijo,
    seaside_reef_url,
    swamis_url,
    tamarack,
    tmp_url,
    torrey_pines,
    tourmaline,
    windansea
]


def get_surf_data():

    dictionary = {}

    for url in urls:

        data = {}

        url_page = requests.get(url)
        url_soup = soup(url_page.text, "html.parser")

        url_loc = url_soup.h1.text.replace(" Report & Forecast", "")

        # current conditions (i.e. top table on website)
        current_cond = url_soup.find("div", {"class": "quiver-spot-report"})
        url_cond = current_cond.div.text.lower()
        data['condition'] = url_cond

        # takes current wave height
        current_height = url_soup.find("span", {"class": "quiver-surf-height"})
        url_height = current_height.text.lower()
        data['wave_height'] = url_height

        # takes current tide
        current_tide = url_soup.find("div", {
            "class": "quiver-spot-forecast-summary__stat-container quiver-spot-forecast-summary__stat-container--tide"})
        url_tide = current_tide.next_element.next_element.next_element.text
        data['tide'] = url_tide

        # takes wind speed
        current_wind = url_soup.find("div", {
            "class": "quiver-spot-forecast-summary__stat-container quiver-spot-forecast-summary__stat-container--wind"})
        url_wind = current_wind.next_element.next_element.next_element.text
        data['wind'] = url_wind

        # # swells
        # data['swells'] = [swells_line_1, swells_line_2, swells_line_3]

        # outside temp
        current_weather = url_soup.find("div", {"class": "quiver-weather-stats"})
        url_weather = current_weather.next_element.next_element.next_element.next_element.next_element
        data['weather'] = url_weather

        # water temp
        current_H20temp = url_soup.find("div", {"class": "quiver-water-temp"})
        H20temp1 = current_H20temp.next_element.next_element.next_element.next_element.next_element
        H20temp2 = current_H20temp.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        data['H20temp'] = H20temp1 + "-" + H20temp2

        # ----------------- API --------------------

        # WEATHER DATA
        spot_id = url.split('/')[-1]
        api_url = 'https://services.surfline.com/kbyg/spots/forecasts/weather?spotId={}&days=6&intervalHours=1'.format(spot_id)
        api_data = requests.get(api_url).json()

        # first light
        first_light_timestamp = api_data['data']['sunlightTimes'][0]['dawn']
        first_light = datetime.datetime.fromtimestamp(first_light_timestamp)
        data['first_light'] = first_light

        # last light
        last_light_timestamp = api_data['data']['sunlightTimes'][0]['dusk']
        last_light = datetime.datetime.fromtimestamp(last_light_timestamp)
        data['last_light'] = last_light





        dictionary[url_loc] = data

    return dictionary



