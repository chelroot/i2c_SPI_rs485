#! /usr/bin/env python
# coding: utf-8

# http://robsraspberrypi.blogspot.ru/2016/01/raspberry-pi-adding-more-inputs-using.html

#SPI_MIS0  = GRIO 09  # восьмая нога первый ряд

#SPI_CLK  = GRIO 11 -  2 нога микросхемы  - на обе микросжемы

#SPI_CE0_N  = GRIO 08 -  1 нога микросхемы  на 1 микросжему
#SPI_CE1_N  = GRIO 07 -  1 нога микросхемы  на 2 микросжемy



import spidev
import time

spi = spidev.SpiDev()

def spiRead (channel):
   spi.open(0,channel)
   spiValue = spi.xfer2([1])
   time.sleep(0.05)
   spi.close()
   return spiValue

while True :
   resp = spiRead(1)
   resp = spiRead(0)
   print ("Input Responce = {}".format(resp))
