import matplotlib
matplotlib.use('Agg')

import random
import matplotlib.pyplot as plt

N = 10000

def som_random_getallen(N):
    sommen_lijst = []  
    count_onder_40 = 0
    count_boven_60 = 0

   
    for experiment in range(N):
        hele_getal = 0
        
        
        for i in range(100):
            getal = random.random()          
            hele_getal += getal
        
        sommen_lijst.append(hele_getal)
        
       
        if hele_getal < 40:
            count_onder_40 += 1
        elif hele_getal > 60:
            count_boven_60 += 1

    
    percentage_onder_40 = (count_onder_40 / N) * 100
    percentage_boven_60 = (count_boven_60 / N) * 100

   
    print(f"Percentage experimenten met som minder dan 40: {percentage_onder_40:.2f}%")
    print(f"Percentage experimenten met som meer dan 60: {percentage_boven_60:.2f}%")

    
    plt.xlim(30, 70)
    plt.hist(sommen_lijst, bins=50)
    plt.savefig('plot.png')


som_random_getallen(N)

# checkpy doet het nietmeer 