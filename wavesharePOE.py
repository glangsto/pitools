# python file to show IP address on the waveshare LCD displayo 
import time
import sys
import os

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging

from waveshare_POE_HAT_B import POE_HAT_B

logging.basicConfig(level=logging.INFO)

POE = POE_HAT_B.POE_HAT_B()

count = 0

try:  
    while(1):
        POE.POE_HAT_Display(43)
        if count < 10:
            time.sleep(1)
            
            POE.POE_HAT_String("National Science Foundation")
            time.sleep(1)
            count = count + 1
        else:
            time.sleep(60)
        
except KeyboardInterrupt:    
    print("ctrl + c:")
    POE.FAN_ON()
