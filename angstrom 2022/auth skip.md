# angstrom 2022 - auth skip

* **Category:** web
* **Points:** 40

## Challenge

>Clam was doing his angstromCTF flag% speedrun when he ran into the infamous timesink known in the speedrunning community as "auth".</br>
>Can you pull off the legendary auth skip and get the flag?

## Solution
![image](https://user-images.githubusercontent.com/78451563/166802135-3f3eee19-fd8b-46f7-ada8-d4ced7a128b2.png)</br>
#### No random encryption was assigned to the cookie creation</br>♡ Once the username "admin" and the correct password is sent a cookie is assigned.</br>♡ We can create a cookie with the value of "admin"</br>
![image](https://user-images.githubusercontent.com/78451563/166801968-21cf7407-a9de-4d4e-af53-cee2a028482c.png)</br>


```
Flag: actf{passwordless_authentication_is_the_new_hip_thing}
```
