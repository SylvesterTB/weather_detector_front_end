import requests

TOKEN = "6394746388:AAH9cXDsJb3caDc6_3wzuFLFMgnu7t46aH0"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
error_message = 'something'
import requests
TOKEN = "6394746388:AAH9cXDsJb3caDc6_3wzuFLFMgnu7t46aH0"
chat_id = "5946134823"
message = "error detected"
url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
# print(requests.get(url).json()) # this sends the message

def telebot(string, user_preference):
    url2 = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={string, user_preference}"
    requests.get(url2).json()




# chat ID: 5946134823 
# bot ID: 6394746388:AAH9cXDsJb3caDc6_3wzuFLFMgnu7t46aH0