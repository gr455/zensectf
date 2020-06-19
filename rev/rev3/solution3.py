s = "CCXXIIIsXXIsVsCCXXVsCLXVIIIsXXXIVsCLIVsXIVsCCXXXVIIsIXsLXVIIsCLXIXsLXIIIsCLXVsLXIsCLIXsCXCVIIIsVIIIsCLsLIVsCCIXsXIXsCLXIIsLXVIsCLXIsLVIIsCCVsXVsXXXIXsCXCVsCLXsLVIIIsCLXVIsLXIIsCLXIsLVsXCIIsCLVIIIs"

l = s.split('s')
l.pop()

print(l)

def numbers(l):
    l_map = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    o = []
    for r in l:
        val = 0
        i = 0
        while i < len(r):
            if(i != len(r)-1 and l_map[r[i]] >= l_map[r[i+1]] or i == len(r)-1):
                val += l_map[r[i]]
                i += 1
            else:
                val += l_map[r[i+1]] - l_map[r[i]]
                i += 2
        o.append(val)
    return o

l = numbers(l)

def linnear(l):
    o = []
    for i in range(0,len(l),2):
        if(i != len(l)-1):
            num1 = (l[i]+l[i+1])/2
            num2 = (abs(l[i]-l[i+1])/2)
            if(l[i] > l[i+1]):
                o.append(num1)
                o.append(num2)
            else:
                o.append(num2)
                o.append(num1)
        else:
            o.append(l[i])
    return o

l = linnear(l)
r = ""

for i in l:
    r += chr(int(i))

print(r)

