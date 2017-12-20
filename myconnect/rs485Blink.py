#! /usr/bin/env python
# coding: utf-8


import serial, time

ser = serial.Serial("/dev/ttyUSB0")
ser.baudrate = 9600

while True :
  ser.write('Q')
  time.sleep(0.5)
  ser.write('q')
  time.sleep(0.5)

