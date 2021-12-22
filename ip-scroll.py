#!/usr/bin/python
import os
from sense_hat import SenseHat

myiptemp = "/tmp/myip"
os.system( "/home/pi/bin/myip | head -1 > %s" % (myiptemp))
    # read all the ip addresses
with open(myiptemp, "r") as f:
    for line in f:
        ipparts = str(line)

f.close()

parts = ipparts.split('\n')
myip = parts[0]














sense = SenseHat()
sense.set_rotation(180)
red = (255, 0, 0)
purple = (255, 0, 255)

sense.show_message("One small step for Pi!", text_colour=purple)
