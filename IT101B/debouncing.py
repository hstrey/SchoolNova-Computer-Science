import board
import digitalio
from adafruit_debouncer import Debouncer
 
button = digitalio.DigitalInOut(board.BUTTON_A)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.DOWN
switch = Debouncer(button)

while True:
    switch.update()
    

    if switch.fell:
        print('Just released')
        
    if switch.rose:
        print('Just pressed')