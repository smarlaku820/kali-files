# Attacking Kerberos


## AS-REQ Flow
- 1.) The client requests an Authentication Ticket or Ticket Granting Ticket (TGT).
- 2.) The Key Distribution Center verifies the client and sends back an encrypted TGT.
- 3.) The client sends the encrypted TGT to the Ticket Granting Server (TGS) with the Service Principal Name (SPN) of the service the client wants to access.
- 4.) The Key Distribution Center (KDC) verifies the TGT of the user and that the user has access to the service, then sends a valid session key for the service to the client.
- 5.) The client requests the service and sends the valid session key to prove the user has access.
- 6.) The service grants access


## Attack Privilege Requirements

- Kerbrute Enumeration - No domain access required 
- Pass the Ticket - Access as a user to the domain required
- Kerberoasting - Access as any user required
- AS-REP Roasting - Access as any user required
- Golden Ticket - Full domain compromise (domain admin) required 
- Silver Ticket - Service hash required 
- Skeleton Key - Full domain compromise (domain admin) required

## Enumeration with kerbrute

- Download kerbrute_linux_amd64 and run the userenum with provided user wordlist file
- For command reference, please check out [commands](./commands.txt)

## Harvesting & Bruteforcing with Rubeus
- Rubeus is a powerful tool for attacking Kerberos. 
- Rubeus is an adaptation of the kekeo tool and developed by HarmJ0y the very well known active directory guru.
- Rubeus has a wide variety of attacks and features that allow it to be a very versatile tool for attacking Kerberos. 
- Just some of the many tools and attacks include overpass the hash, ticket requests and renewals, ticket management, ticket extraction, harvesting, pass the ticket, AS-REP Roasting, and Kerberoasting.
- The tool has way too many attacks and features for me to cover all of them so I'll be covering only the ones I think are most crucial to understand how to attack Kerberos however I encourage you to research and learn more about Rubeus and its whole host of attacks and features here - https://github.com/GhostPack/Rubeus
- **Harvesting** - Gather tickets that are being transferred to the KDC and save them for use in other attacks such as pass the ticket attack.
- **Bruteforcing** - When bruteforcing you use a single user account and word list of potential passwords.
- **PasswordSpraying** - You depend on a single password & "spray" against all found user accounts in the domain to find which one may have that password.

## Kerberosting with rubeus & impacket
- Kerberosting allows a user to request a service ticket for any service with a registered SPN then use that ticket to crack the service password
- If the service has a registered SPN it can kerberostable however the success of the attack depends on how strong the password is.
- kerberostable accounts can be found with a tool like `BloodHound`
- As of now, you can do it with rubeus & impacket
- with impacket make use of the python script found in examples
- `sudo python3 GetUserSPNs.py controller.local/Machine1:Password1 -dc-ip 10.10.140.7 -request` - this will dump the Kerberos hash for all kerberoastable accounts it can find on the target domain just like Rubeus does; however, this does not have to be on the targets machine and can be done remotely.


## AS-REP Roasting
- Very similar to Kerberoasting, AS-REP Roasting dumps the krbasrep5 hashes of user accounts that have Kerberos pre-authentication disabled. 
- Unlike Kerberoasting these users do not have to be service accounts the only requirement to be able to AS-REP roast a user is the user must have pre-authentication disabled.
- We'll continue using Rubeus same as we have with kerberoasting and harvesting since Rubeus has a very simple and easy to understand command to AS-REP roast and attack users with Kerberos pre-authentication disabled. After dumping the hash from Rubeus we'll use hashcat in order to crack the krbasrep5 hash.
- There are other tools out as well for AS-REP Roasting such as kekeo and Impacket's GetNPUsers.py. 
- Rubeus is easier to use because it automatically finds AS-REP Roastable users whereas with GetNPUsers you have to enumerate the users beforehand and know which users may be AS-REP Roastable.
- **Overview** - During pre-authentication, the users hash will be used to encrypt a timestamp that the domain controller will attempt to decrypt to validate that the right hash is being used and is not replaying a previous request. After validating the timestamp the KDC will then issue a TGT for the user. If pre-authentication is disabled you can request any authentication data for any user and the KDC will return an encrypted TGT that can be cracked offline because the KDC skips the step of validating that the user is really who they say that they are.
- do not ever give AS-REP to any users

