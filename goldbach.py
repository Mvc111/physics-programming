def priem_of_niet(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

priemen = []
# counter checkpy goldbach
count = 0

for i in range (0,1001):
    if priem_of_niet(i) == True:
        count+=1
        priemen.append(i)


# als i - een priem een priem is heb je beide getallen         
for i in range(2,1001,2):
    for n in range (0,count):
          p = i - priemen[n]
          if p in priemen:
              print(f"{i}={priemen[n]}+{p}")
              break
                    
if p not in priemen:
        print("bingo")