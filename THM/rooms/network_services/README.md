# Network Services - (Vulns & thier exploitations)

We will cover, SMB/Telnet & FTP protocols.

- [SMB](./SMB.md)
- [telnet](./telnet.md)
- [FTP](./FTP.md)

## Understanding Proto
First step is to understand the protocol.

## Enumeration
- The second step is enumeration. enumeration is the process of gathering information on a target in order to find potential attack vectors and aid in exploitation.
- The process is essential for an attack to be successful.
- Enumeration can be used to gather
  - usernames
  - passwords
  - network information
  - hostnames
  - application data
  - services
  - any other information that is valuable to the attacker.
### Port Scanning
The first step of Enumeration is Port Scanning. You do that with NMAP.

## Exploitation
- Relating to exploits check nmap sce's & cve details for a specific version.
- CVE stands for common vulnerabilities and exposures and is a list of publicly disclosed computer security flaws.
- There is a CVE number attached to a CVE(or security flaw)
- However, relating to exploits you will often find a mis-configuration that will help to exploit the service.
- It is possible to get reverse shells exploiting these vulns or mis-configs

### Reverse Shell
Reverse shell is a type of shell in which the target machine communicates with the attacking machine. The attacking machine has a listening port on which it receives connection, resulting in code or command execution being achieved.

Attackers machine  <-------------------   Victims Machine
Listen Port: 4444                          IP: 192.168.1.3
IP: 192.168.1.25

You can start a tcpdump session to listen for traffic.

## Tools
- msfvenom
- hydra

## References

- [CVE Details](https://www.cvedetails.com)
- [Mitre CVE](https://mitre.cve.org)
- [Exploiting simple network services in CTF](https://gregit.medium.com/exploiting-simple-network-services-in-ctfs-ec8735be5eef)
- [Exploiting remote services](https://attack.mitre.org/techniques/T1210/)
- [NSA Warns of Vulns in VPN services](https://www.nextgov.com/cybersecurity/2019/10/nsa-warns-vulnerabilities-multiple-vpn-services/160456/)
