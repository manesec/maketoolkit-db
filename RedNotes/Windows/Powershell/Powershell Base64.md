# Powershell Base64

To make a powershell base64 enc on linux, just run command:

```bash
echo -n '<base64_enc>' | iconv -f UTF8 -t UTF16LE | base64 -w 0
```

see: https://stackoverflow.com/questions/22768021/different-output-between-powershell-tobase64string-linux-base64