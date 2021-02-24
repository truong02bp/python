n = input()
def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b  = temp
    return a;
def lcm(a,b):
    return (a*b)/gcd(a,b)

for i in range(n):
    a = input()
    b = input()
    print(str(lcm(a,b))+ " " + str(gcd(a,b)))