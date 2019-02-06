import time
import touchio
import board

import neopixel

touch1 = touchio.TouchIn(board.A1)

pixels = neopixel.NeoPixel(board.NEOPIXEL,10,brightness=0.5)

previous = touch1.value

led_state = False

while True:
    current = touch1.value
    
    if (current and (not previous)):
        led_state = not led_state
        
    if led_state:
        pixels[1] = (255,0,255)
    else:
        pixels[1] = (0,0,0)
        
    previous = current
    
    time.sleep(0.1)