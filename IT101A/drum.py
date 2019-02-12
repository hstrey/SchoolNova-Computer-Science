import time
import board
import touchio
import audioio
from digitalio import DigitalInOut, Direction

# enable the speaker
spkrenable = DigitalInOut(board.SPEAKER_ENABLE)
spkrenable.direction = Direction.OUTPUT
spkrenable.value = True

touch1 = touchio.TouchIn(board.A1)

a = audioio.AudioOut(board.A0)

previous = touch1.value
 
def play_file(filename):
    print("playing file " + filename)
    f = open(filename, "rb")
    wave = audioio.WaveFile(f)
    a.play(wave)

while True:
    play_file('drumSamples/bd_tek.wav')
        
#    previous = current
        
    time.sleep(1)