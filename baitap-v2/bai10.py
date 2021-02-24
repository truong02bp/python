arrays = []
t = int(input())
for i in range(10005):
    arrays.append(True)
arrays[0]=False
arrays[1]=False
for i in range (10005):
    if (arrays[i]==True):
        for j in range(i*i,10005,i):
            arrays[j]=False
while (t>0):
    t-=1
    n = int(input())
    for i in range(1,n+1):
        if (arrays[i]==True):
            print(i),
    print("")               