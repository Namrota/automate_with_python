'''
In this code we are using LanguageTool API to check the grammar of a given text.

For this scenario we make a POST request to the API endpoint with the text we want to check, 
and the API will return a JSON response with the grammar errors found in the text.

For grammar checking it can be passed as a 'text' param for an actual text or 'data' param for XML, JSON or form data. 
We will use the 'data' param to pass the text we want to check in JSON format.

'''

import requests
import json

base_url= "https://api.languagetool.org/v2/check"
text_input= input("Enter a sentence to check for grammar: ")
language= input("Enter the language code (e.g. en-US for English, es-ES for Spanish, or de-DE): ")
data= {
    "text": text_input,
    "language": language
}
response= requests.post(base_url, data=data)
# The response from the API is in JSON format, we can parse it using json.loads() function to get a Python dictionary.
result= json.loads(response.text)
print(f"Text submitted:{result['matches'][0]['context']['text']} Grammar Check: {result['matches'][0]['message']} Suggested Correction: {result['matches'][0]['replacements']}   ")