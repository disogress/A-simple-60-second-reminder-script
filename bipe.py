import time
import winsound
import platform

def beep():
    frequency = 440
    duration = 200
    winsound.Beep(frequency, duration)

while True:
    time.sleep(60)
    beep()
