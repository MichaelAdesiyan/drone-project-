import serial
import time

ser = serial.Serial(port='COM18', baudrate=9600, timeout=.1)
time.sleep(3)

while(1):
    def getValues_1():
        userInput = input()
        if userInput == "S":
            time.sleep(.1)
            ser.write(b'S')
        elif userInput == "L":
            time.sleep(.1)
            ser.write(b'L')
        elif userInput == "D":
            time.sleep(.1)
            ser.write(b'D')
        elif userInput == "F":
            time.sleep(.1)
            ser.write(b'F')
        elif userInput == "B":
            time.sleep(.1)
            ser.write(b'B')
        elif userInput == "R":
            time.sleep(.1)
            ser.write(b'R')
        elif userInput == "L":
            time.sleep(.1)
            ser.write(b'L')
        elif userInput == "C":
            time.sleep(.1)
            ser.write(b'C')
        elif userInput == "W":
            time.sleep(.1)
            ser.write(b'W')
    getValues_1()
