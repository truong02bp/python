import math

t = int(input())

while (t>0):
    t-=1
    n = long(input())
    result = 0
    i = 2
    while (i < math.sqrt(n) + 1):
        while (n%i==0):
            result = max(result,i)
            n/=i
        i+=1
    if (n>1):
        result = max(result,n)        
    print(result)    