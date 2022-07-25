# LIT CTF 2022 – EYANGCH Fan Art Maker / EYANGCH Fan Art Maker 2.0

* **Category:** web
* **Points:** 500

## Challenge

> I am biggest fan of Eyang OTZ OTZ OTZ, which is why I built this EYANGCH Fan Art Maker

## Solution

**Unintended easy solution 🤣**
*Works for both challenges*
![image](https://user-images.githubusercontent.com/78451563/180677028-c9ad08c6-2277-4dd8-9851-9db39fac0d18.png)

```html
<component name="EYANGOTZ">
	<component name="eyes1">
		<line x1="0" y1="0" x2="0" y2="0" color="#1089f5" width="0"></line>
		<line x1="0" y1="0" x2="0" y2="0" color="#1089f5" width="0"></line>
	</component>
	<component name="eyes2">
		<line x1="0" y1="0" x2="0" y2="0" color="#1089f5" width="0"></line>
		<line x1="0" y1="0" x2="0" y2="0" color="#1089f5" width="0"></line>
	</component>
	<component name="mouth">
		<line x1="0" y1="0" x2="0" y2="0" color="#1089f5" width="0"></line>
		<line x1="0" y1="0" x2="0" y2="0" color="#1089f5" width="0"></line>
		<line x1="0" y1="0" x2="0" y2="0" color="#1089f5" width="0"></line>
	</component>
	<text x="0" y="0" font="bold 10pt Arial">EYANG SO OTZ</text>
</component>
<EYANGOTZ x="0" y="0"></EYANGOTZ>
<EYANGOTZ x="0" y="0"></EYANGOTZ>
<EYANGOTZ x="0" y="0"></EYANGOTZ>
<EYANGOTZ x="0" y="0"></EYANGOTZ>
<EYANGOTZ x="0" y="0"></EYANGOTZ>
<EYANGOTZ x="0" y="0"></EYANGOTZ>
```
![image](https://user-images.githubusercontent.com/78451563/180677236-4a499261-1d87-4b73-b2c1-eed485185dec.png)


In `main.js` we see how the "code" for the image is generated, we could try to overwrite this by injecting our own code.
```
LITCTF{wh4t_d03s_CH_1n_EyangCH_m3an???}
LITCTF{3y4ngCH_15L1k3_ju5t_s0_g3n10sit4}
```
