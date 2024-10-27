"""
Created by: Emre Guzel
Created on: Oct 26 2024
This module is a Micro:bit MicroPython programThis program mauseres the disance in sonar
"""

from microbit import *
import neopixel

# Added the sonar libray
class HCSR04:
    # this class abstracts out the functionality of the HC-SR04 and
    #   returns distance in mm
    # Trig: pin 1
    # Echo: pin 2
    def __init__(self, tpin=pin1, epin=pin2, spin=pin13):
        self.trigger_pin = tpin
        self.echo_pin = epin
        self.sclk_pin = spin

    def distance_mm(self):
        spi.init(baudrate=125000, sclk=self.sclk_pin,
                 mosi=self.trigger_pin, miso=self.echo_pin)
        pre = 0
        post = 0
        k = -1
        length = 500
        resp = bytearray(length)
        resp[0] = 0xFF
        spi.write_readinto(resp, resp)
        # find first non zero value
        try:
            i, value = next((ind, v) for ind, v in enumerate(resp) if v)
        except StopIteration:
            i = -1
        if i > 0:
            pre = bin(value).count("1")
        try:
                k, value = next((ind, v)
                                for ind, v in enumerate(resp[i:length - 2]) if resp[i + ind + 1] == 0)
                post = bin(value).count("1") if k else 0
                k = k + i
        except StopIteration:
                i = -1
        dist= -1 if i < 0 else round(((pre + (k - i) * 8. + post) * 8 * 0.172) / 2)
        return dist


# Setting the varibles 
sonar = HCSR04
distance = neopixel.NeoPixel(pin16, 4)

# Setting the screen
display.clear()
display.show(Image.HAPPY)

# Setting up the lights 
distance[0] = (0, 0, 0)
distance[1] = (0, 0, 0)
distance[2] = (0, 0, 0)
distance[3]  =(0, 0, 0)
distance.show()
while True:
    display.show(Image.HEART)
    display.show(sonar.distance_mm()/10)
     
    if button_a.is_pressed():
        if sonar < 10:
            distance[0] = (255, 0, 0)
            distance[1] = (255, 0, 0)
            distance[2] = (255, 0, 0)
            distance[3] = (255, 0, 0)
        else:
            distance[0] = (255, 110, 0)
            distance[1] = (255, 110, 0)
            distance[2] = (255, 110, 0)
            distance[3] = (255, 110, 0)
        distance.show()
