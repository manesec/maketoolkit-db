
# Change User Password Without Powerview

```
$SecurePassword = ConvertTo-SecureString 'P0werByM@nE' -AsPlainText -Force
Set-ADAccountPassword -Identity mane -Reset -NewPassword $SecurePassword 
```