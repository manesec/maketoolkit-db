# SSH Key files

```
By default, SSH searches for id_rsa, id_ecdsa, id_ecdsa_sk, id_ed25519, id_ed25519_sk, and id_dsa files. The keys do not have to be named like this, you can name it mykey just as well, or even place it in a different directory. However, if you do either of those, then you need to explicitly reference the key in the ssh command like so:
```

## Check private key with who?

```
$ ssh-keygen -f id_rsa -y
```

## Force key auth

```
$ ssh -v -p 2222 -i id_rsa  root@10.129.23.64   -o PasswordAuthentication=no 
```