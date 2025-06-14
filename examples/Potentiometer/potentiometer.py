"""
Modified: 9 May 2025
By Maggie Lee

Purpose: Read and output the potentiometer value as a percent.
Notes : Scale from a value to a voltage with (3.3/65535)*adc_value
        
Attributions: https://www.halvorsen.blog/documents/technology/iot/pico/pico_potentiometer.php
"""

from machine import ADC
from time import sleep


def ReadPotentiometer():
    # Set up potentiometer pin
    pot_pin = 26
    pot = ADC(pot_pin)

    # Read potentiometer value
    adc_value = pot.read_u16()

    # Convert into a voltage
    volt = (3.3/65535)*adc_value

    percentPot = ScalePercent(volt)

    return percentPot

# Convert voltage into a percentage of 3.3 V


def ScalePercent(volt):
    percent = (volt/3.3)*100
    return int(percent)


while True:
    potvalue = ReadPotentiometer()
    print(potvalue)
    sleep(1)
