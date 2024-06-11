# Bash Ping Scan OneLine


``` bash
for x in {1..254} ;do ping -c 2 "172.16.1.$x" | grep "bytes from" | cut -d ':' -f 1 | cut -d ' ' -f 4 | sort  ; done;
```