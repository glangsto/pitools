# python to get my ip and send an email to megajansky
import os

myiptemp = "/tmp/myip"
os.system( '/home/pi/bin/myip | head -1 > /tmp/myip')

with open(myiptemp, "r") as f:
    for line in f:
        ipparts = str(line)

f.close()

parts = ipparts.split('\n')
myip = parts[0]
#print ("My IP: %s" % (myip))
# 
ipparts = "/tmp/myip." + myip

parts = ipparts.split('\n')
ipfile = parts[0]
#now write ip to a temp file

who = "megajansky@gmail.com"
mailip = 'mail -s "Pi ip: %s" %s < %s' % (myip, who, myiptemp)

print(" Mail command: %s" % mailip)
os.system( mailip)

