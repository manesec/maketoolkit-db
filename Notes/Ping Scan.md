# Ping Scan OneLine


``` bash
for x in {1..254} ;do ping -c 2 "172.16.1.$x" | grep "bytes from" | cut -d ':' -f 1 | cut -d ' ' -f 4 | sort | uniq  ; done;
```


```cmd
(for /L %a IN (1,1,254) DO ping /n 1 /w 1 172.16.2.%a) | find "Reply"
```


