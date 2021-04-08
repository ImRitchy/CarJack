#MCP4728 module: i2c to variable current on 4 channels

import board
import busio
import adafruit_mcp4728
from time import sleep

i2c = busio.I2C(board.SCL, board.SDA)
mcp4728 =  adafruit_mcp4728.MCP4728(i2c)

mcp4728.channel_a.value = 32678# int(65535/4) # Voltage = VDD
mcp4728.channel_b.value = 32678# int(65535/2) # VDD/2
mcp4728.channel_c.value = 32678# int(65535/4) # VDD/4
mcp4728.channel_d.value = 32678# 0V

mcp4728.save_settings() # save the current values to the eeprom,making them the default on power up


def controlVoiture(vitesse, volant): #0-100
    #print("vitesse", vitesse, "volant", volant)
    value = int(vitesse * 65535 / 100)
    mcp4728.channel_a.value = value
    value = int(volant * 65535 / 100)
    mcp4728.channel_b.value = value
    mcp4728.save_settings()

'''
sleep(2)
for i in range(655):
    mcp4728.channel_a.value = int(i*100)
    mcp4728.save_settings()
'''

'''
while True:
    percent = int(input('Vert Speed 0-100: '))
    value = int(percent * 65535 / 100)
    print(value)
    mcp4728.channel_a.value = int(value)
    mcp4728.save_settings()

    percent = int(input('Jaune Direction 0-100: '))
    value = int(percent * 65535 / 100)
    print(value)
    mcp4728.channel_b.value = int(value)
    mcp4728.save_settings()

'''