#! /usr/bin/env python
# coding: utf-8


import smbus, time

bus = smbus.SMBus(1)
address = 0x04

while True:
  try:
    bus.write_byte(address, 1)
  except:
    pass
  time.sleep(0.15)
  try:
    bus.write_byte(address, 0)
  except:
    pass
  time.sleep(0.15)


