# Event Tracing for Windows (ETW)


## Query ETW Provider

```powershell
logman.exe query -ets

logman.exe query "EventLog-System" -ets

logman.exe query providers
logman.exe query providers | findstr "Winlogon"

logman.exe query providers Microsoft-Windows-Winlogon

Get-WinEvent -ListProvider * | Format-Table -AutoSize

```


## Useful Providers

# Reference 

+ https://blog.palantir.com/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63
