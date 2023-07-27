import requests
from notify_bot import *
import time
from threading import Thread
import logging
import os


logging.basicConfig(filename='logging_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
logging.getLogger().addHandler(logging.StreamHandler())

def read_api_key():
    api_key = os.environ['API_KEY'] 
    return api_key




#temp_alert = input('At what temperature would you like to be alerted (in celcius)?')
#temp_alert = int(temp_alert)

def get_temperature():
        city = "Munich" 
        api_key = read_api_key()
        if api_key == '':
             raise Exception("api_key should not be empty!")
        base_url = f"http://api.weatherapi.com/v1/current.json?key={read_api_key()}&q={city}"
        response = requests.get(base_url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["current"]["temp_c"]

        return temperature

running = True
thread = None


def turn_off():
    logger.info('weather turning off...')
    global running
    running = False

def turn_on():
     global running
     running = True





def weather_detector():
    global running
    message_frequency = 60  # in seconds
    temperature_threshhold = 10
    temperature = get_temperature() 
    logger.info('runnning:' + str(running))
    while running:
        if temperature >= temperature_threshhold:
            telebot('the temperature is greater than', temperature_threshhold)
            logger.info('Checking temperature...')
        else:
            print("")
        temperature = get_temperature()
        time.sleep(message_frequency)

             