# Windows Privilege Escalation

- Windows systems have different user privilege levels.
  - `Administrator (local)` -> this is the user with most privileges
  - `Standard (local)` -> these are the set of users who have access to computers but can only perform limited tasks. These users cannot make permanent changes on the system
  - `Guest` -> gives access to the system but it not defined as a user
  - Standard (domain)
  - Administrator (domain)
  - SYSTEM accounts usually deal with services
  - Service Accounts
- Typically, privilege escalation will require you to follow a methodology similar to the one given below: 
  1. Enumerate the current user's privileges and resources it can access.
  2. If the antivirus software allows it, run an automated enumeration script such as winPEAS or PowerUp.ps1
  3. If the initial enumeration and scripts do not uncover an obvious strategy, try a different approach (e.g. manually go over a checklist like the one provided [here](./enumeration/manual_enumeration.md))




- use the xfreerdp to connect & open a windows rdp session
- fire up a python web server or an smb server and try to get the msfvenom stageless (windows/x64/shell_reverse_tcp) onto the target machine & obtain a reverse windows shell on your attack box.

## Ways to privilege escalation on windows
- [ServiceExploits - Insecure service permissions](ServiceExploits_InsecurePermissions.md)
