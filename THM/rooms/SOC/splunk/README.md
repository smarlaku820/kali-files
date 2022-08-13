# Splunk

## SIGMAC

Florian Roth created Sigma. 

### What is Sigma?

- As per the GitHub repo, "Sigma is a generic and open signature format that allows you to describe relevant log events in a straightforward manner. The rule format is very flexible, easy to write and applicable to any type of log file. The main purpose of this project is to provide a structured form in which researchers or analysts can describe their once developed detection methods and make them shareable with others."

- Each SIEM has its own structure/format for creating queries. It isn't easy to share SIEM queries with other Security Teams if they don't use your exact SIEM product. For example, you can have a repo of Splunk queries that your team utilizes for threat exposure checks or threat hunting. These queries (or rules) can be created in the Sigma format and shared with teams that don't use Splunk. Sigma rules can be shared along with IOCs and YARA rules as Threat Intelligence. 

### Some supported target SIEMs:

- Splunk
- Microsoft Defender Advanced Threat Protection
- Azure Sentinel
- ArcSight
- QRadar

### Some projects/products that use Sigma:

- MISP
- THOR
- Joe Sandbox

There also is a Splunk app titled `TA-Sigma-Searches`.(https://github.com/dstaulcu/TA-Sigma-Searches) 

Sigma rules are written in YAML (YAML Ain't Markup Language).
As per the website, "YAML is a human friendly data serialization standard for all programming languages."  
The Sigma repo has signatures in the rules folder. Sigmac, the Sigma Converter, located in the tools folder, can generate a specific SIEM rule. 

Example:-
`./sigmac -t splunk -c tools/config/generic/sysmon.yml ./rules/windows/process_creation/win_susp_whoami.yml`

An online version of this tool created by SOC PRIME (Florian Roth) does the conversion work for you. The tool is Uncoder.io. 



## References
- https://github.com/SigmaHQ/sigma
- https://uncoder.io/
- https://ivanitlearning.wordpress.com/2020/06/23/hunting-with-splunk-botsv2-qns-4xx/#:~:text=405%20%E2%80%93%20What%20is%20the%20first,answer%20above%20from%20qn%20401.
