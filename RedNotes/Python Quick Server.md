# Python Quick Server

## Http server

``` bash
$ python3 -m http.server --bind :: 9999
Serving HTTP on :: port 9999 (http://[::]:9999/) ...
```

## SMTP server

```bash
$ sudo python3 -m smtpd -c DebuggingServer -n 10.10.16.14:25
<Nothing to display>
```
