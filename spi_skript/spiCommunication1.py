#! /usr/bin/env python
# coding: utf-8

# RPi PINOUTS
# MOSI -> GPIO10
# MISO -> GPIO9
# SCK  -> GPIO11
# CE1  -> GPIO7
# CE1  -> GPIO8

import spidev
import time

#Initialze the SPI
spi = spidev.SpiDev()
spi.open(0,0)

while True:
    resp = spi.xfer([0x30,0X0A])
    time.sleep(0.5)

    resp = spi.xfer([0x31,0X0A])
    time.sleep(0.5)

