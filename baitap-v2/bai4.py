
def convert(a,b):
    temp = 0
    for i in range(len(b)):
        temp = (temp*10 + int(b[i]))%a
    return temp
def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a
def result(a,b):
    return gcd(a,convert(a,b))            
t = input()
while (t>0):
    t-=1
    a = long(input())
    b = str(input())
    print(result(a,b))
