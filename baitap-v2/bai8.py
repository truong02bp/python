import math
t = int(input())

while (t>0):
    t-=1
    n = long(input())
    i = 2
    while (i < math.sqrt(n)+1):
        while(n%i==0):
            print(i),
            n/=i
        i+=1
    if (n>1):
        print(n)    
