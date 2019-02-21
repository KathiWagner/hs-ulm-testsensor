#!/usr/bin/env python

import random
import time

time_sec = range(0,10000000,60) # in sec
for x in range(len(time_sec)):
    data = open('/root/lmic_pi/examples/grab-and-send/measurement.txt', "w")
    #a = random.randint(1,201)
    a = 100
    data.write(str(time_sec[x]))
    data.write(' ')
    data.write(hex(a))
    data.close()
    time.sleep(1)




