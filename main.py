import methods
import urllib.parse

"""
Preferences:
For query building check: https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query
""" 
language = 'en'
query = '(#IKEA OR @IKEA OR ikea)'
full_query = f'{query} lang:{language}'
add_column = 'created_at'
max_results = 10

# optional, set starting datetime (maximum 7 days back)
# Format: YYYY-mm-DDTHH:MM:SS.000Z
start_time = '2022-06-27T23:32:21.000Z'

if start_time != '':
    url = f'https://api.twitter.com/2/tweets/search/recent?query={urllib.parse.quote(full_query)}&start_time={start_time}&tweet.fields={add_column}&max_results={max_results}'
else:
    url = f'https://api.twitter.com/2/tweets/search/recent?query={urllib.parse.quote(full_query)}&tweet.fields={add_column}&max_results={max_results}'

if __name__ == "__main__":
    methods.call_api_to_pubsub(url)
