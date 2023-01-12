# angstromctf 2022 - The Flash

* **Category:** web
* **Points:** 40

## Challenge

>The new Justice League movies nerfed the Flash, so clam made his own rendition!</br>
>Can you get the flag before the Flash swaps it out at the speed of light?

## Solution
![image](https://user-images.githubusercontent.com/78451563/166795440-950559f1-d49f-4419-ac98-674fba7187d1.png)</br>
![image](https://user-images.githubusercontent.com/78451563/166801128-acc6732d-631d-4896-bb70-7b86608a9630.png)</br>
Looking into the DOM we can see `flash.js` being used to change the screen.</br>
We can evalute the obfuscated javascript and then set a breakpoint to stop the action being executed.</br>

```
Flag: actf{sp33dy_l1ke_th3_fl4sh}
```
