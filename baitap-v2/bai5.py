def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a
def sinh(a,n):
    result = ""
    for i in range(n):
        result+=a
    return result
def result(a,x,y):
    return sinh(a,gcd(x,y))                
t = input()
while (t>0):
    t-=1
    a = str(input())
    x = long(input())
    y = long(input())
    print(result(a,x,y))