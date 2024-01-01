#
# Program to read Roll pitch and yaw data from a pi pico
# and plot them as realtime strip chards
# HISTORY
# 24Jan01 GIL Initial version
from matplotlib import pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 
import time

# initializing a figure in 
# which the graph will be plotted 
fig, (ax1, ax2, ax3)  = plt.subplots( 3, 1, figsize=(10,6)) 

# marking the x-axis and y-axis 
NKEEP = 30
ax1.set_xlim( 0, NKEEP)
ax2.set_xlim( 0, NKEEP)
ax3.set_xlim( 0, NKEEP)
ax1.set_ylabel("Yaw")
ax2.set_ylabel("Pitch")
ax3.set_ylabel("Roll")

#axis = plt.axes(xlim =(0, NKEEP), ylim =(0, 180)) 

# initalize two line objects (one in each axes)
line1, = ax1.plot([], [], lw=2)
line2, = ax2.plot([], [], lw=2, color='r')
line3, = ax3.plot([], [], lw=2)
line = [line1, line2, line3]

xs = np.linspace( 0, NKEEP, NKEEP)
ys = np.linspace( 0, 1, NKEEP)
rs = np.linspace( 0, 1, NKEEP)
ps = np.linspace( 0, 1, NKEEP)
#
#count the number of values read
n = 0

doTest = True
doTest = False

lasty = 0.
lastDy = 0.
lastp = 0.
lastDp = 0.
lastr = 0.
lastDr = 0.

# data which the line will 
# contain (x, y) 
def init():
        line = [line1, line2, line3]
        return line, 

opened = False
if not doTest:
        try:
                f = open("/dev/ttyACM0","r")
                opened = True
        except:
                print("Could not read roll,pitch and Yaw")
                # Read temperature (Celsius) from TMP102
        
def getRPY():
        """
        Get a single new Y value
        """
        oneRPY = "RPY = 139.92 -14.66 141.23"
        rValue = 139.92
        pValue = -14.66
        yValue = 141.23    

        if not doTest:
                oneRPY = f.readline()

        roll = oneRPY.split("=")
        rpyStr = roll[1].strip()
        rpyValues = rpyStr.split(" ")
        rValue = float(rpyValues[0])
        pValue = float(rpyValues[1])
        yValue = float(rpyValues[2])
        if doTest:
                yValue = yValue + 10. * np.random.rand()
                time.sleep(.1)
        return rValue, pValue, yValue

def animate(i):
        # function to animate rolls
        global n
        global ys, ps, rs
        global xs
        global lasty, lastp, lastr
        global lastDy, lastDp, lastDr
        global line
        global ax1, ax2
        #
        ar, ap, ay = getRPY()
        # plots a sine graph
        if n < NKEEP:
                ys[n] = ay
                ps[n] = ap
                rs[n] = ar
                if n < 10:
                        print("RPY = %.2f, %.2f, %.2f" % (ar, ap, ay))
                n = n + 1
        else:
                #shift all values to the left
                ys[0:n-1] = ys[1:n]
                ys[n-1] = ay
                ps[0:n-1] = ps[1:n]
                ps[n-1] = ap
                rs[0:n-1] = rs[1:n]
                rs[n-1] = ar
                
        y = ys[0:n]
        p = ps[0:n]
        r = rs[0:n]
        x = xs[0:n]

        ymin = min(y)
        ymax = max(y)
        yave = (ymin+ymax)/2.
        yave = int(yave)
        dy = (ymax - ymin)
        dy = 1.5*(int(dy/2.) + 1.)
        
        if yave != lasty or dy != lastDy:
                ax1.set_ylim( yave-dy, yave+dy, auto=True)
                lasty = yave
                lastDy = dy
                
        pmin = min(p)
        pmax = max(p)
        pave = (pmin+pmax)/2.
        pave = int(pave)
        dp = (pmax - pmin)
        dp = 1.5*(int(dp/2.) + 1.)
        
        if pave != lastp or dp != lastDp:
                ax2.set_ylim( pave-dp, pave+dp, auto=True)
                lastp = pave
                lastDp = dp
                fig.canvas.resize_event()
                
        rmin = min(r)
        rmax = max(r)
        rave = (rmin+rmax)/2.
        rave = int(rave)
        dr = (rmax - rmin)
        dr = 1.5*(int(dr/2.) + 1.)
        
        if rave != lastr or dr != lastDr:
                ax3.set_ylim( rave-dr, rave+dr, auto=True)
                lastr = rave
                lastDr = dr
                fig.canvas.resize_event()
                
        line[0].set_data(x, y) 
        line[1].set_data(x, p) 
        line[2].set_data(x, r) 
#        line = [line[0], line[1], line[2]]
        return line,

anim = FuncAnimation(fig, animate, 
					init_func = init, 
					frames = 200, 
					interval = 20, 
					blit = False) 

#anim.save('continuousSineWave.mp4', 
#		writer = 'ffmpeg', fps = 30)
plt.show()
