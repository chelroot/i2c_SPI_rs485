#! /usr/bin/env python
# coding: utf-8


import spidev
import time

spi = spidev.SpiDev()
A=0
def spiWrite(channel,OutValue):
    spi.open(0,channel) # Port 0 , Chip Select 1
    spiValue = spi.xfer2([0,OutValue])
    time.sleep(0.05)
    spi.close()
    return spiValue

while True:
    print ("Output Value = {}".format(A))
    resp = spiWrite(1,A)
    resp = spiWrite(0,A)
    A=A+1
    if (A>1024):

        A=0
