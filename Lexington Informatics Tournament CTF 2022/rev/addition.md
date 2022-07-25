# LIT CTF 2022 – addition

* **Category:** rev
* **Points:** 500

## Challenge

> Enter the flag, and it will be checked with addition!

## Solution

```python
#!/usr/bin/env python3
import angr
import claripy
import logging
logging.getLogger('angr').setLevel(logging.INFO)
addr_MAIN = 0x401070 # Start execution from specific address (reduce runtime)

p = angr.Project('./addition', auto_load_libs=False)
flag = claripy.BVS("flag",25*8) # constraint but not used
state = p.factory.entry_state(add_options=angr.options.unicorn,addr=addr_MAIN,stdin=flag) # Intiate the binary
sm = p.factory.simulation_manager(state)

sm.explore(find=0x4010dd,avoid=0x4010c9)
print(f'Input: {sm.found[0].posix.dumps(0)}')
```
![image](https://user-images.githubusercontent.com/78451563/180673509-81d4f00b-15ac-4fa3-85cc-404a9790c6f6.png)


In the "main" function we see a constraint of length 24 for our input which is being compared to the flag.
```
LITCTF{add1ti0n_is_h4rd}
```
