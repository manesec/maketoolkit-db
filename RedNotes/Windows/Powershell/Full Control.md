
```powershell
$acl = Get-Acl C:\users\administrator\desktop\flag.txt;  $permission = "Everyone","FullControl","Allow" ; $rule = New-Object System.Security.AccessControl.FileSystemAccessRule $permission; $acl.SetAccessRule($rule); $acl | Set-Acl C:\users\administrator\desktop\flag.txt
```