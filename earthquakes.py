
import requests
import json
import numpy as np

def get_data():
    response = requests.get(
        "http://earthquake.usgs.gov/fdsnws/event/1/query.geojson",
    params ={
            'starttime': "2000-01-01",
            "maxlatitude": "58.723",
            "minlatitude": "50.008",
            "maxlongitude": "1.67",
            "minlongitude": "-9.756",
            "minmagnitude": "1",
            "endtime": "2025-10-11",
            "orderby": "time-asc"}
    )
    text = response.text
    return json.loads(text)

def count_earthquakes(data):
    # The number of earthquakes is the number of features in the GeoJSON
    return len(data["features"])


def get_magnitude(data):
  magnitudes = [feature['properties']['mag'] for feature in data['features']]
  return magnitudes

def get_location(data):
    # Return a list of all locations
    locations = [feature['properties']['place'] for feature in data['features']]
    return locations


def get_maximum(earthquake):
    mag_max = 0
    for feature in earthquake['features']:
        mag = feature['properties']['mag']
        if mag > mag_max:
            mag_max = mag
            location = feature['properties']['place']
            
    return mag_max, location



earthquake = get_data()

print(count_earthquakes(earthquake))
print(get_magnitude(earthquake))
print(get_location(earthquake))
print(get_maximum(earthquake))