import methods
import urllib.parse

language = 'en'
query = '(#IKEA OR @IKEA OR ikea)'
full_query = f'{query} lang:{language}'
add_column = 'created_at'
max_results = 10

url = f'https://api.twitter.com/2/tweets/search/recent?query={urllib.parse.quote(full_query)}&tweet.fields={add_column}&max_results={max_results}'

if __name__ == "__main__":
    methods.call_api_to_pubsub(url)
