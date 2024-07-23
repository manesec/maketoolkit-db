# Finding Sensity Files ( powershell )


## Winpeas

```
.\winpeas.exe browserinfo filesinfo fileanalysis eventsinfo
```

## Search string in file

```
findstr /si password *.txt
findstr /si password *.xml
findstr /si password *.ini

```

## Lists all txt

```
dir C:\users -force -filter "*.txt" -Recurse -ErrorAction silentlycontinue | foreach { $_.FullName} 

dir C:\users -force -filter "*.txt" -Recurse -ErrorAction silentlycontinue | foreach { "[$($_.Length)] $($_.FullName)" } 

dir C:\users -force -filter "*.txt" -Recurse -ErrorAction silentlycontinue | foreach { if($_.FullName -like "*PSReadLine*") {"[$($_.Length)] $($_.FullName)"}} 
```