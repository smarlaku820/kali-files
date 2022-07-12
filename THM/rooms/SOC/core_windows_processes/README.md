# Core Windows Processes

## Task Manager
- Go to details tab -> this is where you will find core windows processes running
- right click on any one of the columns and choose "Image Path Name", observe this for any discrepancies.
- you must also look for parent processes and see if there are any outliers
- Task manager doesn't show that parent/child process relation. And therefore tools like ProcessHacker and ProcessExplorer come to our rescue.
- So, going forwards use ProcessHacker or ProcessExplorer to find information about core processes that are running inside of windows machines

## Verification of System Process
- System process always has the PID 4
- What is unusual behavior for this process?
 - A parent process (aside from System Idle Process (0))
 - Multiple instances of System. (Should only be 1 instance) 
 - A different PID. (Remember that the PID will always be PID 4)
 - Not running in Session 0

## SMSS.exe (session manager sub-system process)
- It is responsible for creating sessions. This is the first user-mode process started by the kernel.
- This process starts the user mode & kernel mode of the windows sub-system. This sub-system includes win32k.sys (kernel mode) and winsrv.dll (user mode) and csrss.exe (user mode).
- Smss.exe starts csrss.exe (Windows subsystem) and wininit.exe in Session 0,
- Smss.exe starts csrss.exe and winlogon.exe in Session 1
```
What is normal ?
Image Path:  %SystemRoot%\System32\smss.exe
Parent Process:  System
Number of Instances:  One master instance and child instance per session. The child instance exits after creating the session.
User Account:  Local System
Start Time:  Within seconds of boot time for the master instance

What is unusual?
A different parent process other than System(4)
Image path is different from C:\Windows\System32
More than 1 running process. (children self-terminate and exit after each new session)
User is not SYSTEM
Unexpected registry entries for Subsystem
```

## Last Words

- It is vital to understand how the Windows operating system functions as a defender. The Windows processes discussed in this room are core processes. Understanding how they operate normally can aid a defender to identify unusual activity on the endpoint. 

- With the introduction of Windows 10 additional processes have been added to the list of core processes to know and understand normal behavior.

- Earlier it was mentioned that if Credential Guard is enabled on the endpoint an additional process will be running, which will be a child process to wininit.exe, and that process is lsaiso.exe. This process works in conjunction with lsass.exe to enhance password protection on the endpoint. 

- Other processes with Windows 10 is RuntimeBroker.exe and taskhostw.exe (formerly taskhost.exe and taskhostex.exe). Please research these processes and any other processes you might be curious about to understand their purpose and their normal functionality. 

- The information for this room was derived from multiple sources.

### References
- https://www.threathunting.se/tag/windows-process/
- https://www.sans.org/security-resources/posters/hunt-evil/165/download
- https://docs.microsoft.com/en-us/sysinternals/resources/windows-internals

- Other links were provided throughout the room. It is encouraged to read them at your own leisure to further your foundation and understanding regarding the core Windows processes. 


