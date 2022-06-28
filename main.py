
import requests
import os
import json
import methods
import urllib.parse

language = 'en'
query = '(#IKEA OR @IKEA OR ikea)'
full_query = f'{query} lang:{language}'
add_column = 'created_at'
max_results = 10

url = f'https://api.twitter.com/2/tweets/search/recent?query={urllib.parse.quote(full_query)}&tweet.fields={add_column}&max_results={max_results}'

def main(url):

    next_token = 'N/A'
    while next_token != '' or next_token == 'N/A':
        
        if next_token == 'N/A': # First run
            json_response = methods.connect_to_endpoint(url)
        else:
            json_response = methods.connect_to_endpoint(f'{url}&next_token={next_token}')

        #print(json_response["meta"]["next_token"])
        methods.pass_to_pubsub(json_response)
        next_token = (json_response["meta"]["next_token"])

if __name__ == "__main__":

    main(url)

