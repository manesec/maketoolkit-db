# 623 UDP - IPMI 

UDP/623

> IPMI is a series of specifications that provide standardized interfaces to the so-called “platform management” services. In this context, the term “Platform Management” refers to monitoring hardware (system temperatures, fans, power supplies and so forth), their control (booting and shutting down the server) and the documentation (logging) of “out-of-range” states. IPMI was developed by Intel, Hewlett Packard, NEC and Dell.
>
> https://www.thomas-krenn.com/en/wiki/IPMI_Basics

## Detect Version

```
$ sudo nmap -sU --script ipmi-version -p 623 <target>

msf6 > use auxiliary/scanner/ipmi/ipmi_version 
```

## Dumping Hashes

```
msf6 > use auxiliary/scanner/ipmi/ipmi_dumphashes 
```

Crack hash

```
$ hashcat -m 7300 ipmi.txt -a 3 ?1?1?1?1?1?1?1?1 -1 ?d?u
```

## Reference
+ https://www.thomas-krenn.com/en/wiki/IPMI_Basics
+ Hackthebox Academy - Footprinting - IPML