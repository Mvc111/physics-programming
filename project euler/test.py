import random
import math

# def opgave5():


#     d = 0
#     n = 100000000
#     f12 = 0
#     f89 = 0


#     for i in range(n):
#         x1 = random.random()
#         x2 = random.random()
#         p = x1 - x2
#         if p > 0:
#             d += p 
#         else: 
#             d -= p    

#         if 0.1< p < 0.2 or 0.1< -1*p < 0.2   :
#             f12 += 1
#         if 0.8 < p < 0.9 or 0.8 < -1*p < 0.9 :
#             f89 += 1

#     averaged = d/n
#     averagef = f12/f89
#     return averaged , averagef

# print(opgave5())


# def opgave5():
#     good = 0
#     bad = 0
#     N = 1000000
#     for i in range(N):
        

#         x1 = random.random()*math.pi
#         y1 = random.random()*7

#         f = (x1**x1)*math.sin(x1) 
#         g = 4*math.sin(x1)

#         if y1 > g and y1 < f and x1 > 2 and x1 < math.pi:
#             good += 1
#         else :
#             bad += 1
#     ratio = (good/(good + bad))*7*math.pi

#     return    ratio

# print(opgave5())


def opgave1():

    L = [10,1299,23,12,4,99,100,36,48,120]
    tf = []
    tfn = []
    for i in range(len(L)):
        if L[i] % 3 ==0 and L[i] % 4 ==0 :
            tf.append(L[i])
            if L[i] % 5 != 0:
                tfn.append(L[i])            

    return tf , tfn

print(opgave1())