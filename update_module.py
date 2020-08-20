from alive_progress import alive_bar
from getch import pause
import os
import time

os.system("clear")
items = range(1)            
with alive_bar(len(items)) as bar:   
    for item in items:
        os.system("cd && rm -rf spamr && git clone https://github.com/kirill2281337227/spamr")
        bar()
pause()
os.system("clear")
print("\u001b[33mSuccessfully updated!\n\033[0m")                       
time.sleep(3)
os.system("cd && cd spamr && python spamr.py")

# Это код модуля обновлений!
