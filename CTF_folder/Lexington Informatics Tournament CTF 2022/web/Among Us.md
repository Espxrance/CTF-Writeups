# LIT CTF 2022 – Among Us

* **Category:** web
* **Points:** 500

## Challenge

> Hello! I am Polopopy, and my friends like to call me Ryan. I have an unhealthy fetichobsession with Among Us, so I made this website to demonstrate my unyielding enthusiasm!

## Solution

![image](https://user-images.githubusercontent.com/78451563/180677563-e984fe5d-7cb6-4cf3-b90a-660ca00664a7.png)

Loading the page we get two main request.
1. The web page
2. The resource at `/sussy-yellow-amogus` which is suppose to be a gif file

Testing for an easy sensitive data exposure in the headers i came across a unique header which had the flag.
```
LITCTF{mr_r4y_h4n_m4y_b3_su55y_bu7_4t_l3ast_h3s_OTZOTZOTZ}
```
