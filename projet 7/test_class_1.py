#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:35:29 2021

@author: nsi_1
"""

from baseDeDonee import *
from envoiToVoiture import *
from modificationValeursVolant import *
from afficheur7Segments import *

class joueur:     
        
    def __init__(self,nombreJoueur):
        self.vitesse = 0
        self.etat = 0
        self.nombreJoueur = nombreJoueur
        gamepadANDdictio = mainBaseDeDonee()
        self.gamepad = gamepadANDdictio[0]
        self.dictio = gamepadANDdictio[1]
    
    def creationClassLecture(self,mode):
        self.mode = mode
        self.read = lecture(self.mode,self.dictio,self.gamepad)       
               
               
    def update(self):
        self.read.eventRead()
        self.listSpidVolant = mainModificationValeurs(self.mode,self.gamepad,self.read,self.vitesse,self.etat)
        self.speed = self.listSpidVolant[0]
        self.volant = self.listSpidVolant[1]
        self.vitesse = self.listSpidVolant[2][0]
        self.etat = self.listSpidVolant[2][1]
        controlVoiture(self.speed,self.volant)
        #print(self.nombreJoueur,self.speed)
        #print("joueur:",self.nombreJoueur,"speed",self.speed,"volant",self.volant,"vitesse",self.vitesse)
        if self.nombreJoueur == 0:
            afficherVitesse(self.speed,self.vitesse)


def demandeMode():
    
    modes = ["mode intérieur (voiture bridé)","mode réaliste (avec des vitesses)","mode normal (juste volant et pédales)"]
    print("###################")
    for i in range (len(modes)):
        print("____________")
        print("mode ",i," :",modes[i])
        
    rep = int(input("--- \n choisissez le mode qui vous interesse: "))
    return(rep)
    
def demandeNbrJoueur():    
    nbrjoueur = int(input("combien de joueurs ?"))
    listeJoueurs = []
    for i in range (nbrjoueur) :
        print("______ \n joueur",i+1)
        test = joueur(i)
        listeJoueurs.append(test)
    return listeJoueurs
    
def mainTest():
    listeJoueur = demandeNbrJoueur()
    nbrMode = demandeMode()
    boucle = len(listeJoueur)
    for i in range (boucle):
        listeJoueur[i].creationClassLecture(nbrMode)
    while True:
        for i in range (boucle):
            listeJoueur[i].update()

mainTest()

