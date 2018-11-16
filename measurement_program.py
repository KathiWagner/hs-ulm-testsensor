#!/usr/bin/env python

import random
import time

data = open('/root/lmic_pi/examples/grab-and-send/measurement.txt', "w")
people = []
people_hex =[]
time_sec= [0,60,120,180,240, 300, 360]#range(0,240,60) # in sec
for x in range(len(time_sec)):
    data = open('/root/lmic_pi/examples/grab-and-send/measurement.txt', "w")
    a = random.randint(1,201)
    data.write(str(time_sec[x]))
    data.write(' ')
    data.write(hex(a))
    data.close()
    time.sleep(1)




