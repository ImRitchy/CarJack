#fichier qui gère la lecture du volant
#from lireLeVolant import *
from baseDeDonee import *
from envoiToVoiture import *
from modificationValeursVolant import *
from afficheur7Segments import *

'''
# Adafruit
import board
import busio
from adafruit_ht16k33 import segments

#initialisation des ports pour la carte qui affiche
i2c = busio.I2C(board.SCL, board.SDA)
display = segments.Seg7x4(i2c)
display.fill(0)
'''

def demande():
    modes = ["mode intérieur (voiture bridé)","mode réaliste (avec des vitesses)","mode normal (juste volant et pédales)"]
    print("###################")
    for i in range (len(modes)):
        print("____________")
        print("mode ",i," :",modes[i])
        
    rep = int(input("--- \n choisissez le mode qui vous interesse: "))
    return rep

def main():
    gamepad = mainBaseDeDonee()
    reponse = demande()
    
    while True :
        eventRead(gamepad) #la fonction qui met a jour les variables
        listSpidVolant = mainModificationValeurs(reponse) #list=[SPEED,VOLANT,VITESSE]
        speed = listSpidVolant[0]
        volant = listSpidVolant[1]
        vitesse = listSpidVolant[2]
        controlVoiture(speed,volant)
        #print(speed)
        afficherVitesse(speed,vitesse)

if __name__ == '__main__' :
    main()
