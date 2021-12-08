# TamilCTF - RevFun
* **Category:** reversing
* **Points:** 100
## Challenge  
>n00b had written his password down weirdly in the source code... but then he lost the source and only has the binary... help him out...  
## Solution 
![image](https://user-images.githubusercontent.com/78451563/145109120-04a313e0-2800-4b2d-980b-5e953d98f382.png)  
Using `ida64` it shows us that it gets the length of a string and stores it and the other variable stores the flag. It does a for loop comparing each characters of the flag with `dlr0w_s1h7_s1_yz4rC` which gets reversed to `Cr4zy_1s_7h1s_w0rld`. If a character is not equal to one of the chars in the reverse string it displays "Incorrect Password!" 
```python 
#!/usr/bin/python3
reversed_flag_string = len("dlr0w_s1h7_s1_yz4rC") 
compare = "Cr4zy_1s_7h1s_w0rld" 
for i in range(0, reversed_flag_string):     
if compare[i] != "dlr0w_s1h7_s1_yz4rC"[reversed_flag_string - i - 1]:         
	exit(-1)     
else:         
	print("Correct flag!")         
	print("Flag:", reversed_flag_string[::-1])
	break 
``` 
``` 
Flag: Cr4zy_1s_7h1s_w0rld 
``` 
