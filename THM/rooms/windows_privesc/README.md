# Windows Privilege Escalation

## Windows Users

- Windows systems have different user privilege levels.
  - `Administrator (local)` -> this is the user with most privileges
  - `Standard (local)` -> these are the set of users who have access to computers but can only perform limited tasks. These users cannot make permanent changes on the system
  - `Guest` -> gives access to the system but it not defined as a user
  - Standard (domain)
  - Administrator (domain)
  - SYSTEM accounts usually deal with services
  - Service Accounts

## Different types of accounts

- *Administrators* - These users have the most privileges. They can change any system configuration parameter and access any file in the system.
- *Standard Users* - These users can access the computer but only perform limited tasks. Typically these users can not make permanent or essential changes to the system and are limited to their files.
- *SYSTEM/LocalSystem* - An account used by the operating system to perform internal tasks. It has full access to all files and resources available on the host with even higher privileges than administrators.
- *Local Service* - Default account used to run Windows services with "minimum" privileges. It will use anonymous connections over the network.
- *Network Service* - Default account used to run Windows services with "minimum" privileges. It will use Computer Credentials to authenticate through the network. 


- Typically, privilege escalation will require you to follow a methodology similar to the one given below: 
  1. Enumerate the current user's privileges and resources it can access.
  2. If the antivirus software allows it, run an automated enumeration script such as winPEAS or PowerUp.ps1
  3. If the initial enumeration and scripts do not uncover an obvious strategy, try a different approach (e.g. manually go over a checklist like the one provided [here](./enumeration/manual_enumeration.md))




## Enumeration 
- WinPeas & PowerUp (Automated)
- User Enumeration
- Group Enumeration
- systeminfo
- wmic
- Installed software, versions and exploits

## DLL Hijacking
- this is a technique that can allow you to inject code into your application.
- Some windows executables will use Dynamic Linking Libraries (DLLs) when running
- DLLs are executable files, but they cannot be run directly like an .exe file. The DLL's are launched by other apps.
- If we can switch a legimate DLL file with specially crafted DLL, our code will be run by the app. This is called DLL Hijacking
- DLL hijacking requires an application that has a missing DLL or the search order can be modified to insert the malicious DLL file.
- So, one needs to be aware of the search order when apps start running & start looking for these DLL files.

### Search Order

In summary, for standard desktop applications, Windows will follow one of the orders listed below depending on if the SafeDllSearchMode is enabled or not.

If SafeDllSearchMode is enabled, the search order is as follows:
- The directory from which the application loaded.
- The system directory. Use the GetSystemDirectory function to get the path of this directory.
- The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
- The Windows directory. Use the GetWindowsDirectory function to get the path of this directory.
- The current directory.

The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the App Paths registry key. The App Paths key is not used when computing the DLL search path.

If SafeDllSearchMode is disabled, the search order is as follows:

- The directory from which the application loaded.
- The current directory.
- The system directory. Use the GetSystemDirectory function to get the path of this directory.
- The 16-bit system directory. There is no function that obtains the path of this directory, but it is searched.
- The Windows directory. Use the GetWindowsDirectory function to get the path of this directory.
- The directories that are listed in the PATH environment variable. Note that this does not include the per-application path specified by the App Paths registry key. The App Paths key is not used when computing the DLL search path.

For example, if our application.exe requires the app.dll file to run, it will look for the app.dll file first in the directory from which it is launched. If this does not return any match for app.dll, the search will continue in the above-specified order. If the user privileges we have on the system allow us to write to any folder in the search order, we can have a possible DLL hijacking vulnerability. An important note is that the application should not be able to find the legitimate DLL before our modified DLL.

This is the final element needed for a successful DLL Hijacking attack. You can use `procmon` to identify if there are any NOT_FOUND messages for a particular app or process that can hint you for a DLL hijacking vul, but launching procmon requires you to have admin


malicious_dll.c
```
#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k whoami > C:\\Temp\\dll.txt");
        ExitProcess(0);
    }
    return TRUE;
}

```
install the mingw compiler
```
apt install gcc-mingw-w64-x86-64
x86_64-w64-mingw32-gcc malicious_dll.c -shared -o output.dll
```

- use the xfreerdp to connect & open a windows rdp session
- fire up a python web server or an smb server and try to get the msfvenom stageless (windows/x64/shell_reverse_tcp) onto the target machine & obtain a reverse windows shell on your attack box.

## Unattended Windows Installations
- When installing windows on a large number of hosts, administrators may use windows deployment services, which allows single operating system image to be deployed to several hosts through the network. Such installations require admin account to be setup. And these accounts might end up getting stored at the following places on those machines.
```
C:\Unattend.xml
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattend\Unattend.xml
C:\Windows\system32\sysprep.inf
C:\Windows\system32\sysprep\sysprep.xml
```
## Powershell History
- check this file and you may get lucky if the users have typed in passwords in the powershell command prompt
- `type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt`
- the above command works only in cmd.exe, if you have to execute in powershell prompt, use `$Env:userprofile` instead of `%userprofile%`

## Saved Credentials
- windows will allow you to use others credentials with cmdkey. `cmdkey /list`
- while you can't see the actual credentials you can use runas option. `runas /savecred /user:admin cmd.exe`

