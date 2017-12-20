#! /usr/bin/env python
# coding: utf-8

import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

newData = False
state   = False

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

while True:
    if (state != state) :
      state = number
      newData = true

#    var = input("")
#    if not var:
#        continue

#    writeNumber(var)

    if (readNumber() > 0):
       number = readNumber()
       aa = ('sostoyanie = ' +  str(number) + '\n')
       print(aa)
    else:
       pass