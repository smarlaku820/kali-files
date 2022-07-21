# Windows Event Logs
- Event logs record events taking place in the execution of a system to provide an audit trail that can be used to understand the activity of the system and to diagnose problems.
- Essential to understand the activities of complex systems, particulary in applications with little user interaction (such as server applications)
- As defenders (blue teamers) there is another use case for event logs. It can also be useful to combine log file entries from multiple sources. This approach, in combination with statistical analysis, may yield correlations between seemingly unrelated events on different servers.

## SIEM Main Features
- Threat Detection
- Investigation
- Time to respond

## SIEM Additional Features
- Basic Security Monitoring
- Advanced Threat Detection
- Forensics & Incident Response
- Log Collection
- Normalization
- Notification and alerts
- Security Incident Detection
- Threat Response Workflow

## Event Viewer
- The windows event logs are not text files that can be viewed using a notepad. However the raw data can be translated into XML using the windows API.
- They are stored in .evt or .evtx extensions. These files reside in `C:\Windows\System32\winevt\Logs`

## References
- [EVTX Attack Samples](https://github.com/sbousseaden/EVTX-ATTACK-SAMPLES)
- [PowerShell Blue Teaming](https://devblogs.microsoft.com/powershell/powershell-the-blue-team/)
- [Tampering with Windows Tracing](https://blog.palantir.com/tampering-with-windows-event-tracing-background-offense-and-defense-4be7ac62ac63)
- [Events to Monitor](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/appendix-l--events-to-monitor)
- [Security Monitoring and Auditing Reference](https://www.microsoft.com/en-us/download/confirmation.aspx?id=52630)
- [Greater Visibility through Powershell Logging](https://www.mandiant.com/resources/greater-visibilityt)
- [Powershell logging anamolies in UBA](https://docs.splunk.com/Documentation/UBA/5.0.4/GetDataIn/AddPowerShell)
