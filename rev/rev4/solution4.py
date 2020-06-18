import random
def xor(sd,s):
    random.seed(sd)
    l = list(s)
    m = map(lambda x : chr(ord(x)^random.randint(0,10)),l)
    l = list(m)
    res = ""
    for i in l:
        res += i
    return res

def turner(s):
    res = ""
    res += s[int(len(s)/2)+1:]
    res += s[:int(len(s)/2)+1]
    return res

def modifier(s):
    res = ""
    for i in s:
        res += chr(ord(i)+1)
    return res

s = "N*W]h0m8{R'tPl6V=^fWo<RskdD2Y3q?TaYoT1lHP"
s = xor(1065,s)
s = turner(s)
s = modifier(s)
s = xor(1427,s)
print("zenseCTF{"+s+"}")