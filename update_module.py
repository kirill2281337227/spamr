from alive_progress import alive_bar
import os
import time

os.system("clear")
items = range(1)            
with alive_bar(len(items)) as bar:   
    for item in items:          
        os.system("cd")
        os.system("rm -rf spamr")
        os.system("git clone https://github.com/kirill2281337227/spamr")
        os.system("cd spamr")
        bar()
os.system("clear")
print("\u001b[33mSuccessfully updated!\n\033[0m")                       
time.sleep(3)
os.system("python spamr.py")

