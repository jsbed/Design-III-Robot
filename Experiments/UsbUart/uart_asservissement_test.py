# Avance(2sec) - Gauche(2sec) - Recule(2sec) - Droite(2sec)
# Marche avec les LEDs, prochain test : 4roues + asservissement vitesse.

import serial
import argparse
import time

ser = serial.Serial("COM5", 19200, timeout = 1)

ser.write("GO002002".encode())
ans = ser.readline()
print(ans)
time.sleep(2)
ser.write("LE002002".encode())
ans = ser.readline()
print(ans)
time.sleep(2)
ser.write("BA002002".encode())
ans = ser.readline()
print(ans)
time.sleep(2)
ser.write("RI002002".encode())
ans = ser.readline()
print(ans)
time.sleep(2)
ser.write("ST000000".encode())
ans = ser.readline()
print(ans)

ser.close()
