from lectureVolant import *

global test
test = 0
global VITESSE
VITESSE = 0

'''
#fonction qui transforme la vitesse pour etre plus comprehensible
def changerSpeedIntoAfficheur(vitesse) :
    vitesse = -((SPEED*2)-100)
    if vitesse < -99 :
        vitesse = -99
    if vitesse > 99 :
        vitesse = 99
    return vitesse
#fonction qui s'occupe des palettes
def palettes(vitesse):
    paletteD = getPaletteDroite()
    paletteG = getPaletteGauche()
    #on change les vitesses quand on appuie sur les palettes
    if paletteD != 0:
        if vitesse < 3 :
            vitesse += 1
    if paletteG != 0:
        if vitesse > 0 :
            vitesse -= 1
    return vitesse
    
#fonction qui adapte les pédales en fonction de la vitesse max
def adapteVitesse(vitesse):
    if vitesse==0:
        speed=50
    if vitesse==1:
        speed=speedSortie(0.3)
        speed<=30
    if vitesse==2:
        speed=speedSortie(0.6)
        speed<=60
    if vitesse==3:
        speed=speedSortie(1)
        speed<=99
    speed = int(speed)
    return speed
'''
'''
def speedSortie(k):
    global listeValues
    vitesseDroitep = int(-changerVitesse(listeValues[1],listeValues[0],getVitessePedaleDroite()))-1
    vitesseGauchep = int(-changerVitesse(listeValues[3],listeValues[2],getVitessePedaleGauche()))-1
    speedSortie = int(k*((vitesseDroitep/2)-(vitesseGauchep/2)+50)) #a 50 la voiture ne bouge pas
    return speedSortie
'''
'''
def reglageVitessePlus(SPEED,vitesse):
    if vitesse==1:
        SPEED+=35
    if vitesse==2:
        SPEED+=20
    SPEED=zoneMorte(SPEED)
    return SPEED
    
    
'''
'''
def reglageVitesseMoins(SPEED,vitesse):
    if vitesse==1:
        SPEED-=35
    if vitesse==2:
        SPEED-=20
    SPEED=zoneMorte(SPEED)
    return SPEED
'''
'''
def zoneMorte(SPEED):
    #on définit des zones mortes
    if SPEED<53 and SPEED>47 :
        SPEED=50
    if SPEED>=98 :
        SPEED=99
    if SPEED<=2 :
        SPEED=0
    SPEED=int(SPEED)
    return SPEED
'''





def bridage(speed,mode):
    global VITESSE
    speed = -speed+100
    listBridage = [15,25,50]
    #list[mode1Max,mode2Vitesse1,mode2Vitesse2]
    if mode == 0:
        speed = speed / 5.2
        if speed > listBridage[1] :
            speed = listBridage[1]
    if mode == 1:
        if VITESSE == 0:
            speed = 0            
        if VITESSE == 1:
            speed = speed / (4)
            if speed > listBridage[1]:
                speed = listBridage[1]
        if VITESSE == 2:
            speed = speed / (2)
            if speed > listBridage[2]:
                speed = listBridage[2]
        #print(speed)
    if mode == 2 :
        pass
    
    return -speed-100

def vitesse(paletteD,paletteG):
    global VITESSE
    global test
    if paletteD !=0 or paletteG != 0:
        test +=1
    if paletteD == 0 and paletteG == 0:
        test = 0 
    if test == 1:
        if int(paletteD) != 0:
            if VITESSE < 3 :
                VITESSE += 1
        if int(paletteG) != 0:
            if VITESSE > 0:
                VITESSE -= 1
        print("vous êtes en: ",VITESSE)
        #print(VITESSE,paletteD,paletteG)
        
        
    

def verificationPourcent(value):
    if value <= 1:
        value = 0
    if value >= 99:
        value = 100
    if value <= 51 and value >= 49:
        value = 50
    return value

#fonction qui tranforme les deux valeurs des pedales en une variable
def vitessesTo1(vitesseDroite,vitesseGauche,mini,maxi):
    vitesseDroite = -vitesseDroite/2
    vitesseGauche = 50 - vitesseGauche/2
    spid = int(vitesseGauche - vitesseDroite)
    return spid

#fonction qui tranfsorme les valeurs en pourcentage
def changerVitesse(mini,maxi,value):
    return int((value - mini)*100/(maxi-mini))


def mainModificationValeurs(number):
    global VITESSE
    angleVolant = getAngleVolant()
    
    pedaleDroite = getVitessePedaleDroite()
    pedaleGauche = getVitessePedaleGauche()
    paletteDroite = getPaletteDroite()
    paletteGauche = getPaletteGauche()
    valeursMax = getMaximums() #liste: [pedaleD,pedaleG,volant]
    valeursMin = getMinimums()
    pedaleDroitePourcent=changerVitesse(int(valeursMin[0]),int(valeursMax[0]),pedaleDroite)
    pedaleGauchePourcent=changerVitesse(int(valeursMin[1]),int(valeursMax[1]),pedaleGauche)
    accelBride = bridage(pedaleDroitePourcent,number)
    freinBride = bridage(pedaleGauchePourcent,number)
    #0=reculer / 50=stop / 100=afond
    SPEED = vitessesTo1(accelBride,freinBride,valeursMin,valeursMax)
    #0=gauche / 50=ttdroit / 100=droite
    VOLANT = changerVitesse(int(valeursMin[2]),int(valeursMax[2]),angleVolant)
    #print("speed: ",SPEED,"angle volant: ",VOLANT)S
    #vitesse aux palettes
    vitesse(paletteDroite,paletteGauche)
    
    SPEED = verificationPourcent(SPEED)
    VOLANT = verificationPourcent(VOLANT)
    return SPEED,VOLANT,VITESSE
    
    
    
    
