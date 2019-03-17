import time
import board
import touchio
import neopixel

pixels = neopixel.NeoPixel(board.NEOPIXEL,10,brightness=0.5)
pixels.fill((0,0,0))
pixels.show()

touch1 = touchio.TouchIn(board.A1)
touch2 = touchio.TouchIn(board.A2)
touch3 = touchio.TouchIn(board.A3)
touch4 = touchio.TouchIn(board.A4)
touchR = touchio.TouchIn(board.A5)

password = [3,2,2,1]
guess = []

while True:
    if touchR.value:
        guess = []
        pixels.fill((0,0,0))
    elif touch1.value:
        guess.append(1)
    elif touch2.value:
        guess.append(2)
    elif touch3.value:
        guess.append(3)
    elif touch4.value:
        guess.append(4)
    
    print(guess)
    guesses = len(guess)
    if guesses >0:
        pixels[guesses-1] = (255,255,255)
    
    if guesses == 4:
        if password == guess:
            print("you guessed correctly")
            while True:
                pixels.fill((0,255,0))
                time.sleep(0.2)
                pixels.fill((0,0,0))
                time.sleep(0.2)
        else:
            print("you are wrong!")
            guess = []
            pixels.fill((0,0,0))    
    time.sleep(0.5)