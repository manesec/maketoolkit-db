# Check Current Shell

Check current `cmd` shell or `powershell`, it's useful in command injection.

## Commmands

```cmd

(dir 2>&1 *`|echo CMD);&<# rem #>echo PowerShell

```

## Reference

https://stackoverflow.com/questions/34471956/how-to-determine-if-im-in-powershell-or-cmd