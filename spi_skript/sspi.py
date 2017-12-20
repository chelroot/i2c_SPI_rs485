#! /usr/bin/env python
# coding: utf-8


# Test code to poll Arduino SPI for data 100 times a second
# This requires https://github.com/WiringPi/WiringPi2-Python
# See also http://wiringpi.com/
# sudo modprobe spi_bcm2708 before you run this or unblacklist 
# http://www.raspberrypi.org/phpBB3/viewtopic.php?p=302061#p302061

# Arduino  <  >     PI
# 11                MOSI
# 12                MISO
# 13                SCLK
# DO NOT FORGET 3.3V <> 5V bi-directional level convert to avoid fried pi

# Jonathan H 11/09/2013

import wiringpi2
import sys
import Tkinter as tki # tkinter in Python 3
from time import sleep
print sys.version

wiringpi2.wiringPiSPISetup(1,2000000) #2MHZ = SPI_CLOCK_DIV8; (16Mhz/8)

# Class to replace missing switch/case functionality 
# http://code.activestate.com/recipes/410692/
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration
    
    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

# "I would like to have four horizontal buttons in one row."
# Answer #1 from http://stackoverflow.com/questions/10178652/

root = tki.Tk()
root.title("Button Monitor")

frm = tki.Frame(root, bd=4)
frm.grid()

var = tki.StringVar()

left = tki.Radiobutton(frm, text='left', variable=var, state='disabled')
left.config(indicatoron=0, bd=4, width=12, value='left')
left.grid(row=0, column=0)

middle = tki.Radiobutton(frm, text='middle', variable=var)
middle.config(indicatoron=0, bd=4, width=12, value='middle', state='disabled')
middle.grid(row=0, column=1)

right = tki.Radiobutton(frm, text='right', variable=var)
right.config(indicatoron=0, bd=4, width=12, value='right', state='disabled')
right.grid(row=0, column=2)

def doActions(hexdata):    
# See http://www.asciitable.com/
# DEFAULT 03 LEFT: 13 MID: 0b RIGHT: 07 L+M 1b R+M: 0f
    for case in switch(hexdata):
        if case('03'): # default, could also just omit condition or 'if True'
            #print hexdata
            middle.config(state='disabled')
            right.config(state='disabled')
            left.config(state='disabled')
            break
         # No need to break here, it'll stop anyway        
        if case('13'):
            #print ("left")
            left.config(state='normal')
            break
        if case('0b'):
            #print "middle"
            middle.config(state='normal')
            break
        if case('07'):
            #print "right"
            right.config(state='normal')
            break
        if case('1b'):
            #print "left+middle"
            left.config(state='normal')
            middle.config(state='normal')
            break
        if case('0f'):
            right.config(state='normal')
            middle.config(state='normal')            
            #print "right and middle"
            break      
        if case(): # default, could also just omit condition or 'if True'
            print hexdata
         # No need to break here, it'll stop anyway

def task():
    
    # Doesn't matter WHAT this is, it's just dummy data to poll the slave MCU
    myData = 'A'    # 0x41 in hex
    
    # Because SPI recevies a byte when it sends, for some reason I found you 
    # need to send TWO calls oherwise you get into a "ping pong" scenario 
    wiringpi2.wiringPiSPIDataRW(1,myData)
    wiringpi2.wiringPiSPIDataRW(1,myData)

    # Turn the data into something we can use
    # http://stackoverflow.com/questions/1916928/
    hexdata = ''.join('%02x' % ord(byte) for byte in myData)
    doActions(hexdata)
    
    ## How do you run your own code alongside Tkinter's event loop?
    ## http://stackoverflow.com/questions/459083/
    root.after(10,task)  # reschedule event 100 times per second

root.after(10,task)
root.mainloop()
