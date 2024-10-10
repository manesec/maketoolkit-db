# Find Cheatsheet

Write by mane.

```bash
# Found Readable directory and sort by time.  (depth = 4)
$ find / -type d -maxdepth 4 -readable -printf "%T@ %Tc | %p \n" 2>/dev/null | grep -v "| /proc" | grep -v "| /dev" | grep -v "| /run" | grep -v "| /var/log" | grep -v "| /boot"  | grep -v "| /sys/" | sort -n -r

$ find / -type d -maxdepth 4   -not -path "/proc/*"  -not -path "/run/*"  -not -path "/dev/*"  -not -path "/usr/lib/*"  -not -path "/usr/share/*"  -not -path "/usr/src/*"   -not -path "/snap/*"  -not -path "/var/lib/*"  -not -path "/var/cache/*"  -not -path "/var/snap/*"    -not -path "/var/log/*"  -not -path "/boot/*"  -not -path "/sys/*"  -readable -printf "%T@ %Tc | %p \n" 2>/dev/null 

# Found Writable directory and sort by time.  (depth = 10)
$ find / -type d -maxdepth 10 -writable -printf "%T@ %Tc | %p \n" 2>/dev/null | grep -v "| /proc" | grep -v "| /dev" | grep -v "| /run" | grep -v "| /var/log" | grep -v "| /boot"  | grep -v "| /sys/" | sort -n -r

$ find / -type d -maxdepth 10   -not -path "/proc/*"  -not -path "/run/*"  -not -path "/dev/*"  -not -path "/usr/lib/*"  -not -path "/usr/share/*"  -not -path "/usr/src/*"   -not -path "/snap/*"  -not -path "/var/lib/*"  -not -path "/var/cache/*"  -not -path "/var/snap/*"    -not -path "/var/log/*"  -not -path "/boot/*"  -not -path "/sys/*"  -writable -printf "%T@ %Tc | %p \n" 2>/dev/null 

# Or Found Own by Current User and sort by time. (depth = 10)
$ find / -maxdepth 10 -user $(id -u) -printf "%T@ %Tc | %p \n" 2>/dev/null | grep -v "| /proc" | grep -v "| /dev" | grep -v "| /run" | grep -v "| /var/log" | grep -v "| /boot"  | grep -v "| /sys/" | sort -n -r

# Or Found Own by Current Group ID and Sort by time. (depth = 10)
$ find / -maxdepth 10 -group $(id -g) -printf "%T@ %Tc | %p \n" 2>/dev/null | grep -v "| /proc" | grep -v "| /dev" | grep -v "| /run" | grep -v "| /var/log" | grep -v "| /boot"  | grep -v "| /sys/" | sort -n -r

# Found Newer files and sort by time. (depth = 5)
$ find / -maxdepth 5 -printf "%T@ %Tc | %p \n" 2>/dev/null | grep -v "| /proc" | grep -v "| /dev" | grep -v "| /run" | grep -v "| /var/log" | grep -v "| /boot"  | grep -v "| /sys/" | sort -n -r | less

$ find / -maxdepth 5 -not -path "/proc/*"  -not -path "/run/*"  -not -path "/dev/*"  -not -path "/usr/lib/*"  -not -path "/usr/share/*"  -not -path "/usr/src/*"   -not -path "/snap/*"  -not -path "/var/lib/*"  -not -path "/var/cache/*"  -not -path "/var/snap/*"    -not -path "/var/log/*"  -not -path "/boot/*"  -not -path "/sys/*" -printf "%T@ %Tc | %p \n" 2>/dev/null  | sort -n -r | less

$ find /etc -printf "%T@ %Tc | %p \n" 2>/dev/null  | sort -n -r | less

# Found Newer files only and sort by time. (depth = 5)
$ find / -maxdepth 5 -type f -printf "%T@ %Tc | %p \n" 2>/dev/null | grep -v "| /proc" | grep -v "| /dev" | grep -v "| /run" | grep -v "| /var/log" | grep -v "| /boot"  | grep -v "| /sys/" | sort -n -r | less

$ find / -maxdepth 5 -type f -not -path "/proc/*"  -not -path "/run/*"  -not -path "/dev/*"  -not -path "/usr/lib/*"  -not -path "/usr/share/*"  -not -path "/usr/src/*"   -not -path "/snap/*"  -not -path "/var/lib/*"  -not -path "/var/cache/*"  -not -path "/var/snap/*"    -not -path "/var/log/*"  -not -path "/boot/*"  -not -path "/sys/*" -printf "%T@ %Tc | %p \n" 2>/dev/null  | sort -n -r | less

# Found Newer directory only and sort by time. (depth = 5)
$ find / -maxdepth 5 -type d -printf "%T@ %Tc | %p \n" 2>/dev/null | grep -v "| /proc" | grep -v "| /dev" | grep -v "| /run" | grep -v "| /var/log" | grep -v "| /boot"  | grep -v "| /sys/" | sort -n -r | less

$ find / -maxdepth 5 -type d -not -path "/proc/*"  -not -path "/run/*"  -not -path "/dev/*"  -not -path "/usr/lib/*"  -not -path "/usr/share/*"  -not -path "/usr/src/*"   -not -path "/snap/*"  -not -path "/var/lib/*"  -not -path "/var/cache/*"  -not -path "/var/snap/*"    -not -path "/var/log/*"  -not -path "/boot/*"  -not -path "/sys/*" -printf "%T@ %Tc | %p \n" 2>/dev/null  | sort -n -r | less

# All Hidden Files
$ find / -type f -name ".*" -user $(id -u) -ls 2>/dev/null 

$ find / -type f -name ".*" -not -path "/sys/*" -not -path "/snap/*" -not -path "/usr/src/*" -not -path "/proc/*"  2>/dev/null

# Capabilities
$ find /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin -type f -exec getcap {} \;

# Find SUID set files.
$ find / -perm /u=s -ls 2>/dev/null

$ find / -user root -perm -4000 -exec ls -ldb {} \; 2>/dev/null

$ find / -user root -perm -6000 -exec ls -ldb {} \; 2>/dev/null

# Find SGID set files.
$ find / -perm /g=s -ls 2>/dev/null

# All Hidden Dir
$ find / -type d -name ".*" -user $(id -u) -ls 2>/dev/null 

# All .git repo
$ find / -type f -name ".git"  2>/dev/null

# history files
$ find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null

# Founding sh files
$ find / -not -path '/snap/*' -not -path '/usr/src/*' -not -path '/usr/share/*' -not -path '/usr/lib/python3/*' -type f -name "*.sh" 2>/dev/null

# Founding id_rsa
$ find / -iname "*id_rsa*"  2>/dev/null ; find / -iname "*id_ecdsa*" 2>/dev/null ; find / -iname "*id_ecdsa_sk*" 2>/dev/null ; find / -iname "*id_ed25519*"  2>/dev/null ; find / -iname "*id_ed25519_sk*"  2>/dev/null ; find / -iname "*id_dsa*"  2>/dev/null

$ find / -iname "*id_rsa*"  2>/dev/null
$ find / -iname "*id_ecdsa*" 2>/dev/null
$ find / -iname "*id_ecdsa_sk*" 2>/dev/null
$ find / -iname "*id_ed25519*"  2>/dev/null
$ find / -iname "*id_ed25519_sk*"  2>/dev/null
$ find / -iname "*id_dsa*"  2>/dev/null
```

