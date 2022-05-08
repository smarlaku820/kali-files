# Tools for receiving Reverse Shells and sending Bind Shells.


## Netcat

- netcat is a networking swiss army knife.
- it can grab banners during enumeration
- it can be used to receive reverse shells from a target system.
- it can be used to connect to remote ports attached to bind shells on a target system.
- netcat shells are unstable but can be improved by certain techniques.

## Socat

- socat is like netcat on steroids
- it can do all the things that netcat does and many more
- socat shells are stable shells.
- There are couple of caveats
  - syntax is more difficult
  - socat is not included usually.

Both socat & netcat have .exe versions on windows.

## Metasploit - multi/handler

- the `auxiliary/multi/handler` module of metasploit framework is like socat and netcat.
- they can be used to receive reverse shells
- they are very stable and have lot of options.
- its the only way to interact with a `meterpreter` shell, and is the easiest way to handle staged payloads.

## Msfvenom

- Like `multi/handler`, `msfvenom` is part of metasploit framework. However it is shipped as a standalone tool.
- `Msfvenom` is used to generate payloads on the fly.
- this generates payloads other than reverse and bind shells

## webshells
- kali linux comes with wide variety of webshells located at `/usr/share/webshells`

## Other imporatnt references
- [Seclists Repo - Code for shells](https://github.com/danielmiessler/SecLists)
- [Payloads_all_things](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md)
- [PentestMonkey - ReverseShell CheatSheet](https://web.archive.org/web/20200901140719/http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
