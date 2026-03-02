'''


'''
import requests
from dotenv import load_dotenv
load_dotenv() # Load environment variables from local .env file
import os

def geocode_locator(api_key:str, address:str, limit:int=5):
    api_key= os.environ[api_key]
    url= f"http://api.openweathermap.org/geo/1.0/direct?q={address}&limit={limit}&appid={api_key}"
    r= requests.get(url)
    content= r.json()
    return content[0]['lat'], content[0]['lon']

print(geocode_locator(api_key="weather_api", address="Karlsruhe, DE"))