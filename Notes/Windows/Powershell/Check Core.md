# How to check Server Core or Server with Desktop Experience?

```
*Evil-WinRM* PS C:\Users\Administrator\Documents> Get-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion"


SystemRoot                : C:\Windows
BaseBuildRevisionNumber   : 859
BuildBranch               : fe_release_svc_prod2
BuildGUID                 : ffffffff-ffff-ffff-ffff-ffffffffffff
BuildLab                  : 20348.fe_release_svc_prod2.220707-1832
BuildLabEx                : 20348.859.amd64fre.fe_release_svc_prod2.220707-1832
CompositionEditionID      : ServerStandard
CurrentBuild              : 20348
CurrentBuildNumber        : 20348
CurrentMajorVersionNumber : 10
CurrentMinorVersionNumber : 0
CurrentType               : Multiprocessor Free
CurrentVersion            : 6.3
DisplayVersion            : 21H2
EditionID                 : ServerStandard
EditionSubManufacturer    :
EditionSubstring          :
EditionSubVersion         :
InstallationType          : Server Core
InstallDate               : 1640900106
LCUVer                    : 10.0.20348.2113
ProductName               : Windows Server 2022 Standard
ReleaseId                 : 2009
SoftwareType              : System
UBR                       : 2113
PathName                  : C:\Windows
RegisteredOwner           : Windows User
RegisteredOrganization    :
ProductId                 : 00453-60000-00000-AA756
DigitalProductId          : {164, 0, 0, 0...}
DigitalProductId4         : {248, 4, 0, 0...}
InstallTime               : 132853737069926002
PSPath                    : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion
PSParentPath              : Microsoft.PowerShell.Core\Registry::HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT
PSChildName               : CurrentVersion
PSDrive                   : HKLM
PSProvider                : Microsoft.PowerShell.Core\Registry
```

And you can see it is `InstallationType          : Server Core`, no desktop.