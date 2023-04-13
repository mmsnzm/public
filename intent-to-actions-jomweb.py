import openai, pandas as pd
from time import sleep
from random import randint
import csv
import re
import os
import time
import math
import json, re, requests, pandas as pd
from bs4 import BeautifulSoup

openai.api_key = ""
model_engine = "text-davinci-003"

def local_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time

def qamus(word):
    import requests
    from bs4 import BeautifulSoup

    url = "https://prpm.dbp.gov.my/Cari1?keyword="+word
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')

    words=[]
    result = soup.find_all(class_="tab-content")
    for res in result:
        words.append(res.get_text())

    df = pd.DataFrame(words)
    x=df[0][0]
    if(len(x)):
        return x

def get_commands(intent):
    #end points utk setiap commands
    if intent == 'book_flight':
        return [
            {
                'url': 'https://air-asia',
                'params': {
                    'destination': 'New York',
                    'departure_date': '2023-05-01',
                    'return_date': '2023-05-05'
                }
            }
        ]
    elif intent == 'order_food':
        return [
            {
                'url': 'https://foodpandai',
                'params': {
                    'restaurant': 'Pizza Hut',
                    'cuisine': 'Italian',
                    'order_items': ['Large Pepperoni Pizza', 'Garlic Bread']
                }
            }
        ]
    elif intent == 'get_weather':
        return [
            {
                'url': 'https://rtm.gov.my/get-weather',
                'params': {
                    'location': 'Putrajaya',
                    'date': '2023-05-01'
                }
            }
        ]
    elif intent == 'get_news_updates':
        return [
            {
                'url': 'https://asterukawatni/get-news',
                'params': {
                    'topic': 'Technology',
                    'source': 'asterukawatni'
                }
            }
        ]
    elif intent == 'schedule_meeting':
        return [
            {
                'url': 'https://meeting/schedule-meeting',
                'params': {
                    'attendees': ['Meor', 'Nizam'],
                    'date': '2023-05-01',
                    'time': '14:00'
                }
            }
        ]
    elif intent == 'make_reservation':
        return [
            {
                'url': 'https://pagoda/make-reservation',
                'params': {
                    'place': 'Hotel Oyo'
                    }
            }
            ]

def process_user_input(user_input):
    prompt='''Please provide only ONE suitable intent for this sentence "'''+user_input+'''" from these options: get_weather, tanya_maksud_perkataan, check_current_time, order_pizza. Jika pilihan adalah \'tanya_maksud_perkataan\', soalan seterusnya adalah user ni nak tahu maksud perkataan apa dari ayat ini? "'+user_input+'". Return the exact word(s) asked.'''
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        n=1,
        stop=None,
        temperature=0,
    )
    intent_phrase = response.choices[0].text.strip()
    return intent_phrase

user_input=input('Nak apo??')
#user_input = 'skrg pukul berapa'
#user_input = 'cuaca mcm mana esok?'
#user_input = 'Apa maksud perkataan abai dalam dbp'
#user_input = 'apo maksud perkataan ni ha?? abaimana'

intent = process_user_input(user_input)
print(intent)

if(intent=='check_current_time'):
    print(local_time)

if(intent=='tanya_maksud_perkataan'):
    print(qamus('abai'))

if intent.lower() == "order_pizza":
    pizza_order = input("Nak order piza saiz apo??")