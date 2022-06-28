import requests
import os
import json
import emoji
import regex
from google.cloud import pubsub_v1

import config
import example


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {config.bearer_token}"
    r.headers["User-Agent"] = "v2UserMentionsPython"
    return r

def connect_to_endpoint(url):
    """
    Method to connect to the twitter enpoint
    """
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def decode_utf18(line):
    """
    decode utf18, handles 
    """
    return line.encode('ascii', 'ignore').decode('ascii')

def extract_emoji(text):
    """
    extract emojis from text and store in comma seperated string
    """
    emoji_string = ''
    data = regex.findall(r'\X', text)
    for word in data:
        if any(char in emoji.UNICODE_EMOJI['en'] for char in word):
            emoji_string += (word + ',')
    
    return emoji_string

def pass_to_pubsub(message_json):
    """
    Pass json object to pubsub for ingestion
    """
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.credentials_path

    publisher = pubsub_v1.PublisherClient()
    
    for message in message_json['data']:

        body = json.dumps(message).encode('utf-8') 

        emoji_string = extract_emoji(message['text'])

        attributes = {
            'emojis_used': emoji_string
        }

        future = publisher.publish(config.pubsub_topic, body, **attributes)
        print(f'published message id {future.result()}')

def call_api_to_pubsub(url):
    """
    1. use URL to connect to twitter API
    2. Loop through json response and call pass_to_pubsub method to push each 
       individual message to pub/sub
    """
    next_token = 'N/A'
    while next_token != '' or next_token == 'N/A':
        
        if next_token == 'N/A': # First run
            json_response = connect_to_endpoint(url)
        else:
            json_response = connect_to_endpoint(f'{url}&next_token={next_token}')

        #print(json_response["meta"]["next_token"])
        pass_to_pubsub(json_response)
        next_token = (json_response["meta"]["next_token"])


