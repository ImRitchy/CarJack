from lectureVolant import *
import math


def bridage(speed,mode,VITESSE):
    #speed = -speed+100
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
    return speed
    #return -speed-100

def vitesse(paletteD,paletteG,VITESSE,etatBoutonVitesse):
    #c'est surement bancal, avant on avait un global, la variable sert a ne pas spam les passages de vitesse
    if paletteD !=0 or paletteG != 0:
        etatBoutonVitesse +=1
    if paletteD == 0 and paletteG == 0:
        etatBoutonVitesse = 0 
    if etatBoutonVitesse == 1:
        
        if int(paletteD) != 0:
            if VITESSE < 3 :
                VITESSE += 1
        if int(paletteG) != 0:
            if VITESSE > 0:
                VITESSE -= 1
        print("vous êtes en: ",VITESSE)
    return VITESSE,etatBoutonVitesse
        
        
    

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
    #print(vitesseDroite,vitesseGauche,mini,maxi)
    vitesseDroite = 50 -vitesseDroite/2
    vitesseGauche =  vitesseGauche/2
    #print(vitesseDroite,vitesseGauche)
    spid = int(vitesseGauche + vitesseDroite)
    return spid

#fonction qui tranfsorme les valeurs en pourcentage
def changerVitesse(mini,maxi,value):
    #print(value)
    if (maxi-mini) != 0 :
        #print(int((value - mini)*100/(maxi-mini)))
        return int((value - mini)*100/(maxi-mini))


def modExp(SpeedPourcentage):
    Speed=SpeedPourcentage
    if Speed==0:
        return Speed
    if Speed>0:
        Speed+=4
        Speed=math.exp(Speed)
        Speed=int(Speed)
        Speed-=54
        Speed=Speed*1.05
        Speed=int(Speed)
        return Speed
    if Speed<0:
        Speed=-Speed
        Speed+=4
        Speed=math.exp(Speed)
        Speed=int(Speed)
        Speed-=54
        Speed=Speed*1.05
        Speed=int(Speed)
        Speed=-Speed
        return Speed
    else: # A ENLEVER UNE FOIS QUE C'EST DEBUG
        print("erreur")
    
    
    
def modLog(SpeedPourcentage):
    Speed=SpeedPourcentage
    if Speed==0:
        return Speed
    if Speed>0:
        Speed+=1
        Speed=math.log(Speed)
        Speed=Speed*144
        Speed=int(Speed)
        return Speed
    if Speed<0:
        Speed=-Speed
        Speed+=1
        Speed=math.log(Speed)
        Speed=Speed*144
        Speed=int(Speed)
        Speed=-Speed
        return Speed
    else: # A ENLEVER UNE FOIS QUE C'EST DEBUG
        print("erreur")



def mainModificationValeurs(number,gamepad,self,VITESSE,etat):
    #global VITESSE
    angleVolant = self.getAngleVolant()
    
    pedaleDroite = self.getVitessePedaleDroite()
    pedaleGauche = self.getVitessePedaleGauche()
    paletteDroite = self.getPaletteDroite()
    paletteGauche = self.getPaletteGauche()
    valeursMax = self.getMaximums() #liste: [pedaleD,pedaleG,volant]
    valeursMin = self.getMinimums()
    pedaleDroitePourcent=changerVitesse(int(valeursMin[0]),int(valeursMax[0]),pedaleDroite)
    pedaleGauchePourcent=changerVitesse(int(valeursMin[1]),int(valeursMax[1]),pedaleGauche)
    accelBride = bridage(pedaleDroitePourcent,number,VITESSE)
    freinBride = bridage(pedaleGauchePourcent,number,VITESSE)
    #0=reculer / 50=stop / 100=afond
    SPEED = vitessesTo1(accelBride,freinBride,valeursMin,valeursMax)
    #print(gamepad,SPEED)
    #0=gauche / 50=ttdroit / 100=droite
    VOLANT = changerVitesse(int(valeursMin[2]),int(valeursMax[2]),angleVolant)
    #print("speed: ",SPEED,"angle volant: ",VOLANT)S
    #vitesse aux palettes
    vitesseETetat = vitesse(paletteDroite,paletteGauche,VITESSE,etat)
    #print(SPEED)
    SPEED = verificationPourcent(SPEED)
    VOLANT = verificationPourcent(VOLANT)
    #sprint(SPEED,VOLANT)
    return SPEED,VOLANT,vitesseETetat
    
    
    
    
