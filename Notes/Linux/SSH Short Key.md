#! SSH Short Key

Master key: `~` 

## Enable command line in config

edit file: `~/.ssh/config` 
add `EnableEscapeCommandline=yes`

## Usage

`~C`

```bash
[security@haystack ~]$ (~C)
ssh> -L 127.0.0.1:5601:127.0.0.1:5601
Forwarding port.
```