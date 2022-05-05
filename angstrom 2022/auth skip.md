# angstromctf 2022 - crumbs
* **Category:** web
* **Points:** 50
## Challenge
>Follow the crumbs.
>Server: index.js
## Solution
![image](https://user-images.githubusercontent.com/78451563/166748934-bd7e521a-6bf0-43c3-9f45-ac2b5a785add.png)</br>
##### Basically following the crumbs.

♡ A list is being created with 1000 random v5 UUID's</br>
♡ At the end of the list the flag is replaced with the 1000th v5 UUID
```bash
#!/bin/bash
url="https://crumbs.web.actf.co/"
response=$(curl $url -s)
echo "${response: 6}"
while true
do
	if [[ "actf{" == *${response}* ]]; then
		echo -e "\e[5mSuccess\!"
		echo $response
		exit
	else
		uuid=${response: 6}
		echo $url$uuid
		response=$(curl $url$uuid -s)
		echo $response
	fi
done
```

```
Flag: actf{w4ke_up_to_th3_m0on_6bdc10d7c6d5}
```
