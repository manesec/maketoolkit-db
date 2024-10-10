# Csharp Random

About the CSharp random, It's time-based random.

``` C#
public static void Main(string[] args)
{
    file = "testing"
    FileInfo fileInfo = new FileInfo(file);
    string destFile = Path.ChangeExtension(fileInfo.Name, ".enc");
    long value = DateTimeOffset.Now.ToUnixTimeSeconds();
    Random random = new Random(Convert.ToInt32(value));
    byte[] array = new byte[16];
    random.NextBytes(array);
    byte[] array2 = new byte[32];
    random.NextBytes(array2);
    byte[] array3 = AES.EncryptFile(fileInfo.Name, destFile, array2, array);
}
```

When you know the time from file, you can get the random numbers.

Time can use UNIX-TIME.

``` C# 
using System;
using System.IO;
using System.Security.Cryptography;

int value = 1600000000;
Random random = new Random(value);
byte[] array = new byte[16];
random.NextBytes(array);
Console.WriteLine(BitConverter.ToString(array));
byte[] array2 = new byte[32];
random.NextBytes(array2);
Console.WriteLine(BitConverter.ToString(array2));
```

When you have get `Key` and `IV` :

Mode can choose `CBC`, and INPUT, OUTPUT choose `RAW`