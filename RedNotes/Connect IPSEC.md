# A example for connect IPSEC.

Just simple note for ipsec connection.

## 0x0 Install strongswan

```bash
$ sudo apt install strongswan
```

## 0x1 Add secret key in `/etc/ipsec.secrets`

```bash
$ man ipsec.secrets

   # /etc/ipsec.secrets ? strongSwan IPsec secrets file
              192.168.0.1 %any : PSK "v+NkxY9LLZvwj4qCC2o/gGrWDF2d21jL"
```

and copy it in `/etc/ipsec.secrets`

```bash
$ vim /etc/ipsec.secrets

192.168.0.1 %any : PSK "PASSWORD"
```

## 0x2 Get IPSEC Config

```bash
# Stop to run strongswan to free UDP:500 port.
$ systemctl stop strongswan-starter

# Because ike-scan require bind UDP:500 port.
$ ike-scan  -M 10.129.228.122

Starting ike-scan 1.9.5 with 1 hosts (http://www.nta-monitor.com/tools/ike-scan/)
10.129.228.122  Main Mode Handshake returned
        HDR=(CKY-R=aa5d52d2a86c856f)
        SA=(Enc=3DES Hash=SHA1 Group=2:modp1024 Auth=PSK LifeType=Seconds LifeDuration(4)=0x00007080)
        VID=1e2b516905991c7d7c96fcbfb587e46100000009 (Windows-8)
        VID=4a131c81070358455c5728f20e95452f (RFC 3947 NAT-T)
        VID=90cb80913ebb696e086381b5ec427b1f (draft-ietf-ipsec-nat-t-ike-02\n)
        VID=4048b7d56ebce88525e7de7f00d6c2d3 (IKE Fragmentation)
        VID=fb1de3cdf341b7ea16b7e5be0855f120 (MS-Negotiation Discovery Capable)
        VID=e3a5966a76379fe707228231e5ce8652 (IKE CGA version 1)

Ending ike-scan 1.9.5: 1 hosts scanned in 0.109 seconds (9.14 hosts/sec).  1 returned handshake; 0 returned notify
```

`SA=(Enc=3DES Hash=SHA1 Group=2:modp1024 Auth=PSK LifeType=Seconds LifeDuration(4)=0x00007080)` should be the config.

`0x7080` = 28800 seconds = 8h

## 0x3 Use IPSEC config

```bash
vim /etc/ipsec.secrets

conn Testing
  type=transport
  keyexchange=ikev1
  left=10.10.16.8
  leftprotoport=tcp
  right=10.129.228.122
  rightprotoport=tcp
  authby=psk
  esp=3des-sha1
  ike=3des-sha1-modp1024
  ikelifetime=8h
  auto=start
```

See: `man ipsec.conf`

## 0x4 Testing connection
In nmap, if using `-sS` options, ipsec Tunnel will drops incomplete tcp requests.

```bash
$ sudo nmap -sS -p 445 -Pn 10.129.228.122
[sudo] password for mane:
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-13 22:09 CST
Nmap scan report for 10.129.228.122
Host is up.

PORT    STATE    SERVICE
445/tcp filtered microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 2.10 seconds
```

So, you need to use full tcp requests with `-sT` options.


```bash
$ nmap -sT -p 445 -Pn 10.129.228.122
Starting Nmap 7.94 ( https://nmap.org ) at 2023-12-13 22:11 CST
Nmap scan report for 10.129.228.122
Host is up (0.11s latency).

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Nmap done: 1 IP address (1 host up) scanned in 0.15 seconds
```

## Reference

https://www.youtube.com/watch?v=1ae64CdwLHE
