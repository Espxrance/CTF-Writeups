# LIT CTF 2022 – minimalist

* **Category:** rev
* **Points:** 500

## Challenge

> less is more

## Solution

```python
#!/usr/bin/env python3
import angr
import claripy
import logging
logging.getLogger('angr').setLevel(logging.INFO)
addr_MAIN = 0x4011a9

p = angr.Project('./addition', auto_load_libs=False)
flag = claripy.BVS("flag",46*8)
state = p.factory.entry_state(add_options=angr.options.unicorn,addr=addr_MAIN)
sm = p.factory.simulation_manager(state)

sm.explore(find=0x4012e4,avoid=0x4012d3)
print(f'Input: {sm.found[0].posix.dumps(0)}')
# print('Std output: \n{}'.format(sm.found[0].posix.dumps(1)))
```

```
LITCTF{Wh0_n33ds_a11_th0sE_f4ncy_1nstructions?}
```
