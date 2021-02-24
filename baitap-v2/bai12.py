arrays = []
for i in range(10005):
    arrays.append(True)
arrays[0]=False
arrays[1]=False
for i in range(10005):
    if (arrays[i] == True):
        for j in range(i*i,10005,i):
            arrays[j] = False
t = int(input())
while (t>0):
    t-=1
    m = int(input())
    n = int(input())       
    for i in range(m,n+1):
        if (arrays[i]==True):
            print(i),
    print("")                 
                    