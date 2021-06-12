from luhn import verify
import random, string
import os
import random
import string
import time
import ctypes
from colorama import Fore, init
import sys
import requests



key = ["Nots", "Waffle"]
check = input(Fore.GREEN + "What is the key?\n")

check2 = input(Fore.GREEN + "What Bin Do You Want?\n")

#ALL STORECARD BINS
#60457811 - MOST COMMONLY USED
#60457812
#60457813
#60457814 - PRIVATE BIN
#60457815
#60457816
#60457817 (credit card line)


def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)

def slowprints(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.06)


if check in key:
  slowprints(Fore.RED + """
               __  __ _     
 __ __ ____ _ / _|/ _| |___ 
 \ V  V / _` |  _|  _| / -_)
  \_/\_/\__,_|_| |_| |_\___|
 """ + Fore.RESET)
slowprints(Fore.RED + "Made By Nots And ItzDrWaffle")
slowprint(Fore.BLUE + "DO NOT SKID.")
time.sleep(5)
BIN = check2
 
slowprint(Fore.GREEN + "Thanks for using my gen! Starting in 10 seconds.")
time.sleep(10)
while True:

        cc = ('').join(random.choices(string.digits, k=8))
        card = BIN + cc
        check = verify(card)
        if check == True:

                print(Fore.GREEN + f"[VALID] {card}")
                f = open("4x.txt",'a')
                f.write(f"{card}\n")
                f.close()
                requests.post(f"(webhook here)",json=
                {'content':card,
                'username':"Faster Than Nots™"})
                time.sleep(1)
        else:
          print(Fore.RED + f"[INVALID] {card}")
else:
  print(Fore.RED + "Error: Wrong key.")


#you can use a bin between 60457811 and 60457817 for storecard Errors 
##ik its because repl.it doesnt have an operating system
##you need to run it on real python
##brb i have to watch prince philips funeral :joy:  =a=
