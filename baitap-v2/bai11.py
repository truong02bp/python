import math
def result(n):
    if (n == 1):
        print(1),
        return
    if (arrays[n]==True):
        print(n),
        return
    if (n%2==0):
        print(2),
        return    
    i = 2
    while (i < math.sqrt(n)+1):
        if (n%i==0):
            print(i),
            break
        i+=1;
arrays = []
for i in range(10005):
    arrays.append(True)
arrays[0]=False
arrays[1]=False
for i in range(2,10005):
    if (arrays[i] == True):
        for j in range(i*i,10005,i):
            arrays[j] = False                

t = int(input())
while (t>0):
    n = int(input())
    for i in range(1,n+1):
        result(i)
    print("")    
    t-=1
