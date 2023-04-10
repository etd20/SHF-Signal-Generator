from machine import Timer
from beacon import checkSignal

if __name__ == '__main__':
    print("Running Program")
    timer=Timer(-1)
    timer=Timer(period=100, mode=Timer.PERIODIC, callback=checkSignal)