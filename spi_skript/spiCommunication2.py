#! /usr/bin/env python
# coding: utf-8

# RPi PINOUTS
# MOSI -> GPIO10
# MISO -> GPIO9
# SCK  -> GPIO11
# CE1  -> GPIO7
# CE1  -> GPIO8

# get the GPIO Library and SPI Library
#import RPi.GPIO as GPIO
import spidev
import time

#Initialze the SPI
spi = spidev.SpiDev()
#spi.open(0,0)

def spiRead (aa):
  # spi.open(0,0)
   spiValue = spi.xfer2([8])
   time.sleep(0.05)
 #  spi.close()
   print(spiValue)
   return spiValue



while True:
    spi.open(0,0)
    resp = spi.xfer([0x30,0X0A])
#    spi.close()
#    resp1 = spiRead(1)
    resp = spiRead(0)
    print ("Input Responce = {}".format(resp))
    spi.close()
    time.sleep(0.5)

    spi.open(0,0)
#    spi.open(0,0)
    resp = spi.xfer([0x31,0X0A])
#    spi.close()

#    resp1 = spiRead(1)
    resp = readbytes(1)
    print ("Input = {}".format(resp))
    spi.close()
    time.sleep(0.5)





#End of the Script
