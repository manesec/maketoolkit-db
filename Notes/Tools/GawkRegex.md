# Gawk Regex

From: [regex - AWK: Access captured group from line pattern - Stack Overflow](https://stackoverflow.com/questions/2957684/awk-access-captured-group-from-line-pattern)

With gawk, you can use the `match` function to capture parenthesized groups.

```dart
gawk 'match($0, pattern, ary) {print ary[1]}' 
```

example:

```bash
echo "abcdef" | gawk 'match($0, /b(.*)e/, a) {print a[1]}' 
```

outputs `cd`.


