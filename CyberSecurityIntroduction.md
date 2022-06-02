# Introduction to CyberSecurity

## Offensive Security
- It is the process of breaking into computer systems, exploiting software bugs, finding loopholes in the application to gain unauthorized access to them.
- To beat the hacker, you have to be like a hacker. Always trying to find vulnerabilities in the application & recommending the patches before the cybercriminal does.

## Defensive Security
- It the job of protecting org's network & computer systems by analyzing & securing any potential digital threats. You will learn more about this in Digital Forensics Room.
- In this kind of role, you will often be tasked to investigate infected computers or devices to understand how it was hacked, trackingdown cyber criminals, or monitoring infrastructure for malicious activity.
- Defensive security is concerned with two main tasks
  - Preventing intrusions from occuring
  - Detecting intrusions when they occur and respond properly
- Blue teams are part of defensive security landscape.
- tasks related to defensive security
  - User cyber security awareness
  - Documenting and managing assets
  - Updating and patching systems
  - Setting up preventative security devices -> firewalls & intrusion prevention systems (IPS) are critical components of preventative security.
  - Setting up logging and monitoring devices
- Some of the other crucial areas in relation to Defensive Security are 
  - Security Operations Center (SOC)
  - Threat Intelligence
  - Digital Forensics and Incident Response (DFIR)
  - Malware Analysis

### SOC
- Responsible for monitoring network & its systems to detect malicious cyber security events. 
- Some of the main areas of SOC are
  - Vulnerabilities -> detecting a vulnerable system
  - Policy Voilations -> security policy is a set of rules required for the protection of network and systems.
  - Unauthorized Activity
  - Network Intrusions

### Threat Intelligence
- To ensure protection, SOC does various tasks. One of the important among them is Threat Intelligence.
- *Threat Intelligence* is the information you gather about actual & potential enemies. A threat is any action that can disrupt or adversely affect a system.
  - Some adversaries are interested to steal customer data
  - Some may be interested to stop production services running
  - Some ransomware group may be looking for financial reasons
  - Some nation-state cyber army may be working for political reasons.
- Intelligence needs data. Data is Collected -> Processed -> Analyzed
- From analysis you will find more information about attackers and their motives. This can help create a list of recommendations and actionable steps. (*Response Strategy*)

### Digital Forensics and Incident Response
- Forensics is the application of science to investigate crimes and establish facts.
- The focus of digital forensics shifts to analyzing evidence of an attack & its perpetrators. It is also concerned with areas such as Intellectual property, theft, cyber espionage & possession of unathorized content.
- Digital Forensic areas
  - File System - looking for installed programs, created files, partially over-written files and deleted files
  - System Memory - If the attacker is running a malicious program in the memory without saving it to disk, taking a forensic (low-level) image of the system memory is the best way to analyze the contents & learn about the attack.
  - System Logs
  - Network Logs

### Incident Response
- How would you respond to a cyber attack ?
- Incident response specifies the methodology that should be followed to handle such a case.
- The aim is to reduce damage and recover in shortest time possible.
- Ideally one needs to develop a plan for Incident response.
- 4 Major phases in Incident response
  - Preparation - A team for handling incidents & some measures required to prevent incidents from happening in the first place.
  - Detection and Analysis - The team has all resources to detect any incident. It is essential to further analyze the severity of the occured incident.
  - Containment, Eradication and Recovery - Once an incident is detected it is crucial to stop it affecting other systems, eliminate it & recover the affected systems.
  - Post-Incident Activity - After the recovery, a report is produced & the lesson learned is shared to prevent similar future incidents.

### Malware Analysis
- Malware is software
- Virus -> A piece of code that attaches to a program. Designed to spread from one computer to another. It works by altering, overwriting & deleting files once it infects the computer. The result ranges from computer being slow to unusable.
- Trojan Horse -> its a program that shows one desirable function but hides the malicious function underneath. Ex:- a video palyer from a shady website that gives the attacker complete control of the victims system
- Ransomware -> A malicious program that encrypts user files. Encryption makes the files unreadable. The attacker is willing to offer the encrypted password if the user is willing to pay ransome.
- Static Analysis & Dynamic Analysis - Studying malware at rest & in a controlled environment.


## Carrers in Offensive Security
- Hackers are often called Security Consultants
- Defenders are often called Security Analysts
- Offensive Security Roles
  - *Penetration Tester* -> Responsible for testing technology products for finding exploitable vulnerabilities or security loopholes. Learning Paths:- `Jr.Penetration Tester` & `Offensive Pentesting`
  - *Red Teamer* -> Plays the role of an adversary, attacking an organization & providing feedback from enemy's prespective. Done by a team external to the company. Learning Paths:- `Jr.Penetration Tester`, `Offensive Pentesting` & `Red Team Learning Path`
  - *Security Engineer* -> Design, maintain, monitor security controls, networks & systems to prevent cyberattacks. they develop and implement security solutions using threats and vuln data. The ultimate goal is to retain and adopt security measures to mitigate the risk of attack and data loss. Security engineer has the following responsibilities -> 1. Testing and screening security measures across software. 2. Monitor networks and reports to update systems & mitigate vulns. 3. Identify and implement systems needed for optimal security. Learning Paths:- `Cyber Defense`, `Jr.Penetration Tester` & `Offensive Pentesting`
- Defensive Security Roles
  - *Security Analyst* -> Explore and Evaluate company network. Work with various stakeholders to analyse the cybersecurity in the company. Compile ongoing reports about safety of networks, documenting security issues & measures taken in response. Develop security plans, incorporating research on new attack tools & trends, and measures needed across teams to maintain data integrity. Learning Paths:- `Cyber Defense` & `Pre-Security`.
  - *Incident Responder* -> Identifies and mitigates attacks whilst the attack is still unfolding. Highly pressurized position with assessments and response required in real-time. Incident response metrics include **MTTD, MTTA, MTTR** - Mean time to detect, acknowledge and recover. The aim is to achieve a swift response. Incident responder's protect companies data, reputation and financial standing from cyber attacks. Learning Paths:- `Cyber Defense`
  - *Digital Forensics Examiner* - Investigate incident and crime. Collect & analyse evidence to solve crime. Charging the guity and exonerating the innocent. Main responsibilities include 1.Collecting evidence while observing legal procedures. 2.Analyse evidence 3. Document findings and report a case.
  - *Malware Analyst*  - Static Analysis (Reverse Engineering). They are responsible for convering compiled programs from machine language to readable code, usually in a low-level language. Strong background in C & Low-level languages.

## References
- [AbuseIPDB](https://www.abuseipdb.com/)
