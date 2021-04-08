# -*- coding: utf-8 -*-
from time import sleep
#import evdev
from evdev import InputDevice, categorize, ecodes
#import l'os
import os
from baseDeDonee import *
'''
#global listeCodesTypesVolant
global pedaleDroite
global pedaleGauche
global volantAngle
global paletteDroite
global paletteGauche
global minimums
global maximums
#global gamepad
'''
def listeCodes(dictio):
    global dic
    '''
        "nomVolant" ,
        "volantCode" ,
        "volantType",
        "paletteDCode",
        "paletteDType",
        "paletteGCode",
        "paletteGType",
        "pedaleDCode",
        "pedaleDType",
        "pedaleGCode",
        "PedaleGType",
        "pedaleDroiteMax",
        "pedaleDroiteMin",
        "pedaleGaucheMax",
        "pedaleGaucheMin",
        "volantAngleMax",
        "volantAngleMin"
        '''
    global pedaleDroite
    global pedaleGauche
    global volantAngle
    global paletteDroite
    global paletteGauche
    global minimums
    global maximums
    dic = dictio
    pedaleDroite = dic[12]
    pedaleGauche = dic[14]
    volantAngle = dic[16]
    paletteDroite = 0
    paletteGauche = 0
    minimums = [dic[12],dic[14],dic[16]]
    maximums = [dic[11],dic[13],dic[15]]
    #print(volantAngle)
        
    


def eventRead(gamepad):
    global pedaleDroite
    global pedaleGauche
    global volantAngle
    global paletteDroite
    global paletteGauche
    #print(dic[1],type(dic[1]))
    #print(dic[1][0])
    #global gamepad
    #gamepad = InputDevice('/dev/input/event1')
    
    event = gamepad.read_one()
    while event != None:
        '''if event.value == 0:
            break'''
        
        #print(listeCodesTypesVolant)
        #print(event.code,event.type)
        #print(dic[1],dic[2])
        #print(volantAngle)
        if event.code == int(dic[3]) and event.type == int(dic[4]):
            paletteDroite = event.value
        
            
        if event.code == int(dic[5]) and event.type == int(dic[6]):
            paletteGauche = event.value
       
        #print("cacaca") 
        if event.code == int(dic[1]) and event.type == int(dic[2]) :
            #print("cacaca")
            volantAngle = event.value
            
        if event.code == int(dic[7]) and event.type == int(dic[8]) :
            pedaleDroite = event.value
            
        if event.code == int(dic[9]) and event.type == int(dic[10]) :
            #print("caca",event.value)
            pedaleGauche = event.value
        event = gamepad.read_one()
        
def getVitessePedaleDroite():
    return int(pedaleDroite)
def getVitessePedaleGauche():
    return int(pedaleGauche)
def getAngleVolant():
    return int(volantAngle)
def getPaletteDroite():
    return int(paletteDroite)
def getPaletteGauche():
    return int(paletteGauche)
def getMaximums():
    return maximums
def getMinimums():
    return minimums


    





#good version with dico
#version 11:20
    




