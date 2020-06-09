from pwn import *

host = "localhost"
port = 6969

r = remote(host, port)
prompt = r.recvuntil("guess it correctly :)\n")
print(prompt)
min = 0
max = 1000000
guess = 0

while(guess<30):
    guess += 1
    val = int((min+max)/2)
    print("Sending {0}".format(val))
    r.send(str(val).encode('utf-8'))
    prompt1 = r.recv().decode()
    if (prompt1.find("lesser") >= 0):
        min = val
    elif(prompt1.find("greater") >= 0):
        max = val
    else:
        print(prompt1)
