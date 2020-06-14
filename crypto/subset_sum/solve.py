import random

flag = "5m411_k3y"

l = input().split() 
l3 = [53]
print(l)
for i in range(1,len(l)):
    l3.append(int(l[i]))
print(l3)
'''[]
sumo = 0
sumo_flag = 0
count = 0
for i in range(10000):
    if i%((count+4)*10) == 0 and count < len(flag):
        l.append(ord(flag[count]))
        sumo_flag += ord(flag[count])
        count += 1
    else:
        l.append(random.randint(122,10000))
        sumo += l[-1]

print(f'Sum of the flag characters is {sumo_flag}')

#print(l)
#print(l)
'''
l2 = []
sumof = 0
for i in l:
    if ord('0') <= int(i) <= ord('9') or int(i) == ord('_') or ord('a') <= int(i) <= ord('z'):
        l2.append(i)
        sumof += i

#print((sumo*len(l))/pow(10,9))
print(l2)
print(f'Length of flag is {len(flag)} and length of l2 is {len(l2)} and sumof is {(sumof)*len(l2)/pow(10,9)}')

