### This is where we understand commands in different OS to play with SHA256

## This is how you encode a text to its appropriate SHA256 hash

# Windows
```
[BitConverter]::ToString([Security.Cryptography.HashAlgorithm]::Create('SHA256').ComputeHash([Text.Encoding]::UTF8.GetBytes('YourTextHere'))).Replace('-','').ToLower()
```

```cmd
echo -n "YourTextHere" | openssl dgst -sha256
```

# Linux
```bash
echo -n "YourTextHere" | sha256sum
```

# MacOS
```bash
echo -n "YourTextHere" | shasum -a 256
```

## Now let us explore how to do the reverse. SHA256 to plain_text so we need to decode now

# Hashcat operates in different modes, for our purpose we will use '-m 1400' which is SHA-256.

# Windows
We use MSYS tool as we do not have many native functions available (in our case it would be the "make" command).

After cloning the hashcat repo and deps/OpenCL repo we run this command to retrieve the hashes.

```bash
./hashcat -m 1400 -a 3 -O -w 3 -1 ?l?u?d 0c1a617ba75feb14d9ef2cec35864a6ca2bfeeecacad774c9d1d4b42b52198cf ?1?1?1?1?1?1
```
-m 1400: Indicates you're cracking an SHA-256 hash.
-a 3: Specifies a mask attack. A mask attack is used when you want to specify a particular pattern of characters you think the password might follow, allowing for faster brute force of that pattern.
-O: Enables optimized kernels.
-w 3: Sets the highest workload setting.
-1 ?l?u?d: Custom charset for lowercase (?l), uppercase (?u), and digits (?d).
?1?1?1?1?1?1 - because we know that the length of the plaintext is 6.

# The other method we can use is called John the Ripper
```bash
john hash.txt
```

## Hashcat in general is faster than John as it uses GPU instead of CPU.
## John has more complexity and if need to break complex stuff, John is a better option.