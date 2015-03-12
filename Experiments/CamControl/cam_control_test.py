import argparse

import serial


parser = argparse.ArgumentParser()
parser.add_argument('cervo')
parser.add_argument('degree')
args = parser.parse_args()

ser = serial.Serial('/dev/ttyACM0')
ser.write(bytearray([0x84, int(args.cervo), 0x70, int(args.degree)]))
