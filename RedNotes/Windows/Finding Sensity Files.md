# Finding Sensity Files ( powershell )


## Winpeas

```
.\winpeas.exe browserinfo filesinfo fileanalysis eventsinfo
```

## Search string in file 

```
findstr /S /I /C:"password" "C:\Users\*"*.txt *.ini *.cfg *.config *.xml
findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml
findstr /SI /M "password" *.xml *.ini *.txt
findstr /spin "password" *.*
findstr /si password *.txt
findstr /si password *.xml
findstr /si password *.ini

select-string -Path C:\Users\htb-student\Documents\*.txt -Pattern password

```


## Extension files

```
dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*

where /R C:\ *.config

Get-ChildItem C:\ -Recurse -Include *.rdp, *.config, *.vnc, *.cred -ErrorAction Ignore
```

## Lists all txt

```
dir C:\users -force -filter "*.txt" -Recurse -ErrorAction silentlycontinue | foreach { $_.FullName} 

dir C:\users -force -filter "*.txt" -Recurse -ErrorAction silentlycontinue | foreach { "[$($_.Length)] $($_.FullName)" } 


```
## Powershell History

```
dir C:\users -force -filter "*.txt" -Recurse -ErrorAction silentlycontinue | foreach { if($_.FullName -like "*PSReadLine*") {"[$($_.Length)] $($_.FullName)"}} 

(Get-PSReadLineOption).HistorySavePath

gc (Get-PSReadLineOption).HistorySavePath
```

## Chrome Dictionary Files

```
PS C:\htb> gc 'C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Custom Dictionary.txt' | Select-String password

Password1234!
```

## Unattended Installation Files

like: `unattend.xml`

maybe in `C:\Windows\Panther` or `System32\Panther`

password store with base64 encode.

## Sticky Notes Passwords

IN `C:\Users\<user>\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite`

using sqlite to open and read the notes.

or `strings plum.sqlite-wal`

## Other Interesting Files

```
%SYSTEMDRIVE%\pagefile.sys
%WINDIR%\debug\NetSetup.log
%WINDIR%\repair\sam
%WINDIR%\repair\system
%WINDIR%\repair\software, %WINDIR%\repair\security
%WINDIR%\iis6.log
%WINDIR%\system32\config\AppEvent.Evt
%WINDIR%\system32\config\SecEvent.Evt
%WINDIR%\system32\config\default.sav
%WINDIR%\system32\config\security.sav
%WINDIR%\system32\config\software.sav
%WINDIR%\system32\config\system.sav
%WINDIR%\system32\CCM\logs\*.log
%USERPROFILE%\ntuser.dat
%USERPROFILE%\LocalS~1\Tempor~1\Content.IE5\index.dat
%WINDIR%\System32\drivers\etc\hosts
C:\ProgramData\Configs\*
C:\Program Files\Windows PowerShell\*

C:\programData\*
```

