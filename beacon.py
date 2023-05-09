from machine import Timer
from machine import Pin

# " " is element space
# x is character space
# z is word space
# Message is W8EDU-B
BEACON = ". - -x- - - . .x.x- . .x. . -x- . . - .x- . . .z"

# Number of times to write a high/low signal (in periods of 100 ms)
WRITE = 0
# Should the written element be a space (low signal)
SPACE = False
# Spot in iteration of beacon message
x = 0

# Writes to GPIO pin 16
SIGNAL = Pin(16, Pin.OUT)

# Writes a high/low signal based on BEACON
def checkSignal(input):
    global WRITE
    global SPACE
    global x
    # If we have finished the previous write
    if(WRITE == 0):
        # If the Beacon message is a .
        if(BEACON[x] == "."):
            print(".")
            # Write for 1 period
            WRITE = 1
            # Not a space
            SPACE = False
        # If the Beacon is a -
        if(BEACON[x] == "-"):
            print("-")
            # Write for 3 periods
            WRITE = 3
            # Not a space
            SPACE = False
        # IF the beacon is an x
        if(BEACON[x] == "x"):
            print("x")
            # Write for 3 periods
            WRITE = 3
            # Is a space
            SPACE = True
        # If the beacon is a space
        if(BEACON[x] == " "):
            print(" ")
            # Write for 1 period
            WRITE = 1
            # Is a space
            SPACE = True
        # If the beacon is a z
        if(BEACON[x] == "z"):
            print("Stop here.")
            # Write for 10 periods (ends message)
            WRITE = 10
            # Is a space
            SPACE = True
        print(x)
        # Increment x by one
        x = x + 1
        # If x is the length of the message
        if(x == (len(BEACON))):
            # Set to 0
            x = 0
    # Write the signal
    writeSignal()
            
def writeSignal():
    global WRITE
    global SPACE
    global SIGNAL
    # If write is not 0
    if(WRITE != 0):
        # If the beacon is a space
        if(SPACE == True):
            # Write low
            SIGNAL.value(0)
        # If the beacon is not a space
        if(SPACE == False):
            # Write high
            SIGNAL.value(3)
        # Decrement the write counter by one
        WRITE = WRITE - 1
