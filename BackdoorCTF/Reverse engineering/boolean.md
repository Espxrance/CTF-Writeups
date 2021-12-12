# BackdoorCTF / noob20ctf - boolean

* **Category:** reversing
* **Points:** 96

## Challenge

> I like NAND logic, what's your favourite?

## Solution
![image](https://user-images.githubusercontent.com/78451563/145724713-c448a83e-9a81-436f-b313-131073e0eb70.png)
![image](https://user-images.githubusercontent.com/78451563/145725057-dc647a5b-362f-45b6-ba63-6a28ce3a8665.png)

The flag is already xored by the key `0x49` and stored in a variable. Our input is being xored by `0x49` acting as the key and then individually being compared with the flag.
```python3
#!/usr/bin/env python3
encrypted_flag = [47,37,40,46,50,49,121,59,22,120,58,22,36,48,22,47,125,63,121,60,59,32,61,122,52]
flag = []
for i in range(0, len(encrypted_flag)):
    flag.append(chr(encrypted_flag[i] ^ 0x49))
print("Flag:",''.join(flag))
```
```
Flag: flag{x0r_1s_my_f4v0urit3}
```
