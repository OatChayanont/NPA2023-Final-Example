import requests
import json
import time

openweatherGeoAPIGetParameters = {
            "q": "London",
            "limit": 1,
            "appid": "48af826e7c925d11f2acc314068861de",
        }

#######################################################################################       
# 6. Provide the URL to the OpenWeather Geocoding address API.
        # Get location information using the OpenWeather Geocoding API geocode service using the HTTP GET method
r = requests.get("http://api.openweathermap.org/geo/1.0/", 
                             params = openweatherGeoAPIGetParameters
                        )
        # Verify if the returned JSON data from the OpenWeather Geocoding API service are OK
json_data = r.json()
        # check if the status key in the returned JSON data is "0"
if not r.status_code == 200:
    raise Exception("Incorrect reply from OpenWeather Geocoding API. Status code: {}".format(r.statuscode))
print(json_data)