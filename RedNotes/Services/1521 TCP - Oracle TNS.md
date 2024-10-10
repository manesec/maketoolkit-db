# 1521 TCP - Oracle TNS

TCP/1521

Each database or service has a unique entry in the [tnsnames.ora](https://docs.oracle.com/cd/E11882_01/network.112/e10835/tnsnames.htm#NETRF262) file, containing the necessary information for clients to connect to the service.

In short, the client-side Oracle Net Services software uses the `tnsnames.ora` file to resolve service names to network addresses,

the listener uses the `listener.ora` file to determine what service need to listen.

## Enumlation

In Kali, just `sudo apt install odat`.

```
# dont forget to sudo 
$ sudo odat all -s <server ip>
```

**Upload file via odat**

```
$ echo "webshell" > testing.txt
$ ./odat.py utlfile -s <TargetIP> -d <SIDS> -U <username> -P <password> --sysdba --putFile C:\\inetpub\\wwwroot testing.txt ./testing.txt
```


## Nmap Bruteforce

```
$sudo nmap -p1521 -sV <server ip> --open --script oracle-sid-brute
```

## sqlplus

```
$ sudo apt install oracle-instantclient-sqlplus
```

Solve for `sqlplus: error while loading shared libraries: libsqlplus.so: cannot open shared object file: No such file or directory`

```
$ sudo sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf";sudo ldconfig
```

How to Connect 

```
$ sqlplus <username>/<password>@<Target IP>/<SIDS>
$ sqlplus <username>/<password>@<Target IP>/<SIDS> as sysdba
```

Example SQL Command

```sql
SQL> select * from user_role_privs;
SQL> select table_name from all_tables;
SQL> select name, password from sys.user$;
```


## Reference 

+ Hackthebox Academy - Footprinting - Oracle TNS