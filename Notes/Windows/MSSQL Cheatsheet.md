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
