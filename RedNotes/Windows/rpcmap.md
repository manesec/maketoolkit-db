# MS RPC Brute Force

August 28, 2022 by manesec.

## MS-DCOM

```bash
$ impacket-rpcmap "ncacn_ip_tcp:10.129.96.60" -brute-uuids -brute-opnums -opnum-max 5
Protocol: [MS-DCOM]: Distributed Component Object Model (DCOM) Remote
Provider: rpcss.dll
UUID: 99FCFEC4-5260-101B-BBCB-00AA0021347A v0.0
Opnum 0: rpc_x_bad_stub_data
Opnum 1: rpc_x_bad_stub_data
Opnum 2: rpc_x_bad_stub_data
Opnum 3: success
Opnum 4: rpc_x_bad_stub_data
Opnum 5: success
```

If the Protocol is `MS-DCOM` and uuid is `99FCFEC4-5260-101B-BBCB-00AA0021347A`, it allow use `IOXIDResolver` interface to get machine IP via Opnum 5 which is `ServerAlive2()` method.

The tools: [GitHub - mubix/IOXIDResolver: IOXIDResolver.py from AirBus Security](https://github.com/mubix/IOXIDResolver)



Ref: https://medium.com/nets3c/remote-enumeration-of-network-interfaces-without-any-authentication-the-oxid-resolver-896cff530d37