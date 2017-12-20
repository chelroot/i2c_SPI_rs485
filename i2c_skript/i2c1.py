#! /usr/bin/env python
# coding: utf-8


import smbus, time

bus = smbus.SMBus(1)
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    return number

while True:
  var = str('1')
  bus.write_byte(address, 1)
  time.sleep(1)
#  number = readNumber()


