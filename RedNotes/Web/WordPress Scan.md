# WordPress Scan

```
$ wpscan --update
$ cat ~/.wpscan/db/metadata.json | jq -r '.plugins | keys | .[]' > plugin.list
$ ffuf -c -w plugin.list -u http://<IP>/wp-content/plugins/FUZZ -t 32

# Result put back into list.txt 

$ wpscan --url <URL> --enumerate ap --plugins-detection aggressive --plugins-list result.txt

```

## CheatSheet

```
enumerate plugins
wpscan --update --url <URL> --enumerate ap --plugins-detection aggressive

Enumerate all plugins with known vulnerabilities
wpscan --url example.com -e vp --plugins-detection mixed --api-token YOUR_TOKEN

Enumerate all plugins in our database (could take a very long time)
wpscan --url example.com -e ap --plugins-detection mixed --api-token YOUR_TOKEN

enumerate users
wpscan --url http://$_target -e u --disable-tls-checks

brute force user accounts
wpscan --url http://$_target -e u --disable-tls-checks -U users.lst -P /usr/share/wordlists/rockyou.txt

Password brute force attack
wpscan --url example.com -e u --passwords /path/to/password_file.txt

```

## Reference 
+ https://www.reddit.com/r/oscp/comments/mepugi/wordpress_enumeration_without_wpscan/