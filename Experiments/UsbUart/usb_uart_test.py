import serial
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command')
##parser.add_argument('arg1')
##parser.add_argument('arg2')
##parser.add_argument('arg3')
##parser.add_argument('arg4')
##parser.add_argument('arg5')
##parser.add_argument('arg6')
##parser.add_argument('arg7')
##
args = parser.parse_args()

ser = serial.Serial("COM5", 19200, timeout = 1)
ser.write((args.command).encode())

