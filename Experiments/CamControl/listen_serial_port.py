import serial

ser = serial.Serial('/dev/ttyUSB0', baudrate=19200, timeout=None)

while 1:
    print(ser.readline())
