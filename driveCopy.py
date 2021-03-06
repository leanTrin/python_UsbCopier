#!/usr/bin/env python3
##########################################################
# Created by Leandro Trinidad
# Description:
#   Copies a certain folder of a usb to another folder in
#   the pi. Useful for Copying files while the pi is in
#   headless mode.
#
# Prequsities
#   - eject -- run 'sudo apt install eject'
####################################

#TODO: Memory optimization

import os
from shutil import copyfile
import time
import subprocess

dev = False                         # If True: logs the information in the terminal

usb = "/media/pi/9132-18E9/movies"  #TODO: this will be different when using other usbs
usbDisk = "/dev/sda1"               #TODO: auto detect a new usb pluged in and see the folders
storage = "/home/pi/Movies"         #TODO: the storage folder can be in another usb

def printlog(text):
    if dev:
        print("[%s]: %s" %(time.asctime( time.localtime(time.time())),text))
while True:
    try:
        if(os.path.isdir(usb)):
            copy = []
            usbFiles = [f for f in os.listdir(usb)]
            storageFiles = [f for f in os.listdir(storage)]
            for i in usbFiles:
                if(i not in storageFiles):
                    copy.append(i)
            if(copy): # if there is a new file in the usb that is not already in the server
                printlog(copy)
                for item in copy:
                    printlog("copying " + item)
                    copyfile(usb + "/" + item, storage + "/" + item)
                    printlog("done")
            #TODO: gpio lights
            os.system('sudo eject ' + usbDisk)
            printlog("Files Copied")
            time.sleep(10)
    except:
        pass
    time.sleep(60)
