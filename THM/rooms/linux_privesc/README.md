# Common Linux Privilege Escalation Vulnerabilities and Techniques

## What is privilege escalation ?

- Privilege escalation usually involves going from a lower permission to a higher permission.
- More technically its an
  - exploitation of a vulnerability
  - exploitation of a design flaw or configuration oversight
- to gain unauthorized access to resources that are usually restricted from the users.

## Why is it important ?
- you can reset passwords 
- you can bypass access controls to compromise protected data
- edit software configurations
- enable persistence, so you can access machine later
- change privilege of users
- get that cheeky root flag ;)

## Privilege Tree



                                                 Administrator
                                                      ^
                                                      | Vertical Privesc
                                                      |
                             Normal User 1 ----> Normal User 2 ----> Normal User 3
                                           
                                           --> Horizontal Privesc --->

### Horizontal Privesc
- this is where you expand your reach over the compromised system by taking over a different user who is on the same privilege level as you. For instance a normal user hijacking another normal user. this allows one to inherit whatever files and access that specific user has. this for example, can be used to gain access to another normal privilege user that happens to have a SUID file attached to their home directory which can then be used to get super user access.

### Vertical Privsec
- this is with respect to gaining superuser or administrator privileges by hacking an admin account.

## References

- [checklists linux priv escalation](https://github.com/netbiosX/Checklists/blob/master/Linux-Privilege-Escalation.md)
- [payloads all things linux priv escalation](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md)
- [privilege escalation - oscp guide](https://sushant747.gitbooks.io/total-oscp-guide/privilege_escalation_-_linux.html)
- [linux priv escalation guide](https://payatu.com/guide-linux-privilege-escalation)

