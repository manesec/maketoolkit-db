# Founding Credit

Some notes from HTB Acadme, Password Attacks. 

## Founding Credit

```
# Files	    
Configs	    
Databases	
Notes		
Scripts		
Source codes
Cronjobs	
SSH Keys	

# History	         
Logs	             
Command-line History

# Memory
Cache
In-memory Processing

# Key-Rings
Browser stored credentials
```


## Finding Credit from command

```bash
# Configuration Files
$ for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done

# Credentials in Configuration Files
$ for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc\|lib");do echo -e "\nFile: " $i; grep "user\|password\|pass" $i 2>/dev/null | grep -v "\#";done

# Database
$ for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share\|man";done

# Notes
$ find /home/* -type f -name "*.txt" -o ! -name "*.*"

# Scripts
$ for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done

# SSH - Private KEY
$ grep -rnw "PRIVATE KEY" /home/* 2>/dev/null | grep ":1"#
$ grep -rnw "PRIVATE KEY" /* 2>/dev/null | grep ":1"

# SSH - Public Key
$ grep -rnw "ssh-rsa" /home/* 2>/dev/null | grep ":1"

# SSH - Encrypted SSH Keys
$ cat /home/cry0l1t3/.ssh/SSH.private

# script history
$ tail -n5 /home/*/.*_history

# Hunting Logs
$ for i in $(ls /var/log/* 2>/dev/null);do GREP=$(grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null); if [[ $GREP ]];then echo -e "\n#### Log file: " $i; grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null;fi;done

# Hunting for Encoded Files
$ for ext in $(echo ".xls .xls* .xltx .csv .od* .doc .doc* .pdf .pot .pot* .pp*");do echo -e "\nFile extension: " $ext; find / -name *$ext 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done

```
