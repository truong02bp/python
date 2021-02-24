modulo = 1000000007
def tich(a):
    mul = 1
    for item in a:
        mul = mul*item
        mul%=modulo
    return mul

def gcd(a,b):
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a    

def uocSoChung(a):
    result = a[0]
    for i in range(1,len(a)):
        result = gcd(result,a[i])
    return result 
def result(hx,gx):
    if (gx == 1):
        return hx
    if (gx == 0):
        return 1
    temp = result(hx,gx/2)
    if (gx%2):
        temp = (((hx*temp)%modulo)*temp)%modulo
    else:
        temp = (temp*temp)%modulo
    return temp;                
t = input()
while (t>0):
    n = input()
    a = []
    for i in range(n):
        a.append(int(input()))
    hx = tich(a)
    gx = uocSoChung(a)
    print(result(hx,gx))
    t-=1
