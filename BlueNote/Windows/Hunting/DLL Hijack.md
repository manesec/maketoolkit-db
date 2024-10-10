# Dll Hijack

need to setup sysmon, sysmon log, event id `7` : 

`ImageLoaded` 


## Powershell


```powershell 
Get-WinEvent -FilterHashtable @{Path='C:\Logs\DLLHijack\DLLHijack.evtx'; ID=7} -MaxEvents 10 | ForEach-Object {
    $message = $_.Message
    # 使用正則表達式提取 Image 和 ImageLoaded 的值
    if ($message -match 'Image:\s*(.+?)\s*ImageLoaded:\s*(.+)') {
        $image = $matches[1]
        $imageLoaded = $matches[2]
        # 輸出格式化的字符串
        "$image - $imageLoaded"
    }
}
```