# SMB Note

Write by manesec.

## Tools: smbcacls 

Using `smbcacls` to check permission, `smbmap` may not display correctly.

For example: If you want to check `\\10.129.103.152\Department Shares\Users\Public` , 

```bash
$smbcacls -N '\\10.129.103.152\Department Shares' /Users/Public
REVISION:1
CONTROL:SR|DI|DP
OWNER:BUILTIN\Administrators
GROUP:HTB\Domain Users
ACL:Everyone:ALLOWED/OI|CI/FULL
ACL:S-1-5-21-2379389067-1826974543-3574127760-1000:ALLOWED/OI|CI|I/FULL
ACL:BUILTIN\Administrators:ALLOWED/OI|CI|I/FULL
ACL:Everyone:ALLOWED/OI|CI|I/READ
ACL:NT AUTHORITY\SYSTEM:ALLOWED/OI|CI|I/FULL


$smbmap -u 'guest' -p '' -H 10.129.103.152 -R 'Department Shares/Users/Public'
[+] IP: 10.129.103.152:445      Name: 10.129.103.152
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        Department Shares                                       READ ONLY
        .\Department SharesUsers\Public\*
        dr--r--r--                0 Wed Sep 26 06:45:32 2018    .
        dr--r--r--                0 Wed Sep 26 06:45:32 2018    ..
```

You can see `smbcacls` show that EVERYONE have full access, but `smbmap` show `READ ONLY` permissions.

## About impacket-smbserver

Sometimes impacket-smbserver does not work very well (you can test it in HTB machine: Sniper), which mean you can start smbserver via smbd.

1. Edit /etc/samba/smb.conf
2. Copy and paste
3. save and start service

Config like this: 

```bash
[mane]
   comment = Mane
   path = /srv/smb
   browseable = yes
   read only = no
   guest ok = yes
```

Test it in `smbclient -L <IP>`.


## smbclient download recursively

```
$ smbclient -U 'domain/user%password' '\\server\share'
mask ""
recurse ON
prompt OFF
cd 'path\to\remote\dir'
lcd '~/path/to/download/to/'
mget *

```

**Onelines**: 

```
$ smbclient '\\server\share' -N -c 'prompt OFF;recurse ON;cd 'path\to\directory\';lcd '~/path/to/download/to/';mget *'`
```










# Reference

Ref: https://www.samba.org/samba/docs/current/man-html/smbcacls.1.html
Ref: https://superuser.com/questions/856617/how-do-i-recursively-download-a-directory-using-smbclient