## Mimikatz
- Most popular & powerful post-exploitation tool commonly used for dumping user credentials inside of an active directory network. However we will be using mimikatz in order to dump a TGT from LSASS memory
- The Local Security Authority Subsystem Service (LSASS) is a memory process that stores credentials on an active directory server and can store Kerberos ticket along with other credential types to act as the gatekeeper and accept or reject the credentials provided.
- You can dump kerberos tickets from LSASS memory just like you can dump hashes.
- When you dump the tickets with mimikatz it will give you a .kirbi ticket which can be used to gain domain admin if there is domain admin ticket in the LSASS memory
- This attack is great for privilege escalation & lateral movement if there are unsecured domain service account tickets lying around.
- The attack allows you to escalate to domain admin if you dump a domain admin's ticket and then impersonate that ticket using mimikatz PTT (pass the ticket) attack allowing you to act as that domain admin. You can think of a pass the ticket attack like reusing an existing ticket were not creating or destroying any tickets here were simply reusing an existing ticket from another user on the domain and impersonating that ticket.
- Do not ever allow any domain admins to login anywhere except on the domain controller. If domain admins login it is so simple to dump the tickets and move laterally

## Mimikatz - Golden/Silver Ticket attacks
- A silver ticket can sometimes be better used in engagements rather than a golden ticket because it is a little more discreet.
- If stealth and staying undetected matter then a silver ticket is probably a better option than a golden ticket however the approach to creating one is the exact same.
- The key difference between the two tickets is that a silver ticket is limited to the service that is targeted whereas a golden ticket has access to any Kerberos service.
- A specific use scenario for a silver ticket would be that you want to access the domain's SQL server however your current compromised user does not have access to that server. You can find an accessible service account to get a foothold with by kerberoasting that service, you can then dump the service hash and then impersonate their TGT in order to request a service ticket for the SQL service from the KDC allowing you access to the domain's SQL server.
- **KRBTGT Overview** - In order to fully understand how these attacks work you need to understand what the difference between a KRBTGT and a TGT is. A KRBTGT is the service account for the KDC this is the Key Distribution Center that issues all of the tickets to the clients. If you impersonate this account and create a golden ticket form the KRBTGT you give yourself the ability to create a service ticket for anything you want. A TGT is a ticket to a service account issued by the KDC and can only access that service the TGT is from like the SQLService ticket.
- A golden ticket attack works by dumping the ticket-granting ticket of any user on the domain this would preferably be a domain admin however for a golden ticket you would dump the krbtgt ticket and for a silver ticket, you would dump any service or domain admin ticket. This will provide you with the service/domain admin account's SID or security identifier that is a unique identifier for each user account, as well as the NTLM hash. You then use these details inside of a mimikatz golden ticket attack in order to create a TGT that impersonates the given service account information.
- Access machines that you want, what you can access will depend on the privileges of the user that you decided to take the ticket from however if you took the ticket from krbtgt you have access to the ENTIRE network hence the name golden ticket; however, silver tickets only have access to those that the user has access to if it is a domain admin it can almost access the entire network however it is slightly less elevated from a golden ticket. 

## Kerberos backdoors with mimikatz
- Unlike the golden and silver ticket attacks a Kerberos backdoor is much more subtle because it acts similar to a rootkit by implanting itself into the memory of the domain forest allowing itself access to any of the machines with a master password. 
- The Kerberos backdoor works by implanting a skeleton key that abuses the way that the AS-REQ validates encrypted timestamps. A skeleton key only works using Kerberos RC4 encryption.
- The default hash for a mimikatz skeleton key is 60BA4FCADC466C7A033C178194C03DF6 which makes the password -"mimikatz"

## Installing the skeleton key with mimikatz

- example:`net use c:\\DOMAIN-CONTROLLER\admin$ /user:Administrator mimikatz` - The share will now be accessible without the need for the Administrators password
- example: `dir \\Desktop-1\c$ /user:Machine1 mimikatz` - access the directory of Desktop-1 without ever knowing what users have access to Desktop-1
- The skeleton key will not persist by itself because it runs in the memory, it can be scripted or persisted using other tools and techniques however that is out of scope for this room.

## References
- https://medium.com/@t0pazg3m/pass-the-ticket-ptt-attack-in-mimikatz-and-a-gotcha-96a5805e257a
- https://ired.team/offensive-security-experiments/active-directory-kerberos-abuse/as-rep-roasting-using-rubeus-and-hashcat
- https://posts.specterops.io/kerberoasting-revisited-d434351bd4d1
- https://www.harmj0y.net/blog/redteaming/not-a-security-boundary-breaking-forest-trusts/
- https://www.varonis.com/blog/kerberos-authentication-explained/
- https://www.blackhat.com/docs/us-14/materials/us-14-Duckwall-Abusing-Microsoft-Kerberos-Sorry-You-Guys-Don't-Get-It-wp.pdf
- https://www.sans.org/cyber-security-summit/archives/file/summit-archive-1493862736.pdf
- https://www.redsiege.com/wp-content/uploads/2020/04/20200430-kerb101.pdf
