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





## Ways to privilege escalation on windows
- [ServiceExploits - Insecure service permissions](ServiceExploits_InsecurePermissions.md)
