import math

n =  470598593461

root = math.sqrt(n)

for i in range(1,int(root)+1):
    if n%i == 0:
        p = i
        q = n/i

print((p,q))
