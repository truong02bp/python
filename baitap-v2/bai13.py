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
    n = int(input())
    kt=0  
    for i in range(2,n/2):
        if (arrays[i]==True & arrays[n-i]==True):
            print(str(i) + " " + str(n-i))
            kt=1
            break
    if (kt==0):
        print(-1)               
                    