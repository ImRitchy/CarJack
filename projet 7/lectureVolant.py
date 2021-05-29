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

class lecture:
    def __init__(self,mode,dictio,gamepad):
        self.mode = mode
        self.dic = dictio
        self.gamepad = gamepad
        self.volantAngle = 0
        self.paletteDroite = 0
        self.paletteGauche = 0
        self.pedaleDroite = 0
        self.pedaleGauche = 0
        self.listeCodes()
    
    def listeCodes(self):  #a rename initialisationCodes
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
        self.pedaleDroiteMax = self.dic[12]
        self.pedaleGaucheMax = self.dic[14]
        self.volantAngleMax = self.dic[16]
        self.paletteDroite = 0
        self.paletteGauche = 0
        self.minimums = [self.dic[12],self.dic[14],self.dic[16]]
        self.maximums = [self.dic[11],self.dic[13],self.dic[15]]
        
    def eventRead(self):       
        event = self.gamepad.read_one()
        while event != None:
            '''if event.value == 0:
                break'''
            if event.code == int(self.dic[3]) and event.type == int(self.dic[4]):
                self.paletteDroite = event.value           
            if event.code == int(self.dic[5]) and event.type == int(self.dic[6]):
                self.paletteGauche = event.value
            if event.code == int(self.dic[1]) and event.type == int(self.dic[2]) :
                self.volantAngle = event.value           
            if event.code == int(self.dic[7]) and event.type == int(self.dic[8]) :
                self.pedaleDroite = event.value           
            if event.code == int(self.dic[9]) and event.type == int(self.dic[10]) :
                self.pedaleGauche = event.value
            event = self.gamepad.read_one()
        
        
    def getVitessePedaleDroite(self):
        return int(self.pedaleDroite)
    def getVitessePedaleGauche(self):
        return int(self.pedaleGauche)
    def getAngleVolant(self):
        return int(self.volantAngle)
    def getPaletteDroite(self):
        return int(self.paletteDroite)
    def getPaletteGauche(self):
        return int(self.paletteGauche)
    def getMaximums(self):
        return self.maximums
    def getMinimums(self):
        return self.minimums


    
