# CTF Name – rev-warmup

* **Category:** reversing
* **Points:** 235

## Challenge

>n00b is a beginner in reversing, but even he was able to do it. Can you?

## Solution
![image](https://user-images.githubusercontent.com/78451563/145462644-b26d9b7d-605f-4734-bb2c-0b1bba9f7924.png)
![image](https://user-images.githubusercontent.com/78451563/145462674-3947f1e1-05b2-4a4f-93f7-86bbf2a87fc7.png)
![image](https://user-images.githubusercontent.com/78451563/145465208-6e7b494c-26ef-4396-bb6f-6976a3557d57.png)

Essentially, the there are two variables which xored gives the flag.
```python3
from pwn import *
v6 = [-40, 77, 114, 86, 23, -107, -71, 85, -3, 62, -29, -112, -46, -37, 124, -126, -105, 16, 103, 111, 43, -49, -50, 88, 22, 12]
v7 = [-66, 33, 19, 49, 108, -47, -48, 49, -94, 71, -45, -59, -115, -79, 41, -73, -96, 79, 21, 92, 125, -4, -68, 109, 37, 113]
flag = []
results = []
for i in range(0, 26):
    flag += xor(v6[i] ^ v7[i])
results = [chr(i) for i in flag]
print("Flag: %s" % ''.join(results))
```
### Using gdb:
![image](https://user-images.githubusercontent.com/78451563/145464845-bb68466b-2c79-4252-9236-627be67d7c4f.png)
![image](https://user-images.githubusercontent.com/78451563/145465345-37e1f49e-c630-4e14-9116-2eec4b319f81.png)

We can break at the main function then skip steps until we reach the strcmp(string compare) call and from then we can check the RDI register to see what is being compared.

```gdb
b main
ni (do "ni" until strcmp is called)
print (char *) ($rsi)
```
```
Flag: 
```
