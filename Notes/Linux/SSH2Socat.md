# SSH 2 socat tunnel

```
socat TCP-LISTEN:1111,reuseaddr,fork EXEC:"ssh -i id_rsa -p 2222 backup_adm@10.13.38.23",pty,stderr,setsid,sigint,sane 
```