import math
import numpy

a,b = 2,1
def opgave4(a,b):

    for t in range(0,2*math.pi,0.0001):
        x = a*math.cos(t)
        y = b*math.sin(t)

        