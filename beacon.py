from machine import Timer
from machine import Pin

# " " is element space
# x is character space
# z is word space
BEACON = ". - -x- - - . .x.x- . .x. . -x- . . - .x- . . .z"

WRITE = 0
SPACE = False
x = 0

# Writes to GPIO pin 16
SIGNAL = Pin(16, Pin.OUT)

def checkSignal(input):
    global WRITE
    global SPACE
    global x
    if(WRITE == 0):
        if(BEACON[x] == "."):
            print(".")
            WRITE = 1
            SPACE = False
        if(BEACON[x] == "-"):
            print("-")
            WRITE = 3
            SPACE = False
        if(BEACON[x] == "x"):
            print("x")
            WRITE = 3
            SPACE = True
        if(BEACON[x] == " "):
            print(" ")
            WRITE = 1
            SPACE = True
        if(BEACON[x] == "z"):
            print("Stop here.")
            WRITE = 10
            SPACE = True
        print(x)
        x = x + 1
        if(x == (len(BEACON))):
            x = 0
    writeSignal()
            
def writeSignal():
    global WRITE
    global SPACE
    global SIGNAL
    if(WRITE != 0):
        if(SPACE == True):
            SIGNAL.value(0)
        if(SPACE == False):
            SIGNAL.value(3)
        WRITE = WRITE - 1
