'''
This code demonstrates how to make a GET request to a REST API using the `requests` library 
in Python. It retrieves data from the specified API endpoint and prints the response in 
JSON format.

In this code, we define a function `get_data_from_api` that takes the base URL of the API.
api_key: API key of the user stored in environment variable
q= keywords or phrases to search for in the article title and body.
    -Accepted values are: bitcoin, apple, tesla, etc. Default is None (no keyword filtering).
domains= A comma-separated string of domains to restrict the search to.
    -Example: "bbc.co.uk, techcrunch.com,m wsj.com". Default is None (no domain filtering).
country= The 2-letter ISO 3166-1 code of the country you want to
language= The 2-letter ISO-639-1 code of the language you want to get headlines for.
sortBy= The order to sort the articles in. Possible options: relevancy, popularity, publishedAt.
default is publishedAt (newest first).
    - relevancy = articles more closely related to q come first.
    - popularity = articles from popular sources and publishers come first.
    - publishedAt = newest articles come first.
    
base_url: https://newsapi.org/v2/everything

'''

import requests
from dotenv import load_dotenv
load_dotenv() # Load environment variables from local .env file
import os

def get_data_from_api(base_url:str, api_key:str, country:str=None, domains:str=None, q:str="None", language:str="en", 
                      sortBy:str="publishedAt"):
    api_key= os.environ[api_key]
    url= f"{base_url}?apiKey={api_key}"
    if country:
        url += f"&country={country}"
    if domains:
        url += f"&domains={domains}"
    if q != "None":
        url += f"&q={q}"
    if language != "en":
        url += f"&language={language}"
    if sortBy != "publishedAt":
        url += f"&sortBy={sortBy}"
    r= requests.get(url)
    content= r.json()
    return content 

print(get_data_from_api("https://newsapi.org/v2/everything", "news_api", q= "cryptocurrency", sortBy= "relevancy"))