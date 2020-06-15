import enchant

d = enchant.Dict("en_UK")

def mapp(f,l):
    l2 = []
    for i in l:
        l2.append(f(i))
    return l2

t = ""

def change(l,i,x):
    l[l.index(i)] = x

def leet_to_ascii(l):
    for i in l:
        if i == "1":
            change(l,i,"l")
        if i == "3":
            change(l,i,"e")
        if i == "4":
            change(l,i,"a")
        if i == "5":
            change(l,i,"s")
    return l

def change_string(s,i,x):
    return s[ :i] + x + s[i+1:]

def ascii_to_leet(l):
    for i in range(len(l)):
        if l[i] == "l":
            l = change_string(l,i,"1")
            #print(f'This is {l}')
        if l[i] == "e":
            l = change_string(l,i,"3")
        if l[i] == "a":
            l = change_string(l,i,"4")
        if l[i] == "s":
            l = change_string(l,i,"5")
    return l
#print(ascii_to_leet("1b3"))
while t != "-1":
    t = input()
    if t == -1:
        break
    l = mapp(int,t.split())
    l.reverse()
    l = mapp(chr,l)
    l = leet_to_ascii(l)
    if "_" in l:
        s1 = ""
        s2 = ""
        ind = l.index("_")
        for i in l:
            if l.index(i) < ind:
                s1 += i
            if l.index(i) > ind:
                s2 += i
        if len(s1) == 0 or len(s2) == 0:
            continue
        if d.check(s1) and d.check(s2):
            s3 = ascii_to_leet(s1+s2)
            print(s3) #ascii_to_leet(s1+s2))
            #print(s2)



