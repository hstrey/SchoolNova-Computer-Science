# Write your code here :-)
import time
import digitalio
import adafruit_thermistor
import board
import neopixel

thermistor = adafruit_thermistor.Thermistor(
    board.TEMPERATURE, 10000, 10000, 25, 3950)

pixels = neopixel.NeoPixel(board.NEOPIXEL,10,brightness=0.1)
pixels.fill((0,0,0))
pixels.show()

t_max=27
t_min=24

def red(temp):
    r= 255/(t_max-t_min)*(temp-t_min)
    if r>255:
        r=255
    if r<0:
        r=0
    return int(r)
    
def blue(temp):
    b= -255/(t_max-t_min)*(temp-t_max)
    if b>255:
        b=255
    if b<0:
        b=0 
    return int(b)
    
def angle(temp):
    a = -9/(t_max-t_min)*(temp-t_max)
    if a<0:
        a = 0
    elif a>9:
        a=9
    return round(a)

while True:
    temp_c = thermistor.temperature
    print(temp_c,red(temp_c),blue(temp_c))
    for i in range(angle(temp_c),10):
        pixels[i] = (red(temp_c),0,blue(temp_c))
    for i in range(angle(temp_c)):
        pixels[i]=(0,0,0)
    time.sleep(0.25)