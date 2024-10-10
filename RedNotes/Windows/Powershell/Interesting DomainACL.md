# Interesting Domain ACL

```powershell
# powerview.ps1
PS C:\mane> Find-InterestingDomainAcl

# convert mane to sid
PS C:\mane> Import-Module .\PowerView.ps1
PS C:\mane> $sid = Convert-NameToSid mane

# Finding SecurityIdentifier with XXX
PS C:\mane> Get-DomainObjectACL -Identity * | ? {$_.SecurityIdentifier -eq $sid}

# Get Group User
PS C:\mane> Get-DomainGroup -Identity "Domain Admins" | select memberof

```






