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
