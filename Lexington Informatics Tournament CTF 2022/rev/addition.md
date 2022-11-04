# LIT CTF 2022 – addition

* **Category:** rev
* **Points:** 500

## Challenge

> Enter the flag, and it will be checked with addition!

## Solution
![image](https://user-images.githubusercontent.com/78451563/180712839-9764512e-0763-4849-b433-7b79ef2c8b0f.png)

As the binary is `stripped` which means `a program that is compiled with a strip flag that tells the compiler to discard these debugging symbols and compile to program as it is` we need to find the main address of the binary.</br>
How to find the main address, either:
- Search for defined strings and check for references</br>
![image](https://user-images.githubusercontent.com/78451563/180714609-10ff3336-7840-4666-84d7-d10f18fc5674.png)

- Go to `entry()` function</br>
![image](https://user-images.githubusercontent.com/78451563/180715144-2e5ea227-4ccb-4b8e-ad12-3157753b6a79.png)

**Main function**

![image](https://user-images.githubusercontent.com/78451563/180673509-81d4f00b-15ac-4fa3-85cc-404a9790c6f6.png)


Having found the "main" function we can start analysing:
* We see a constraint of length 24 for our input
* Our input is converted to ascii and stored
* The flag variable is storing pieces of the flag which is made up from an addition of different numbers from different variables.
* Finally, our input is being compared to pieces of the flag


We can use `angr` to simply solve:
```python
#!/usr/bin/env python3
import angr
import claripy
import logging
logging.getLogger('angr').setLevel(logging.INFO) # debugging purposes
addr_MAIN = 0x401070 # Start execution from specific address (reduce runtime)

p = angr.Project('./addition', auto_load_libs=False)
flag = claripy.BVS("flag",25*8) # constraint defined but not used
state = p.factory.entry_state(add_options=angr.options.unicorn,addr=addr_MAIN) # Intiate the binary
sm = p.factory.simulation_manager(state)

sm.explore(find=0x4010dd,avoid=0x4010c9) # addresses we want to reach or avoid e.g puts("correct") / puts("wrong")
print(f'Input: {sm.found[0].posix.dumps(0)}')
```
```
Flag: LITCTF{add1ti0n_is_h4rd}
```
