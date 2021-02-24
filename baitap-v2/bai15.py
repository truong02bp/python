t = input()
def result(n,p):
    counter = 0
    for i in range(p,n+1,p):
        x = i
        while (x%i==0):
            counter+=1
            x/=p
    return counter        
while (t > 0):
    t-=1
    n = input()
    p = input()
    print(result(n,p))