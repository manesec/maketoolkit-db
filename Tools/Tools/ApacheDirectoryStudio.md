# Apache Directory Studio Search

LDAP search, filter search for ldap.

Select `LDAP` -> `New Search...` -> Edit `Filter` 

## Query

Query user:`(objectClass=user)` or `(userPrincipalName=*)`

Query group: `(objectClass=group)`

## User Naming Attributes

- [userPrincipalName](https://docs.microsoft.com/en-us/windows/win32/ad/naming-properties#userprincipalname) — the logon name for the user
- [objectGUID](https://docs.microsoft.com/en-us/windows/win32/ad/naming-properties#objectguid) — the unique identifier of a user
- [sAMAccountName](https://docs.microsoft.com/en-us/windows/win32/ad/naming-properties#samaccountname) — a logon name that supports previous version of Windows
- [objectSid](https://docs.microsoft.com/en-us/windows/win32/ad/naming-properties#objectsid) — security identifier (SID) of the user
- [sIDHistory](https://docs.microsoft.com/en-us/windows/win32/ad/naming-properties#sidhistory) — the previous SIDs for the user object

## Link

[User Naming Attributes - Win32 apps | Microsoft Docs](https://docs.microsoft.com/en-us/windows/win32/ad/naming-properties)
