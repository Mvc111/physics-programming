
#  def euler():
#     even = []
#     odd = []
#     for n in range(906000):
#         if n**2 % 2 == 0:
#             even.append(n**2)
#         else:
#             odd.append(n**2)

#     return sum(even) , sum(odd)                

# def multiples35():
#     m35 = []
#     for n in range(1000):
#         if n % 3 == 0:
#             m35.append(n) 
#         elif n % 5 == 0:
#             m35.append(n)
#     return sum(m35)        

# #print(multiples35())

# def evenfibbonacci():
#     fibbonacci = [1]
#     efib = []
    
#     for n in range(100):  
#             fn = fibbonacci[n] + fibbonacci[n-1]   
#             fibbonacci.append(fn)

#             if fn % 2 == 0 :
#                 fp = fn
                

#                 if sum(efib) >= 4000000:
#                     break 
#                 else: 
#                     efib.append(fp)

                


#     return sum(efib) , efib

# print(evenfibbonacci()) 
# 



# def largestprimefactor():
#     LN = 600851475143
#     PF = [1]
#     mp = 1
#     r = 0
#     for i in range(2,LN):

#         if LN % i == 0 :
#             PF.append(i)
#             mp = mp * i
            
#         if mp >= LN:
#             break    
#     return PF , mp

# print( largestprimefactor()  )  
    

# def largestPalindromeProduct():
#     for q in range(100,1000):
#         for p in range(100,1000):
#             i = p*q

#             num = i
#             reversed_num = int(str(num)[::-1])
#             #print(reversed_num)
#             if num == reversed_num :

#                 print(num,reversed_num, p ,q)



# print(largestPalindromeProduct())


# def smallestmultiple():
#     multiples = []
    
#     last = 20
#     for q in range(last,100000000000,last):
#         for i in reversed(range(3,last)):
        
#             if q % i == 0:
#                 if i == 3:
#                     return q
    
#             else :
#                 break    
                

# print(smallestmultiple())


# def sumsquaredifference():
#     sum1 = 0
#     sum2 = 0
#     n = 1000000000
#     for i in range(1,n+1):
#         sum1 += i
#         sum2 += i**2

#     print((sum1**2)-sum2) 



# sumsquaredifference()      

# def sumsquaredifference():
#     n = 100
    
#     sum_val = (n * (n + 1)) // 2 
    
#     sum_sq = (n * (n + 1) * (2 * n + 1)) // 6
   
#     print((sum_val**2) - sum_sq)

# sumsquaredifference()



# def selfpowers():
#     p = 0
#     for i in range(1,1001):
#         p += pow(i,i,10**10)

        

#     print(p%10**10)

# selfpowers()


