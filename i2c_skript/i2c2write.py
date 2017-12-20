#! /usr/bin/env python
# coding: utf-8


import smbus, time

bus = smbus.SMBus(1)
address = 0x04
number1 = 1000
while True:
#  try:
#    bus.write_byte(address, 1)
#    number = bus.read_byte(address)
#    print "Arduino: Hey RPI, I received a digit ", number
#    print
#  except:
#    pass
#  time.sleep(1.15)

  try:
#    bus.write_byte(address, 0)
    number = bus.read_byte(address)
    if number == number1:
       pass
    else:
       print "Arduino:", number
       print
       number1 = number
  except:
    pass
  time.sleep(0.15)


