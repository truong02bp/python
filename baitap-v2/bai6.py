def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a
        
t = input()

while (t>0):
    t-=1
    n = int(input())
    m = int(input())
    sum = n*(n+1)/2
    sum1 = (sum+m)/2
    sum2 = sum-sum1
    if (abs(sum1-sum2) == m):
        if (gcd(sum1,sum2) == 1):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")            
