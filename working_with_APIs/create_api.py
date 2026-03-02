'''
This code demonstrates how to create your own API 
This API needs to made Public since it is created in a local IDE and we need to access it from the browser.
To create an API, we can use the Flask framework in Python.

'''
from flask import Flask, jsonify


# We will use BeautifulSoup to scrape the exchange rate from a website, and requests to make the HTTP request to get the content of the page.
from bs4 import BeautifulSoup
import requests

def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  
  return rate

app = Flask(__name__)

# This is the route for the API, it will return a simple message when accessed

@app.route('/')
def home():
    return "<h1> Currency Rate API </h1>" \
    "<p><h3>Base URL:</h3> /api/v1/input_currency-output_currency </p>"

'''
The base url for the API is /api/v1/ and then we can specify the input currency and output currency 
in the format of ISO 4217, that is, three-letter codes like USD, EUR, GBP, etc.

Next we define the function that will be called when the route is accessed, it will take the input currency and output currency as 
parameters, and return the exchange rate from input currency to output currency in a JSON format.
We will use the get_currency function to get the exchange rate and then return it in a dictionary format which will be converted to 
JSON using jsonify function from Flask.

'''
# This route will return the exchange rate from input currency to output currency when accessed
@app.route('/api/v1/<in_cur>-<out_cur>')
def api_exchange_rate(in_cur, out_cur):
    rate= get_currency(in_cur, out_cur)
    result_dictionary={"input_currency": in_cur, "output_currency": out_cur, "rate": rate}
    return jsonify(result_dictionary)

app.run(debug=True)