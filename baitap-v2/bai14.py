import math
def check(n):
    kt=0
    i=2
    while (i < math.sqrt(n)+1):
        counter=0
        while (n%i==0):
            counter+=1
            n/=i
        if (counter == 1):
            kt+=1
        if (counter > 1):
            return False    
        i+=1;    
    if (n > 1):
        kt+=1    
    if (kt != 3):
        return False
    return True    
t = input()
while (t>0):
    n = input()
    if (check(n)):
        print(1)
    else:
        print(0)    
    t-=1;