# Firewall Testing

test callback port.



# Host
```
sudo tcpdump -i tun0 src 10.10.110.250 -w save.pcap -v
```

# victim

```
.\rustscan -t 1500 -a 10.10.16.127 --tries 2 --range 1-65535


```