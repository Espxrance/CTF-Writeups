# HackTheBoo - Juggling Facts  
* **Category:** Web 
* **Points:** 200
* **Author:** xcl0w3n  
## Challenge  
> An organization seems to possess knowledge of the true nature of pumpkins. Can you find out what they honestly know and uncover this centuries-long secret once and for all?  
## Solution 

![image](https://user-images.githubusercontent.com/78451563/198313644-1a82c2ea-505f-43dc-955d-710d919fa55a.png)  

* We need to access the "secret facts" to get the flag. However, we need to be strictly from the origin source of 127.0.0.1.
* The vulnerability here is that `switch()` uses a loose comparison which can lead to a type juggling attack.  
```
(PHP 4, PHP 5, PHP 7, PHP 8)
The switch statement is similar to a series of IF statements on the same expression. In many occasions, you may want to compare the same variable (or expression) with many different values, and execute a different piece of code depending on which value it equals to.
```
![image](https://user-images.githubusercontent.com/78451563/198375489-f63b6668-e774-4345-8b35-d9c8f1bcff62.png)

* Basically, the code treats our input as a comparison of "secret" and `true`
```
if("secret" == true){
case 'secrets':
    return $router->jsonify([
        'facts' => $this->facts->get_facts('secrets')
    ]);
}
```
```
Flag: HTB{sw1tch_stat3m3nts_4r3_vuln3r4bl3!!!}
```
