import os
import subprocess
from time import sleep
import string
import re
import evdev
# file and directory listing
def inputVolant():
    print("débranchez le volant")
    sleep(2)
    returned_text1=[]
    returned_text2=[]
    returned_text1.append(subprocess.check_output("ls /dev/input/", shell=True, universal_newlines=True))
    print("branchez votre périphérique")
    sleep (3)
    returned_text2.append(subprocess.check_output("ls /dev/input/", shell=True, universal_newlines=True))
    longListe1 = len(returned_text1[0])
    longListe2 = len(returned_text2[0])
    liste1=[]
    liste2=[]
    print(longListe1,longListe2)
    chaineTemporaire=""
    for i in range (longListe1):
        lettre = returned_text1[0][i]
        chaineTemporaire=chaineTemporaire+str(lettre)
        if returned_text1[0][i] == "\n":
            liste1.append(chaineTemporaire)
            chaineTemporaire = ""

    for i in range (longListe2):
        lettre = returned_text2[0][i]
        chaineTemporaire=chaineTemporaire+str(lettre)
        if returned_text2[0][i] == "\n":
            liste2.append(chaineTemporaire)
            chaineTemporaire = ""        


    for i in range (len(liste1)):
        chainetempo = re.sub('\n','',liste1[i])
        liste1[i] = chainetempo
    for i in range (len(liste2)):
        chainetempo = re.sub('\n','',liste2[i])
        liste2[i] = chainetempo
        
    print(liste1)
    print(liste2)

    long = min(len(liste1),(len(liste2)))
    for i in range (long):
        if liste1[i] != liste2[i]:
            print(liste2[i])
            event = liste2[i]
            break
    return event


def selectDevice():
    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    print("Available devices:")
    print("------------------")
    numDevices = len(devices)
    for i in range(numDevices):
        device = devices[i]
        print(numDevices-1-i, "-", device.name)

    devNum = int(input("\nChoose a device: "))
    device = devices[devNum]
    #nameDevice = "event"+str(devNum)
    #print(nameDevice)
    return devNum

#selectDevice()