import math
t = input()
while (t > 0):
    t-=1
    n = long(input())
    counter = 1
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i==0 & i!= math.sqrt(n)):
            counter+=i
            counter+=n/i
    if (int(math.sqrt(n))*int(math.sqrt(n))==n):
        counter+=math.sqrt(n) 
    if (counter == n):
        print(1)
    else:
        print(0)                