import os
import time
try:
    from alive_progress import alive_bar
except:
    print("\u001b[33m[!] \u001b[31mALIVE_BAR not installed, start installation!\033[0m\n")
    time.sleep(1)
    os.system("pip install alive_progress")
    os.system("python update_module.py")

print("\u001b[33m[+] \u001b[32mI'm starting to update the program!\033[0m\n")

os.system("clear")
items = range(1)            
with alive_bar(len(items)) as bar:   
    for item in items:
        os.system("cd && rm -rf spamr && git clone https://github.com/kirill2281337227/spamr")
        bar()
os.system("clear")
print("\u001b[33mSuccessfully updated!\n\033[0m")                       
time.sleep(3)
os.system("cd && cd spamr && python spamr.py")
