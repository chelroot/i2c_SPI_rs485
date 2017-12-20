#! /usr/bin/env python
# coding: utf-8

# RPi PINOUTS
# MOSI -> GPIO10
# MISO -> GPIO9
# SCK  -> GPIO11
# CE1  -> GPIO7
# CE1  -> GPIO8

# get the GPIO Library and SPI Library
import RPi.GPIO as GPIO
import spidev
import time

#GPIO Constants 
chip_change = 2
led_data = 3

# setup the pins as output and input as needed
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(chip_change, GPIO.IN)
GPIO.setup(led_data, GPIO.IN)

#Initialze the SPI 
spi = spidev.SpiDev()
spi_2 = spidev.SpiDev()

#Varialbes for the Debounce 
upPressed = 0
upCompletePress = 0
upReleased = 0
downPressed = 301
downReleased = 0
downCompletePress = 0

buttonFlag = 0
ledFlag = 0
ledFlag_2 = 0
boardSelected = 0

try:
    while True:
	if GPIO.input(led_data):
	    if downPressed < 350:
		downPressed += 1
		if downPressed >= 300 and downCompletePress == 1:
		    downCompletePress = 0
		    downReleased = 0

		    spi.open(0,1)
		    if ledFlag == 0:
		      resp = spi.xfer([0x30,0X0A])
		      ledFlag = 1
		    else:	
		      resp = spi.xfer([0x31,0X0A])
		      ledFlag = 0
		    spi.close()			


	else:
	    if downReleased < 350:
		downReleased += 1
		if downReleased >= 300 and downCompletePress == 0:
		    downPressed = 0
		    downCompletePress = 1 

	    
except KeyboardInterrupt:
    # Ctrl+C pressed, so...
    spi.close()
    spi_2.close()

#End of the Script
