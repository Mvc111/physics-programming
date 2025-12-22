import random
import numpy as np
import math
import matplotlib.pyplot as plt




def montecarlo(func,x1,y1,x2,y2):
    total = 0

    p = 100000
    for i in range(0,p):

        x = random.uniform(x1,x2)
        y = random.uniform(y1,y2)

        if func(x) > 0 and 0 < y <= func(x) :
            total +=1
        elif func(x) < 0 and func(x) <= y <= 0:  
            total -=1   

     

    area = (total/p)*((x2-x1)*(y2-y1))


    return area     









    