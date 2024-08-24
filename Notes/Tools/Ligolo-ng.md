# ligolo-ng

```
$ ./proxy -laddr 0.0.0.0:80 -selfcert
```

```
$ sudo ip link del ligolo
$ sudo ip tuntap add user [your_username] mode tun ligolo
$ sudo ip link set ligolo up
$ sudo ip route add 192.168.0.0/24 dev ligolo
$ sudo ip route add 240.0.0.1/32 dev ligolo
```

```
$ ./agent -connect xxx:80 -ignore-cert -retry
```