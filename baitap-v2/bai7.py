def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a;
def lcm(a,b):
    return (a*b)/gcd(a,b)    
def result(n,x,y,z):
    ucln = lcm(x,y)
    ucln = lcm(ucln,z)
    result = pow(10,n-1)
    temp = result%ucln
    if (temp == 0):
        return result
    else:
        result = result-temp+ucln     
        if (result >= pow(10,n)):
            return -1
        return result           
t = input()
while (t>0):
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(result(n,x,y,z))
    t-=1