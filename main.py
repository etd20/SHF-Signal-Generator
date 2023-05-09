from machine import Timer
from beacon import checkSignal

if __name__ == '__main__':
    print("Running Program")
    # Create a virtual timer
    timer=Timer(-1)
    # Every 100 ms, call checkSignal from beacon.py
    timer=Timer(period=100, mode=Timer.PERIODIC, callback=checkSignal)