# Avance(xmm) - Gauche(xmm) - Recule(xmm) - Droite(xmm)
# Fait faire le tour de la zone cible au robot.

import serial
import argparse
import time

ser = serial.Serial("COM5", 19200, timeout = 1)

ser.write("GOxx0640".encode())
ans = ser.readline()
print(ans)

ser.write("LExx0640".encode())
ans = ser.readline()
print(ans)

ser.write("BAxx0640".encode())
ans = ser.readline()
print(ans)

ser.write("RIxx0640".encode())
ans = ser.readline()
print(ans)
time.sleep(1)
ser.write("ST000000".encode())
##ans = ser.readline()
##print(ans)
ser.write("ROR00050".encode())
ans = ser.readline()
print(ans)
time.sleep(1.5)
ser.write("ST000000".encode())
ans = ser.readline()
print(ans)

ser.close()


