from gpiozero import LED
from time import sleep

back = LED(14)
right = LED(15)

FACTOR = 2

def move_wrapper(distance): 
    if(distance < 0):
        back.on()
        right.off()
        sleep(-distance * FACTOR)
        back.off()
    else:
        right.on()
        back.off()
        sleep(distance*FACTOR)
        right.off()
