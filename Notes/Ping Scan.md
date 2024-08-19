# Ping Scan OneLine

``` bash
for x in {1..254} ;do ping -c 2 "172.16.1.$x" | grep "bytes from" | cut -d ':' -f 1 | cut -d ' ' -f 4 | sort | uniq  ; done;
for i in {1..254} ;do (ping -c 1 172.16.5.$i | grep "bytes from" &) ;done
```

```cmd
(for /L %a IN (1,1,254) DO ping /n 1 /w 1 172.16.2.%a) | find "Reply"
for /L %i in (1 1 254) do ping 172.16.5.%i -n 1 -w 100 | find "Reply"
```

```powershell
1..254 | % {"172.16.5.$($_): $(Test-Connection -count 1 -comp 172.15.5.$($_) -quiet)"}
```


