# Docker Container

Write by manesec.

## 0x1 Check IP

+ `hostname -I` , You can get the container IP address.

## 0x2 Privilege escalation with special permissions

There are some containers that give some special permissions, and then go through this permission to escalation.

See：[Capabilities Abuse Escape](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/docker-breakout/docker-breakout-privilege-escalation#capabilities-abuse-escape)

In other words container can attempt to escalation need to have one of following permissions: `CAP_SYS_ADMIN`, `CAP_SYS_PTRACE`, `CAP_SYS_MODULE`, `DAC_READ_SEARCH`, `DAC_OVERRIDE`, `CAP_SYS_RAWIO`, `CAP_SYSLOG`, `CAP_NET_RAW`, `CAP_NET_ADMIN`.

You can use the command `capsh --print` to check the permissions of the container, in many cases will not be installed.

The manual way is :

```bash
# In container
$ cat /proc/self/status
CapInh: 0000000000000000
CapPrm: 00000000a80425fd
CapEff: 00000000a80425fd
CapBnd: 00000000a80425fd
CapAmb: 0000000000000000

# In your host
$ capsh --decode=00000000a80425fd
0x00000000a80425fd=cap_chown,cap_dac_read_search,cap_fowner,cap_fsetid,cap_kill,cap_setgid,cap_setuid,cap_setpcap,cap_net_bind_service,cap_net_raw,cap_sys_chroot,cap_mknod,cap_audit_write,cap_setfcap

```

See: [Linpeas.sh](https://github.com/carlospolop/PEASS-ng/blob/e36d5a57363fa6acf0d7daa69ca89dd8add6a847/linPEAS/builder/linpeas_parts/2_container.sh#LL391C15-L391C15)


Privilege escalation method can be referred to [Linux Capabilities](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/linux-capabilities#cap_sys_admin)





