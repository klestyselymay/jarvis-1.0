import webbrowser
import socket
import random
from threading import Thread
from datetime import datetime
from AppOpener import run
import os
import pyperclip

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

while True:
    cmd = s.recv(1024).decode()
    if '4r6j38rj3imyr83rjmy373o4krym389r3ijkr9w:app' in cmd:
        app1 = cmd.replace('4r6j38rj3imyr83rjmy373o4krym389r3ijkr9w:app', '')
        run(app1)

    elif '4r6j38rj3imyr83rjmy373o4krym389r3ijkr9w:close' in cmd:
        cl_app = cmd.replace('4r6j38rj3imyr83rjmy373o4krym389r3ijkr9w:close', '')
        os.system(f'TASKKILL /F /IM {cl_app}')

    elif 'ebtru2rjhntur2ijrnye27i2jkm7m24iujnrug34jm7hr3jghntn783j:::sg:clipboard' in cmd:
        clp1 = cmd.replace('ebtru2rjhntur2ijrnye27i2jkm7m24iujnrug34jm7hr3jghntn783j:::sg:clipboard', '')
        pyperclip.copy(clp1)


    else:
        url = cmd
        webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(f'https://www.google.com/search?q={url}')