# RBash Escape

## Show support command

```
$ compgen -c
```

## Echo to show files

```
htb-user@ubuntu:~$ echo ./*
./bin ./flag.txt

htb-user@ubuntu:~$ echo ./bin/*
./bin/man

htb-user@ubuntu:~$ echo $(<flag.txt)
```

## read printf

```bash
while IFS= read -r line
do
    printf '%s\n' "$line"
done < "flag.txt"
```


## Reference
Please Read the reference.

+ https://0xffsec.com/handbook/shells/restricted-shells/

+ https://www.exploit-db.com/docs/english/44592-linux-restricted-shell-bypass-guide.pdf