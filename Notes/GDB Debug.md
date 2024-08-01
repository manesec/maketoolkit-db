# GDB Debug 


## Write Data

+ https://en.cppreference.com/w/cpp/language/types
+ https://www.tutorialspoint.com/cplusplus/cpp_data_types.htm

change memory: `set *((uint64_t *) ($rbp-0x10) ) = 0x1234`


## Show some data

```
pwndbg> help x
Examine memory: x/FMT ADDRESS.
ADDRESS is an expression for the memory address to examine.
FMT is a repeat count followed by a format letter and a size letter.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),
  t(binary), f(float), a(address), i(instruction), c(char), s(string)
  and z(hex, zero padded on the left).
Size letters are b(byte), h(halfword), w(word), g(giant, 8 bytes).
The specified number of objects of the specified size are printed
according to the format.  If a negative number is specified, memory is
examined backward from the address.
```

```
x/10x $rip
```

## Watch and print (PWNDBG)

```
cwatch execute "x/20x $rsp"
contextwatch execute "<command>"
```

## GDB conditional breakpoints 
you need to make a breakpoints frist and add condition

```
break your_function
condition <breakpoint-number> $rdx == 666666
```

```
# break all syscall
catch syscall
catch syscall read
```


## Script for GDB (example)

```
start
break *main+606
commands
  silent

  # get data from xxx
  set $local_variable = *(unsigned long long*)($rbp-0x18)
  printf "[Mane] Current value: %llx\n", $local_variable

  # write data in xxx
  set *((uint64_t *) ($rbp-0x10) ) = $local_variable

  # skip scanf example
  set $rip = $rip + 24 
  continue
end
continue

```

and using 

```
pwndbg> source xxx.gdb
```


## gdb and pwntools

```python
from pwn import *

context.terminal = ['tmux', 'new-window']

gdbCommand = '''
invoke-pwndbg
b *challenge + 1540
'''

process = gdb.debug(filename ,aslr=False, gdbscript=gdbCommand)
```