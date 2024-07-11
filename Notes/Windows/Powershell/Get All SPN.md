## Get All SPN


```powershell
$search = New-Object DirectoryServices.DirectorySearcher([ADSI]"")
$search.filter = "(servicePrincipalName=*)"
$results = $search.Findall()

#list results

foreach($result in $results)
{
    $userEntry = $result.GetDirectoryEntry()
    Write-host "Object Name = " $userEntry.name -backgroundcolor "yellow" -foregroundcolor "black"
    Write-host "DN      =      "  $userEntry.distinguishedName
    Write-host "Object Cat. = "  $userEntry.objectCategory
    Write-host "servicePrincipalNames"        

    foreach($SPN in $userEntry.servicePrincipalName)
    {
        Write-host "SPN   =      " $SPN    
    }
    Write-host ""

}
```


https://identityunderground.wordpress.com/2013/08/08/list-all-spns-used-in-your-active-directory/