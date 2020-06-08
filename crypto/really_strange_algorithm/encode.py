import math
from Crypto.Util.number import inverse
def gcd(x,y):
    if y <= x:
        return gcd(y,x)
    if y%x == 0:
        return x
    return gcd( y%x,x)

def extended_euclid(x,y):
    if( y<= x):
        return extended_euclid(y,x)
    if gcd(x,y) != 1:
        return -1
    r = [y,x]
    q = [] #int(y/x)]
    a = [0,1]
    while r[-1] != 1:
        q.append(int(r[-2]/r[-1]))
        r.append(r[-2]%r[-1])
        a.append( (a[-2] - q[-1]*a[-1])%y)
    return a[-1]





def convert_to_message(s):

    d = {}
    d2 = {}

    for i in range(ord('a'), ord('z')+1):
        d[chr(i)] = i-ord('a')+1
    #d['_'] = ord('_') - ord('a') + 1
    s2 = ""
    for i in s:
        print(d[i])
        s2 += str(d[i])
    return int(s2)

def convert_to_number(n):
    s2 = ""

p = 982451653
q = 961748927
n = p*q #944871823102126331
e = 65537

phi = (p-1)*(q-1)

d = inverse(e,phi) #int((1+phi)/e) #extended_euclid(e,phi)
print(f'This is d {d}')
msg = convert_to_message("weakrsaeasy") 
#msg = 2351111819191912351915135
print(f'msg : {msg}')
ciphertext = pow(msg,e,n)
#print(ciphertext)

print(type(d))
print(f'n : {n}')
print(f'e : {e}')
print(f'ciphertext : {ciphertext}')

msg2 = pow(ciphertext,d,n)
print(f'message2 : {msg2}')

