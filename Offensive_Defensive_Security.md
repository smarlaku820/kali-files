# Network Security (Offensive Security)

Network security is protecting the data and computers connected to a network. There is hardware & software based security.
Hardware security is often offered by appliances themselves like
- Virtual Private Appliance
- Intrusion Detection System
- Intrusion Prevention System
- Firewalls

Software security comes bundled up into the target machine
- Host based firewalls
- Anti-Virus Software

## Methodology
Breaking into a target network is a series of steps
- Recon -> attacker trying to know as much info as possible
- Weaponization -> preparing a malicious file with a malicious component. for example, to provide attacker with remote access
- Delivery -> delivering the weaponized "file" to target via any feasible method, such as email or USB flash memory
- Exploitation -> when the user opens the malicious file, the system executes the malicious component
- Installation -> the previous step should install the malware program
- Command & Control -> the successful installation provides attacker with command & control on the target system
- Action on Objectives -> after gaining the access on the target system, the attacker will start working on his objectives. For example:- Data exfiltration (stealing target's data)

# Digital Forensics (Defensive Security)
Digital Forensics is the application of computer science to investigate digital evidence for a legal purpose. It is used in two types of investigations

## Public-Sector Investigations
- usually carried out by government and law enforcement agencies. they would be part of civil and criminal investigation.
## Private-Sector Investigations 
- usually carried out by private investigators when there are policy violations in corporate policies. the private investigator can be in-house or outsourced.

Weather investigating a crime or corporate policy violation, part of the evidence is related to digital devices and digital media. This is where digital forensics come into play & tries to establish what happened. without trained digital forensic examiners, nothing can be established & won't be possible to process digital evidence properly.

As a digital forensics investigator, what do you do ?
- Acquire the evidence
- Establish a chain of custody - Fill out the related form ([Sample Form](https://www.nist.gov/document/sample-chain-custody-formdocx)). The purpose is to ensure that only authorized investigators have access to it & no one could have tampered with it.
- Place the evidence in a secure container - You want to ensure that the evidence does not get damaged. In the case of smart phones, you have to ensure that they cannot connect to the network, so they don't get wiped remotely.
- transport the evidence to digital forensics lab.

At the lab,
- Retrieve the digital evidence from the secure container
- create a forensic copy of the evidence
- return the digital evidence to the secure container
- start processing the copy of your forensic workstation
The steps have been detailed here. [Guide to computer forensics and investigations,6th Edition](https://www.cengage.uk/shop/isbn/9781337568944)

More generally digital forensics include
- proper search authority
- chain of custody
- validation with math
- use of validated tools
- repeatability
- reporting

# Security Operations Center

## Purpose
- Find vulns on the network
- Detect unauthorized activity
- Discover Policy Violations
- Detect Intrusions
- Support with Incident response


## Data Sources
- Server logs
- DNS logs
- DHCP logs
- Firewall logs
- SIEM (Security Information and Event Management) - aggregates data from various sources so that SOC can correlate event data with attacks
- database logs

## SOC services
- Monitor Security Posture
- Vuln Management
- Malware analysis
- Intrusion Detection
- Reporting

## SOC Proactive Services
- Network Security Monitoring(NSM) - monitor networks & detect any intrusions
- Threat Hunting - with *threat hunting* the SOC assumes that the an intrusion has already taken place & they begin the hunt to confirm their assumption
- Threat Intelligence - focuses on learning about potential adversaries & their tactics/techniques to improve companies defences. Its a **Threat-Informed Defence Model.**
- Security Awareness training - just raise the awareness of users

## Example Scenario

- One role in a SOC is the SOC analyst. A SOC analyst is responsible for network security monitoring and log management. Let’s consider the following scenario. While monitoring the network traffic, a SOC analyst notices a particular DNS query repeating every minute. This behaviour is not that of a user browsing the Internet, and every precisely one minute, they are making a new DNS query.

- The SOC analyst checks the source of the DNS query and identifies the cause as one laptop on the network. They isolate it and inspect it for signs of infection; they discover a process (program) using DNS to communicate with a malicious server. Soon, they find out that the computer was infected after visiting a malicious website by reviewing the computer logs. As a result, the laptop began communicating with a malicious server by hiding the messages in DNS queries. The laptop is cleaned, and threat hunting starts to ensure that no other computers are infected.
