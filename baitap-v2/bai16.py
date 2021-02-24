import math
t = input()
while (t > 0):
    t-=1
    n = input()
    i = 2
    while(i < math.sqrt(n)+1):
        counter = 0
        while (n%i==0):
            counter+=1
            n/=i
        if (counter != 0):
            print(str(i) + " " + str(counter)),
        i+=1
    if (n > 1):    
        print(str(n) + " " + str(1)),
    print("")    

    