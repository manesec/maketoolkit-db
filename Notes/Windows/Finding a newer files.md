# Finding a newer files.


Time can sort by : `CreationTime`,  `CreationTimeUtc`, `LastAccessTime`,  `LastAccessTimeUtc`, `LastWriteTime`, `LastWriteTimeUtc`

## Powershell Command

```bash

(gci C:\ -r | sort -Descending LastWriteTime | select -first 100) | Select-Object -Property LastWriteTime,FullName

```