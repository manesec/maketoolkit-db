# Install Programs

```
cmd> wmic product get name

PS> Get-WmiObject -Class Win32_Product |  select Name, Version

PS> $InstalledSoftware = Get-ChildItem "HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall"
foreach($obj in $InstalledSoftware){write-host $obj.GetValue('DisplayName') -NoNewline; write-host " - " -NoNewline; write-host $obj.GetValue('DisplayVersion')}

PS> $InstalledSoftware = Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Uninstall"
foreach($obj in $InstalledSoftware){write-host $obj.GetValue('DisplayName') -NoNewline; write-host " - " -NoNewline; write-host $obj.GetValue('DisplayVersion')}

PS> Get-WinEvent -ProviderName msiinstaller | where id -eq 1033 | select timecreated,message | FL *
```


## Reference

+ https://www.codetwo.com/admins-blog/how-to-check-installed-software-version/