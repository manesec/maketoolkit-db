# Powershell RUNAS

note by manesec.

```powershell

# <USERNAME> may like: `.\manesec` on local domain.

# Sometimes will fail with unknow reason.
$pass = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("<USERNAME>", $pass)
Start-Process -Credential ($cred)  -NoNewWindow powershell "whoami"

# Via winrm
$pass = ConvertTo-SecureString '<PASSWORD>' -AsPlainText -Force
$cred = New-Object System.Management.Automation.PSCredential("<USERNAME>", $pass)
Invoke-Command -Computer $(hostname) -ScriptBlock { whoami } -Credential $cred

```

# Reference
https://book.hacktricks.xyz/windows-hardening/basic-powershell-for-pentesters#sudo