## IIS, Putty 
- Internet Information Services is a web server & in its web.config file there are credentials stored.
- Putty is a software that can help you with SSH connections, you can find clear text authentication credentials, you can use reg query to search for it.

## Service MisConfigurations
- Windows services are managed by ServiceControlManager (SCM). The SCM is a process in charge of managing the state of services as needed, checking the current status of any given service & generally provide a way to configure services
- Each service on windows will have an associated executable which will be run by SCM whenever a service is started. It is important to note that service executables implement special functions to be able to communicate with SCM.
- Services have `Discretionary Access Control lists (DACL)`, its the security around who can query,stop,start,pause services
- Service configuration is stored under `HKLM\SYSTEM\CurrentControlSet\Services\`


## Ways to privilege escalation on windows
- [ServiceExploits - Insecure service permissions](ServiceExploits_InsecurePermissions.md)


## Abusing dangerous privileges
- `whoami /priv` lets you know the privs of a user
- `SEBackup` & `SERestore` privs let you take backup (read/write) of any file on a windows computer without requiring any admin privs
- What we can do is copy the `SAM` & `SYSTEM` registry hives to extract the local administrator's password hash.
## SEBackup
- Dump the SAM/SYSTEM hashes and copy them to the attack box
- use impacket/psexec.py -hashes to use the hash (pass the hash attack) and obtain a foothold on the target

## SETakeOwnerShip
- SETakeOwnership allows us to take ownership of any object on the system including files and registry keys, opening up many possibilities for an attacker to elevate privileges.
- For example we could search for a service running as system user & take ownership of the service's executable.


## SEImpersonate/SEAssignPrimaryToken
- These privileges allow for a process to impersonate other users & act on their behalf. Impersonation usually consists of being able to spawn a process under the security context of another user. This is used by services that need to allow different users to access various resources, allowing the server to provide access restricted to a user's permission easily.
- As attackers you need to take control of a process with SEImpersonate and SEAssignPrimaryToken privileges, we can impersonate any user connecting and authenticating to that process
- In Windows systems, you will find that the LOCAL SERVICE and NETWORK SERVICE ACCOUNTS already have such privileges enabled. Since these accounts are used to spawn services using restricted accounts, it makes sense to allow them to impersonate connecting users if needed by the service. Internet Information Services (IIS) will also create a similar default account called "iis apppool\defaultapppool" for web applications.
- To elevate privileges using such accounts an attacker needs following:-
  - To be able to spawn a process so that a user can authenticate to it for impersonation to occur
  - Find a way to force privileged users to connect & authenticate to spawned malicious processes

## tools of trade
- There are tools to perform enumeration and help us find potential attack vectors.
- However do remember that automatic tools miss privelege escalation vectors
### WinPeas
- WinPEAS is a script developed to enumerate the target system to uncover privilege escalation paths. You can find more information about winPEAS and download either the precompiled executable or a .bat script. WinPEAS will run commands similar to the ones listed in the previous task and print their output. The output from winPEAS can be lengthy and sometimes difficult to read. This is why it would be good practice to always redirect the output to a file, as shown below: `winpeas.exe > output.txt`

### PrivescCheck
- PrivescCheck is a PowerShell script that searches common privilege escalation on the target system. It provides an alternative to WinPEAS without requiring the execution of a binary file.
```
Set-ExecutionPolicy Bypass -Scope process -Force
. .\PrivescCheck.ps1
Invoke-PrivescCheck
```
### WES-NG: Windows Exploit Suggester - Next Generation
- If you want to be stealthy go for WES-NG
- Some exploit suggesting scripts (e.g. winPEAS) will require you to upload them to the target system and run them there. This may cause antivirus software to detect and delete them. To avoid making unnecessary noise that can attract attention, you may prefer to use WES-NG, which will run on your attacking machine (e.g. Kali or TryHackMe AttackBox).
- Once installed before using it, type the `wes.py --update` command to update the database
. This script will refer to the database it checks for missing patches that can result in a vulnearbility you can use to elevate your privileges on the target system.
- To use the script you need to first run the following command:- `wes.py systeminfo.txt`

### Metasploit
- If you already have a meterpreter shell on the target system, you can use the following module to list vulnerabilities that may affect the target system & allow you to elevate privileges on the target system.
- `use multi/recon/local_exploit_suggester`



## References
- [Windows Exploit Suggester](https://github.com/bitsadmin/wesng)
- [PayloadsAllTheThings - Windows Privilege Escalation](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md)
- [Priv2Admin - Abusing Windows Privileges](https://github.com/gtworek/Priv2Admin)
- [RogueWinRM Exploit](https://github.com/antonioCoco/RogueWinRM)
- [Potatoes](https://jlajara.gitlab.io/others/2020/11/22/Potatoes_Windows_Privesc.html)
- [Decoder's Blog](https://decoder.cloud/)
- [Token Kidnapping](https://dl.packetstormsecurity.net/papers/presentations/TokenKidnapping.pdf)
- [Hacktricks - Windows Local Privilege Escalation](https://book.hacktricks.xyz/windows-hardening/windows-local-privilege-escalation)
