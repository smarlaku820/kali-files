# Network Services - SMB

## understanding SMB
- client & server communication protocol
- sharing access to files/printers/serial ports & other resources on the network.
- servers make filesystems and other resources (printers, named pipes and api's) available to clients.
- client connect to server on tcp/ip over netbios as specified in `RFC1001` and `RFC1002`,NetBEUI or IPX/SPX.
- once connection is established, smb commands are sent by the client to access resources.
- smb is run by MS windows OS's since Windows95 have included client & server SMB protocol support.
- smb is a `response-request` protocol.
- `samba` an open source server that supports SMB protocol for unix systems.

## Enumerating SMB
- In the process of enumeration you will look out for SMB share drives. These are usually connected to by the client to gain access.
- Its a great starting point to find out sensitive information.
- Do a port scan first with NMAP to find info about OS,services etc.,
- `Enum4linux` is a tool used to enumerate SMB shares on both Windows and Linux Systems. Its a wrapper around samba package.
- From this you know, SMB share location and interesting SMB shares

## Exploiting SMB
- While there are vulns that can allow remote code execution, you can exploit just a mis-configuration to get a reverse shell.
- Now do a smbclient.
```
smbclient //10.10.64.71/profiles -U Anonymous -p 445
```
- Check out .ssh directory
- Check out for any private keys
- Download them with mget
- Check out for other sensitive files
