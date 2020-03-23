import datetime
import json
import requests
import argparse
import logging
from bs4 import BeautifulSoup
from tabulate import tabulate
from slack_client import slacker

FORMAT = '[%(asctime)-15s] %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG, filename='bot.log', filemode='a')

URL = 'https://www.mohfw.gov.in/'
SHORT_HEADERS = ['Sno', 'State','In','Fr','Cd','Dt']
FILE_NAME = 'corona_india_data.json'
extract_contents = lambda row: [x.text.replace('\n', '') for x in row]


def save(x):
    with open(FILE_NAME, 'w') as f:
        json.dump(x, f)


def load():
    res = {}
    with open(FILE_NAME, 'r') as f:
        res = json.load(f)
    return res
    

if __name__ == '__main__':
   
    parser  = argparse.ArgumentParser()
    parser.add_argument('--states', default=',')
    args = parser.parse_args()
    interested_states = args.states.split(',')
    
    current_time = datetime.datetime.now().strftime('%d/%m/%Y %H:%M')
    info = []

    
