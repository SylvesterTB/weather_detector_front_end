from flask import Flask, render_template
from data import *
import logging
from threading import Thread

def color_selector(input_temperature):
    if 20 >input_temperature > 0:
        color_var = '00BD00'
    elif 25 >input_temperature>= 20:
        color_var = 'FF9200'
    else:
        color_var = 'FF0000'
    return color_var


logging.basicConfig(filename='logging_info.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logger=logging.getLogger() 
logger.setLevel(logging.DEBUG) 
logging.getLogger().addHandler(logging.StreamHandler())

app = Flask(__name__) 

@app.route('/')
def index():
    return "The web app is working"

@app.route('/start')
def weather_start():
    global thread
    if thread is None or not thread.is_alive():
        turn_on()
        thread = Thread(target=weather_detector)
        thread.start()
        return 'Process started', 200
    else:
        return 'Process is already running', 200

@app.route('/stop')
def weather_stop():
    turn_off()
    return 'Process stopped', 200

@app.route('/temperature')
def retrieve_temperature():
    # temperature = get_temperature()
    temperature = 10
    return render_template('temperature.html', temp = temperature, color = color_selector(temperature))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, threaded=True)