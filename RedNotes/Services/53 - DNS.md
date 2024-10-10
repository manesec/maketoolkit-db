# DNS 

## Nmap scan

```
# nmap -p53 -Pn -sV -sC 10.10.110.213
```

## NS Query

```bash
# DIG - ANY Query
$ dig any inlanefreight.htb @10.129.14.128

# DIG - AXFR Zone Transfer
$ dig axfr inlanefreight.htb @10.129.14.128

# DIG - AXFR Zone Transfer - Internal
dig axfr internal.inlanefreight.htb @10.129.14.128

# Subdomain Brute Forcing
$ for sub in $(cat /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.inlanefreight.htb @10.129.14.128 | grep -v ';\|SOA' | sed -r '/^\s*$/d' | grep $sub | tee -a subdomains.txt;done

$ gobuster dns -d inlanefreight.htb -r 10.129.203.6 -w /Tools/Wordlists/N0kovoSubdomains/n0kovo_subdomains_tiny.txt

# Auto enum
$ dnsenum --dnsserver 10.129.14.128 --enum -p 0 -s 0 -o subdomains.txt -f /opt/useful/SecLists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb

$ fierce --domain zonetransfer.me
$ ./subfinder -d inlanefreight.com -v
$ ./subbrute inlanefreight.com -s ./names.txt -r ./resolvers.txt
```