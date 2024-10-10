# Group - Event Log Readers

```
net localgroup "Event Log Readers"
```

## Read the log

```
PS C:\mane> wevtutil qe Security /rd:true /f:text | Select-String "/user"

C:\mane> wevtutil qe Security /rd:true /f:text /r:share01 /u:mane /p:password | findstr "/user"

PS C:\mane> Get-WinEvent -LogName security | where { $_.ID -eq 4688 -and $_.Properties[8].Value -like '*/user*'} | Select-Object @{name='CommandLine';expression={ $_.Properties[8].Value }}

```

## Reference

+ Hackthebox academy - Windows Privilege Escalation - Event Log Readers