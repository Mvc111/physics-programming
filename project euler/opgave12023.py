l = [10,1299,23,12,4,99,100,36,48,120]

def opgave1(l):
    drieenvier = []
    vijfen = []
    for i in range(0,len(l)):

        if l[i]%3 == 0 and l[i]%4 == 0:
            drieenvier.append(l[i])

    for p in range(0,len(drieenvier)):
        if drieenvier[p]%5 > 0:
            vijfen.append(drieenvier[p])

    print("veelvouden van 3 en 4",drieenvier)
    print("veelvouden van 3 en 4 (maar niet 5)",vijfen)

opgave1(l)