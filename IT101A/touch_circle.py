import time
import board
import touchio

import neopixel

touch1 = touchio.TouchIn(board.A1)

pixels = neopixel.NeoPixel(board.NEOPIXEL,10,brightness=0.5) 
pixels.show()

previous = touch1.value
led_pos = 9
pixels[led_pos]=(255,0,255)

while True:
    current = touch1.value
    
    if current and (not previous):
        pixels[led_pos] = (0,0,0)
        led_pos = (led_pos - 1) % 10
        pixels[led_pos] = (255,0,255)
        
    previous = current
        
    time.sleep(0.01)