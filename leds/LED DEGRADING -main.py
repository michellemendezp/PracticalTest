
from microbit import *
import neopixel
from random import randint
red=1
green=0
blue=0

np = neopixel.NeoPixel(pin2, 12)
ineos=12
while True:
    for pixel_id in range(0, len(np)): 
        red = red+1 
        #green = green+1
        #blue = blue+1
        if red > 100: red = 0
        if green > 100: green = 0
        if blue > 100: blue = 0
        np[pixel_id] = (red, green, blue)    
        np.show()
        sleep(300)


