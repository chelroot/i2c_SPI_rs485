#! /usr/bin/env python
# coding: utf-8


import smbus, time

bus = smbus.SMBus(1)
address = 0x27

while True:
  try:
#    bus.write_byte(address, 0xEF)
     bus.write_byte(address, 2)
#@     bus.write_byte(address, 2)
#     bus.write_byte(address, 3)
#     bus.write_byte(address, 4)
  except:
    pass
  time.sleep(0.55)
  try:
    bus.write_byte(address, 0)
  except:
    pass
  time.sleep(0.55)


