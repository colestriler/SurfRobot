import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np
import re
import requests

tmp_url = "https://www.surfline.com/surf-report/terra-mar-point/5842041f4e65fad6a77088a6"
tamarack = 'https://www.surfline.com/surf-report/tamarack/5842041f4e65fad6a7708837'
oside_pier_south_url = "https://www.surfline.com/surf-report/oceanside-pier-southside/584204204e65fad6a7709435"
oside_pier_north_url = "https://www.surfline.com/surf-report/oceanside-pier-northside/5842041f4e65fad6a7708835"
oside_harbor_url = "https://www.surfline.com/surf-report/oceanside-harbor-north-jetty/5842041f4e65fad6a7708832"
grandview_url = "https://www.surfline.com/surf-report/grandview/5842041f4e65fad6a770889f"
seaside_reef_url = "https://www.surfline.com/surf-report/seaside-reef/5842041f4e65fad6a77088b3"
d_street_url = "https://www.surfline.com/surf-report/d-street/5842041f4e65fad6a77088b7"
la_jolla_url = "https://www.surfline.com/surf-report/la-jolla-shores/5842041f4e65fad6a77088cc"
swamis_url = "https://www.surfline.com/surf-report/swami-s/5842041f4e65fad6a77088b4"
pacific_beach = 'https://www.surfline.com/surf-report/pacific-beach/5842041f4e65fad6a7708841'

urls = [tmp_url, oside_harbor_url, oside_pier_north_url, oside_pier_south_url, tamarack, swamis_url, grandview_url, d_street_url,
        seaside_reef_url, la_jolla_url, pacific_beach]


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

        # swells
        swells = url_soup.find("div", {
            "class": "quiver-spot-forecast-summary__stat-container quiver-spot-forecast-summary__stat-container--swells"})
        swells_line_1 = ""
        swells_line_2 = ""
        swells_line_3 = ""
        swells_line_1 += swells.next_element.next_element.next_element.next_element.next_element
        swells_line_1 += swells.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_1 += swells.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_1 += swells.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_1 += " " + swells.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_1 += swells.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells2 = swells.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_2 += swells2.next_element.next_element.next_element.next_element
        swells_line_2 += swells2.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_2 += swells2.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_2 += swells2.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_2 += " " + swells2.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_2 += swells2.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_3 = swells2.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_3 += swells_3.next_element.next_element.next_element
        swells_line_3 += swells_3.next_element.next_element.next_element.next_element.next_element
        swells_line_3 += swells_3.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_3 += swells_3.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_3 += " " + swells_3.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        swells_line_3 += swells_3.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        url_swells = swells_3.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        data['swells'] = [swells_line_1, swells_line_2, swells_line_3]

        # outside temp
        current_weather = url_soup.find("div", {"class": "quiver-weather-stats"})
        url_weather = current_weather.next_element.next_element.next_element.next_element.next_element
        data['weather'] = url_weather

        # water temp
        current_H20temp = url_soup.find("div", {"class": "quiver-water-temp"})
        H20temp1 = current_H20temp.next_element.next_element.next_element.next_element.next_element
        H20temp2 = current_H20temp.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element
        data['H20temp'] = H20temp1 + "-" + H20temp2

        dictionary[url_loc] = data

    return dictionary



