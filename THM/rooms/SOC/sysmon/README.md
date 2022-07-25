# Sysmon

- event id #1 - process creation
- event id #3 - network connections - metasploit remote connections - port 4444
- event id #7 - image loaded - dll injection or hijacking from C:\temp directory
- event id #8 - remote thread create -  The first method will look at the memory address for a specific ending condition which could be an indicator of a Cobalt Strike beacon. The second method will look for injected processes that do not have a parent process. This should be considered an anomaly and require further investigation. 
- event id #10 - process accessed
- event id #11 - file creation - This could be used to identify file names and signatures of files that are written to disk. Its a ransomware monitor.
- event id #12, #13, #14 - modifications to the registry, this could include persistence and credential abuse. C:\Windows\System\scripts common place to hide scripts by adversaries for persistence
- event id #15 - file create stream hash - files created in alternate streams
- event id #22 - dns anamolies

## References
- [Common Malware Connect Ports](https://docs.google.com/spreadsheets/d/17pSTDNpa0sf6pHeRhusvWG6rThciE8CsXTSlDUAZDyo/edit#gid=0)
- [Measure Object](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/measure-object?view=powershell-7.2)
