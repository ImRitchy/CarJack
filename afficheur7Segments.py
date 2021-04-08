# Adafruit
import board
import busio
from adafruit_ht16k33 import segments

#initialisation des ports pour la carte qui affiche
i2c = busio.I2C(board.SCL, board.SDA)
display = segments.Seg7x4(i2c)
display.fill(0)


def modifAffichageVitesse(spid):
    spid = int(-((spid*2)-100))
    if spid <= -99:
        spid = -99
    if spid >= 99:
        spid = 99
    if spid >= -3 and spid <= 3:
        spid = 0
    return spid

def afficherVitesse(value,vitesse):
    valueAffichage = modifAffichageVitesse(value)  
    #pour ne pas que l'on affiche une valeur a 3 chiffres
    #valueAffichage=int(-valueAffichage)
    if valueAffichage > -100 and valueAffichage < 100:
        #display.fill(0)
        #print(valueAffichage)
        #en fonction du nombre de caractères, on affiche plus ou moins d'espace        
        if valueAffichage <= -10 :
            text = str(vitesse) +":"+  str(valueAffichage)
        if valueAffichage >= 10 or valueAffichage <0 and valueAffichage > -10 :
            text =  str(vitesse) + " :" +  str(valueAffichage)
        if valueAffichage >= 0 and valueAffichage < 10  :
            text =  str(vitesse) + " : " + str(valueAffichage)
        #on écrit le texte sur le petit écran
        display.print(text)
    
    

'''
def affichageText(speedPourAfficher):
    #pour ne pas que l'on affiche une valeur a 3 chiffres
    speedPourAfficher=int(-speedPourAfficher)
    if speedPourAfficher > -100 and speedPourAfficher < 100:
        #display.fill(0)
        
        #en fonction du nombre de caractères, on affiche plus ou moins d'espace
        
        if speedPourAfficher <= -10 :
            text = str(vitesse) +":"+  str(speedPourAfficher)
        if speedPourAfficher >= 10 or speedPourAfficher <0 and speedPourAfficher > -10 :
            text =  str(vitesse) + ": " +  str(speedPourAfficher)
        if speedPourAfficher >= 0 and speedPourAfficher < 10  :
            text =  str(vitesse) + " : " + str(speedPourAfficher)
        #on écrit le texte sur le petit écran
        display.print(text)
        #on appelle la fonction qui renvoi la fréquence on fonction de la vitesse
        acceleration(SPEED)
        
'''