import numpy as np
import math
import matplotlib.pyplot as plt


#a = 0
#b = 1
#N = 10
#width = (b-a)/N


def func(x):
    return  1/(1 + 100*(x-0.5)**2)
    
def riemann(func,a,b,N):
    area = 0
    width = (b-a)/N
    
    for x in np.arange(a,b+width,width):
        y = func(x)
        rect = y * width
        area += rect
    return area


result = riemann(lambda x: x * math.sin(1/x) if x != 0 else 0, 0.001, 0.1, 100000)
print(result) 