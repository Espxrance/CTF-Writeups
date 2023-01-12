# angstrom 2022 - art gallery

* **Category:** web
* **Points:** 100

## Challenge

>bosh left his image gallery service running.... quick, git all of his secrets before he deletes them!!!

## Solution
#### LFI (Local File Inclusion)
![image](https://user-images.githubusercontent.com/78451563/166815435-707f181f-3553-47c7-ac4a-d5f0626bfc1c.png)</br>
♡ As there is no sanitization for the `member` parameter we can control which file is joined.
#### Git dumping
![image](https://user-images.githubusercontent.com/78451563/166816935-5fa9ef7f-1aa2-46ff-ad5e-1aec4bbafe64.png)</br>
![image](https://user-images.githubusercontent.com/78451563/166817018-00897820-639c-4d38-8ded-0bca3df81683.png)</br>
♡ The challenge description gives us a hint that there is a file `.git`</br>
♡ Using [git dumper](https://github.com/arthaud/git-dumper/blob/master/git_dumper.py) we can extract the web contents of `.git`</br>
♡ Then using [git extractor](https://github.com/internetwache/GitTools/blob/master/Extractor/extractor.sh) we can extract the history</br>
♡ Inside the extracted git directory `2-56449caeb7973b88f20d67b4c343cbb895aa6bc7` the flag is there.
```
Flag: actf{lfi_me_alone_and_git_out_341n4kaf5u59v}
```
