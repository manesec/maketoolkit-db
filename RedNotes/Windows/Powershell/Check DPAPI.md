# Check DPAPI with all user

some certification file on window system.


# Oneline
```powershell
Get-ChildItem C:\users | foreach-object { "=================== $($_.FullName) ==================="; "[*] Finding Credentials ..."; Get-ChildItem -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Local\Microsoft\Credentials\") | foreach-object {$_.FullName}; ; Get-ChildItem -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Roaming\Microsoft\Credentials\") | foreach-object {$_.FullName}; ; "[*] Finding Master Key ..."; Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Roaming\Microsoft\Protect\") | foreach-object {$_.FullName}; Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Local\Microsoft\Protect\") | foreach-object {$_.FullName}; ; }

```

## Find Credentials 
```powershell
Get-ChildItem C:\users | foreach-object {  Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Local\Microsoft\Credentials\"); Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Roaming\Microsoft\Credentials\");  }
```

## Master Key

```powershell
Get-ChildItem C:\users | foreach-object {  Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Roaming\Microsoft\Protect\"); Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Local\Microsoft\Protect\");  }
```

## Fullscript

```powershell
Get-ChildItem C:\users | foreach-object { 
 "===================   $($_.FullName)   ===================";
 "[*] Finding Credentials ...";
 Get-ChildItem -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Local\Microsoft\Credentials\") | foreach-object {$_.FullName}; ; 
 Get-ChildItem -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Roaming\Microsoft\Credentials\") | foreach-object {$_.FullName}; ;
 
 "[*] Finding Master Key ...";
 Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Roaming\Microsoft\Protect\") | foreach-object {$_.FullName}; 
 Get-ChildItem -Recurse -Force -ErrorAction silentlycontinue $( $_.FullName + "\AppData\Local\Microsoft\Protect\") | foreach-object {$_.FullName}; ;  
}
```


