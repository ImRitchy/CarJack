# -*- coding: utf-8 -*-
from time import sleep
#import evdev
from evdev import InputDevice, categorize, ecodes
#import l'os
import os
#import csv
import csv
#import path
import os.path
#import volant
from lectureVolant import *
#import test
from detectionPeripherique import *
#global gamepad

def demandeNomVolant():
    return gamepad.name

def chercheVolants(nbr,nameVolant):
    for i in range(nbr):
        name = "dico"+str(i)+".csv"
        fichier = open(str(name), "r")
        read=csv.reader(fichier)
        for lecture in read:
            if lecture[1] == str(nameVolant):
                return name
    return None
    
def recupererFichierVolant(nomFichier):
    fichier = open(str(nomFichier), "r")
    read=csv.reader(fichier)
    laListe = []
    for lecture in read:
        laListe.append(lecture[1])
    return laListe
        
    
    
def chercheTouches():
    listeCode = ["volant","paletteDroite","paletteGauche","pedaleDroite","pedaleGauche"]
    listeType = ["volant","paletteDroite","paletteGauche","pedaleDroite","pedaleGauche"]
    for i in range(len(listeCode)):
        print("faites bouger/appuyez sur : ",listeCode[i])
        
        for event in gamepad.read_loop():
            #print(event)
            if event.value != 0 and event.value < 9999 and event.code!=listeCode[0]:
                if i>0:
                    if not event.code in listeCode :
                        #print(event)
                        listeCode[i] = event.code
                        listeType[i] = event.type
                else:
                    #print(event)
                    listeCode[i] = event.code
                    listeType[i] = event.type
                
            if type(listeCode[i]) != str and type(listeType[i]) != str :
                #print(listeCode,listeType)
                sleep(2)
                break
            
    return (listeCode,listeType)


def ONCHERCHEVALUE(dico,tupleList):
    #liste = [code,type]
    dico["volantCode"] = int(tupleList[0][0])
    dico["volantType"] = int(tupleList[1][0])
    dico["paletteDCode"] = int(tupleList[0][1])
    dico["paletteDType"] = int(tupleList[1][1])
    dico["paletteGCode"] = int(tupleList[0][2])
    dico["paletteGType"] = int(tupleList[1][2])
    dico["pedaleDCode"] = int(tupleList[0][3])
    dico["pedaleDType"] = int(tupleList[1][3])
    dico["pedaleGCode"] = int(tupleList[0][4])
    dico["pedaleGType"] = int(tupleList[1][4])
    #print(type(dico["volantCodeAndType"]))
    
        
    print("bougez le volant et les pedales au maximum puis appuyez sur la palette de droite")
    for event in gamepad.read_loop():
        #print(event)
        if event != None and event.value != 0:
            
            #print(event)
            
            if event.code == dico["paletteDCode"] and event.type == dico["paletteDType"]:
                print("\n vous pouvez utiliser le volant ")
                #print(dico)
                sleep(5)
                return dico
                    
            if event.code == dico["volantCode"] and event.type == dico["volantType"] :
                if dico['volantAngleMax'] < event.value: 
                    dico['volantAngleMax'] = event.value
                if dico['volantAngleMin'] > event.value:
                    dico['volantAngleMin'] = event.value
            
            if event.code == dico["pedaleGCode"] and event.type == dico["pedaleGType"] :
                if dico['pedaleGaucheMax'] < event.value:
                    dico['pedaleGaucheMax'] = event.value
                if dico['pedaleGaucheMin'] > event.value:
                    dico['pedaleGaucheMin'] = event.value
                    
            if event.code == dico["pedaleDCode"] and event.type == dico["pedaleDType"] :
                if dico['pedaleDroiteMax'] < event.value:
                    dico['pedaleDroiteMax'] = event.value
                if dico['pedaleDroiteMin'] > event.value:
                    dico['pedaleDroiteMin'] = event.value


def chercheLesFichiersVolants():
    nombreFichierDuVolant = 0
    print("on cherche un fichier correspondant a votre peripherique")
    for i in range (10):
        name = "dico"+str(i)+".csv"
        if os.path.isfile(str(name)):
            #print ("File exist")
            nombreFichierDuVolant += 1
        '''else:
            print ("File not exist")'''
    #nomFichier = "dico"+str(nombreFichierDuVolant)+".csv"
    return nombreFichierDuVolant

def creationNewDico(dico,nbrNextFichier):
    #print(nbrNextFichier)
    nomFichier = "dico"+str(nbrNextFichier)+".csv"
    fichier = open(str(nomFichier), "w")
    write = csv.writer(fichier)
    for key,val in dico.items():
        write.writerow([key, val])
    fichier.close()
    #print("end")





def mainBaseDeDonee():
    global gamepad
    event = selectDevice()
    commande = '/dev/input/event'+str(event)
    gamepad = InputDevice(str(commande))
    print("________________________")
    
    dictionnaire = {
        "nomVolant" : "",
        "volantCode" : 0,
        "volantType" : 0,
        "paletteDCode" : 0,
        "paletteDType" : 0,
        "paletteGCode" : 0,
        "paletteGType" : 0,
        "pedaleDCode" : 0,
        "pedaleDType" : 0,
        "pedaleGCode" : 0,
        "PedaleGType" : 0,
        "pedaleDroiteMax" : 0,
        "pedaleDroiteMin" : 1000,
        "pedaleGaucheMax" : 0,
        "pedaleGaucheMin" : 1000,
        "volantAngleMax":0,
        "volantAngleMin":1000
        }
    
    nombreProchainFichier = chercheLesFichiersVolants()
    nomFichier = demandeNomVolant()
    #print(nomFichier,nombreProchainFichier)
    reponse = chercheVolants(nombreProchainFichier,nomFichier)
    
    sleep(1)
    print("________________________")
    if reponse == None :
        print("fichier non trouvé, besoin de faire une calibration")
        tupleCodeType = chercheTouches()
        dictionnaire["nomVolant"] = nomFichier
        reponse = "dico"+str(nombreProchainFichier)+".csv"
        #print(reponse)
        newDico = ONCHERCHEVALUE(dictionnaire,tupleCodeType)
        #print(newDico,type(newDico['volantCodeAndType']))
        creationNewDico(newDico,nombreProchainFichier)
    print("volant trouvé dans le fichier : " , reponse)
    dictioEnListe = recupererFichierVolant(reponse)
    print("________________________ \n",dictioEnListe,"le dico qu'on a recup")
    sleep(2)
    listeCodes(dictioEnListe)
    #print("dico mis a jour cdxsijocwdso")
    return gamepad


#version 11:20

        
