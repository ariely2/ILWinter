from bs4 import BeautifulSoup
from bs4 import NavigableString
from requests import get
from math import cos
from math import asin
from math import sqrt
import datetime
import json

def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    hav = 0.5 - cos((lat2-lat1)*p)/2 + cos(lat1*p)*cos(lat2*p) * (1-cos((lon2-lon1)*p)) / 2
    return 12742 * asin(sqrt(hav))

def check_winter(a, b):
    send_url = "http://ip-api.com/json"
    geo_req = get(send_url)
    geo_json = json.loads(geo_req.text)
    lat = float(geo_json['lat'])
    lon = float(geo_json['lon'])

    with open(b) as file:
        lines = file.readlines()

    index = min(range(len(lines)), key=lambda c: distance(lat,lon,float(lines[c].split()[0]),float(lines[c].split()[1])))

    with open(a) as file:
        cities = file.readlines()
        cities = [city.rstrip() for city in cities]
    city = cities[index]
    #print("location: " + city)

    url = "https://ims.gov.il/sites/default/files/ims_data/xml_files/isr_cities_1week_6hr_forecast.xml"

    r = get(url)
    soup = BeautifulSoup(r.content, "xml")
    for location in soup.find_all('Location'):
        if location.LocationMetaData.LocationNameEng.text == city:
            print("found!")
            for day in location.LocationData:
                if isinstance(day, NavigableString):
                    continue
                if 1150 >= int(day.WeatherCode.text) >= 1020:
                    date = day.ForecastTime.text.split()[0].split('-')
                    return("Winter weather on " + datetime.date(int(date[0]), int(date[1]), int(date[2])).strftime('%A') + "!")
            return 0