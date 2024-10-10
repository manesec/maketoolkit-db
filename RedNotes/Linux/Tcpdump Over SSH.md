# Tcpdump Over SSH Tunnel

This is note by manesec.

Sometimes remote machines without wireshark become very useful :)

## Usage

```bash
ssh user@remote_ip /sbin/tcpdump -i ens160 -U -s0 -w - | wireshark -k -i -

# exclude ssh traffic
ssh user@remote_ip /sbin/tcpdump -i ens160 -U -s0 -w - 'port not 22' | wireshark -k -i -

ssh user@remote_ip tcpdump -i any -U -s0 -w - 'port not 22' | wireshark -k -i -
```

And then wireshark will be open.