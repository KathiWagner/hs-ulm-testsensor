#!/usr/bin/env python

import random
#import matplotlib.pyplot as plt


data = open('/root/lmic_pi/grab-and-send/measurement.txt', "w")
people = []
people_hex =[]
time_sec= [0,60,120,180,240, 300, 360]#range(0,240,60) # in sec
for x in range(len(time_sec)):
    a = random.randint(1,201)
    people.append(a)
    people_hex.append(hex(a))
    b= str(time_sec[x])+ ' ' + str(a)
    data.write(str(time_sec[x]))
    data.write(' ')
    data.write(hex(a))
    data.write('\n')

data.close()

#print(time_sec,people)
#print(people_hex)
#plt.plot(time_sec,people)
#plt.show()



