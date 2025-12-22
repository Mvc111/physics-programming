import random

N = 1000000

def vierkant(N):       
    total = 0
    for i in range(N):
        x1 = random.random()
        x2 = random.random()
        y1 = random.random()
        y2 = random.random()
        distance = ((x2-x1)**2+(y2-y1)**2)**0.5
        total += distance
    return total/N





average = vierkant(N)
print(average)
