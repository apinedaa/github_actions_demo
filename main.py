
import math
import os
import requests


def add(a, b) -> int:
    return math.floor(a + b)


def to_sentence(s) -> str:
    s = s.capitalize()

    if s.endswith('.'):
        return s
    else:
        return s + '.'

def difference (a, b) -> int:
    return a-b

#todo constant request in SMEE
temporal_url = 'https://webhook.site/01b5eafd-e702-40d7-b8cd-6c73f74b386c'
headers= {"Content-Type": "application/json"}

requests.request("POST",temporal_url,data={'example': 'value'}, headers=headers)
