'''


'''
import requests
from dotenv import load_dotenv
load_dotenv() # Load environment variables from local .env file
import os
import datetime
import pandas as pd
def geocode_locator(api_key:str, address:str, limit:int=5):
    result=[]
    api_key= os.environ[api_key]
    url= f"https://api.openweathermap.org/geo/1.0/direct?q={address}&limit={limit}&appid={api_key}"
    r= requests.get(url)
    content= r.json()
    result.append({"lat": content[0]['lat'], "lon": content[0]['lon']})
    return result

def get_weather_forecast(api_key:str, lat:float, lon:float):
    api_key= os.environ[api_key]
    url= f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    r= requests.get(url)
    content= r.json()
    return content

lat= (geocode_locator("weather_api", "Karlsruhe,DE"))[0]['lat']
lon= (geocode_locator("weather_api", "Karlsruhe,DE"))[0]['lon']

weather_forecast= get_weather_forecast("weather_api", lat, lon)
results_list = []
for forecast in weather_forecast['list']:
    results_list.append({
        "City": weather_forecast["city"]["name"],
        "Time": datetime.datetime.fromtimestamp(forecast['dt']),
        "Temperature": forecast["main"]["temp"],
        "WeatherDescription": forecast["weather"][0]["description"]
    })

results_df= pd.DataFrame(results_list, columns=["City", "Time", "Temperature", "WeatherDescription"])
print(results_df.head())

#save the reult as csv file
results_df.to_csv("weather_forecast.csv", index=False)