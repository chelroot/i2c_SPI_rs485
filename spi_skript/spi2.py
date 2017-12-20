#! /usr/bin/env python
# coding: utf-8


# http://robsraspberrypi.blogspot.ru/2016/01/raspberry-pi-adding-more-outputs-using.html

#SPI_MOSI  = GRIO 10  На обе микросхемы - третья нога слева (между первым выходом и землей)
##// MOSI — выход ведущего, вход ведомого (англ. Master Out Slave In). Служит для передачи данных от ведущего устройства ведомому. 
## третья нога 

#SPI_CLK  = GRIO 11 -  6 нога микросхемы  - на обе микросжемы

#SPI_CE0_N  = GRIO 08 -  5 нога микросхемы  на 1 микросжему
#SPI_CE1_N  = GRIO 07 -  5 нога микросхемы  на 2 микросжемy


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
    resp = spiWrite(1,A)   #Тут задаются каналы - канал 1
    resp = spiWrite(0,A)   #тут задаются каналы - канал 0
    A=A+1
    if (A>254):

        A=0
