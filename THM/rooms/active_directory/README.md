# Attackative Directory

- 99% of corporate networks run off AD. But can you exploit a vulnerable domain controller
- You need some tools to be able to do the job
  - neo4j
  - bloodhound
  - impacket


## Enumeration
- Basic enum starts with an nmap scan
- `Enum4Linux` is a pentesting tool used for enumerating NETBIOS(139)/SMB(445)


## Enumerating Users via Kerberos
- A whole host of services are running including kerberos.
- kerberos is a *key authentication* service within Active Directory.
- With this port open we can use a tool called `Kerbrute`. You can download it from [here](https://github.com/ropnop/kerbrute/releases) to brute force discovery of users, passwords and even password spray!
- Kerbrute when performing enumeration of user accounts will generate windows log events (#4768) if kerberos logging is enabled. During this enumeration process, kerberos sends TGT requests with no pre-authentication. If the KDC responds with a PRINCIPAL UNKNOWN error, the username does not exist. If the KDC prompts for pre-authentication, we know the username exists & we move on. This does not cause any login failures so it will not lock out any account.

## Abusing Kerberos
- After the enumeration of user accounts is finished, we can attempt to abuse a feature within Kerberos with an attack method called ASREPRoasting. ASReproasting occurs when a user account has the privilege "Does not require Pre-Authentication" set. This means that the account does not need to provide valid identification before requesting a Kerberos Ticket on the specified user account.
-  Impacket has a tool called "GetNPUsers.py" (located in impacket/examples/GetNPUsers.py) that will allow us to query ASReproastable accounts from the Key Distribution Center. The only thing that's necessary to query accounts is a valid set of usernames which we enumerated previously via Kerbrute. This will help us with getting a kerberos hash and cracking it would open new doors.
- We can use smbclient to list shares and see if some sensitive files are hidden there
- Once you obtain further credentials and especially if you find spooksec.local\backup then it means you can abuse impacket secretsdump.py script to get all the user credentials
