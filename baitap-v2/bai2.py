def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a;
def lcm(a,b):
    return (a*b)/gcd(a,b)
n = int(input())
for i in range(n):
    a = input()
    result = 1
    for j in range(1,a+1):
        result = lcm(result,j)        
    print(result)            