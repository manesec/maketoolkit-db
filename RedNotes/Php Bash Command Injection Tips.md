# Php Bash Command Injection Tips

Let's see the example code, 

```php
<?php
$res=0;
if (isset($_GET['ip']) && $_GET['ip']) {
    $ip = $_GET['ip'];
    $m=[];
    if (!preg_match_all("/(\||&|;| |\/|cat|flag)/", $ip, $m)) {
        $cmd = "ping -c 4 {$ip}";
        exec($cmd,$res);
    }else{
        $res=$m;
    }
    if ($res) {
            print_r($res);
        }
}
?>
```

The code show that it filtered:  `|` `&` `;` `<space>` `/` `cat` `flag`

## Bypass

To bypass the space, you can input url encode like `%09` (as `<Tab>` char).

And `%0a will be <enter> char`.

## Example

`?ip=localhost%0Als`

## Reference

https://blog.csdn.net/qq_45655564/article/details/117395152