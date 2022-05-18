"""Helper functions for inventory app for a logistic company."""

import requests
import os

from datetime import datetime

#Open weather updates every hour
#Store weather data by city to save on API calls

weather_cache = {}

def is_float(input_string):
    """Check if an input string is a float"""
    try:
        float(input_string)
        return True
    except ValueError:
        return False

def validate_create_item_input(sku, name, quantity, unit, unit_cost, warehouse):
    """Form input fields error handling"""
    # Check if fields are empty
    # Check if SKU is digit
    # Check if quantity is digit
    # Check if unit cost is is float

    if  sku == "" or \
        name == "" or \
        quantity == "" or \
        unit == "" or \
        unit_cost == "" or \
        warehouse == "" or \
        not sku.isdigit() or \
        not quantity.isdigit() or \
        not is_float(unit_cost):
            return False
    else:
        return True

def validate_add_warehouse_input(city_name, city_code):
    """Form input fields error handling"""
    # Check if fields are empty
    # Check if city_code consists of 3 alphabetical characters

    if  city_name == "" or \
        city_code == "" or \
        len(city_code) != 3:
            return False
    else:
        return True

def get_city_geocode(city_name):
    """Given a US city name.
        Make an API call to Open Weather.
        Obtain geocodes for city.
        Return a coordinates dictionary with latitutde(lat) and longitude(lon)."""

    q = f"{city_name},US"
    api_key = os.environ["OPEN_WEATHER_KEY"]

    resp = requests.get("http://api.openweathermap.org/geo/1.0/direct",
    params={"q": q, "limit":1, "appid":api_key})

    data = resp.json()
    coordinates = {}
    coordinates['lon'] = data[0]['lon']
    coordinates['lat'] = data[0]['lat']

    return coordinates


def get_current_weather(warehouse):
    """Given an warehouse object.
    Make an API call to Open Weather to obtain current weather.
    Parse data and return a weather dictionary with temp and description. 
    """

    lat = warehouse.lat
    lon = warehouse.lon
    api_key = os.environ["OPEN_WEATHER_KEY"]

    resp = requests.get("https://api.openweathermap.org/data/2.5/weather",
                        params={"lat": lat, "lon":lon, "units":"imperial", "appid":api_key})

    data = resp.json()

    description = data['weather'][0]['description']
    temp = int(data['main']['temp'])

    weather = {'description':description, 'temp':temp}

    return weather
            
def get_weather_info(warehouse):
    """Check if up-to-date weather info exits in weather cache.
        If so, return.
        If not, make API call to update info."""  

    #Get current time
    current_time = datetime.now()

    #Check if weather cache exists
    if weather_cache.get(warehouse.warehouse_id):
        diff = current_time - weather_cache[warehouse.warehouse_id]['timestamp']
        if diff.total_seconds() < 3600: #Open weather updates weather info every hour (3600seconds)
            return weather_cache[warehouse.warehouse_id]
        else:
            weather = get_current_weather(warehouse) #Make API request for updated weather info
            weather['timestamp'] = current_time
            weather_cache[warehouse.warehouse_id] = weather #set weather_cache
            return weather_cache[warehouse.warehouse_id]
    else:
        weather = get_current_weather(warehouse) #Make API request for updated weather info
        weather['timestamp'] = current_time
        weather_cache[warehouse.warehouse_id] = weather #set weather_cache
        return weather_cache[warehouse.warehouse_id]
