import math
N = 100
def opgave2():
    lpi = []
    epi = []
    for i in range(N):
        leibniz = ( (-1)**i ) / (2*i + 1)
        euler = (((i+1)**(-2)))

        lpi.append(leibniz)
        epi.append(euler)
    
    lfpi = 4*sum(lpi)
    efpi = (6*sum(epi))**0.5
    deltal = abs(lfpi - math.pi) / math.pi * 100
    deltae = abs(efpi-math.pi)/ math.pi * 100
    
    print(N)
    print("leibniz", lfpi, deltal)
    print("euler",efpi, deltae)

opgave2()