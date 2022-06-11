# Vulnerabilities

## Types
- Application Logic
- Weak or Default Credentials
- Human-factor
- Mis-Configuration
- Operating System

## Scoring Vulnerabilities (CVSS - Common Vulnerability Scoring System & VPR - Vulnerability Priority Rating)
- Vulnerability Management is the process of evaluating, categorising and ultimately remediating threats (vulns) faced by an organization
- As per stats, only 2% of Vulns will ever get exploited
- Therefore, it is all about addressing the most dangerous/critical vulns. This is where vuln scoring comes into play. Scoring will be based on the risk and impact it will have on a network or computer system.
- CVSS introduced in 2005. It asks three questions
  - How easy is it to exploit the vulnerability ?
  - Does exploit exists for this ?
  - How does the vulnerability interfere with CIA triad ?
### CVSS Scoring
|Rating|Score|
|-|-|
|None|0|
|Low|0.1-3.9|
|Medium|4.0-6.9|
|High|7.0-8.9|
|Critical|9.0-10.0|
### Pros/Cons of CVSS
- Pros:- Has been there for a long time & it is popular. It is free and is recommended by NIST
- Cons:- No prioritization of vuls is talked about. It relies heavily on exploit being available. the scoring always remain constat even after new developments take place
### VPR
- VPR was developed by Tenable. It is Modern.
- VPR heavily relies on the risk of the vuln to org.
- If the org is not using a piece of software, the vulns of the software are no meaning and the risk is very low.
- VPR uses similar scoring range like CVSS
### Pros/Cons of VPR
- Pros:- Modern framework; Takes into account about 150 factors when calculating risk;It is risk-driven,orgs can prioritize vulns;scorings are dynamic and they may change as the vuln ages.
- Cons:- VPR is not open-source.VPR can be adopted only on a commercial platform. VPR does not consider the CIA triad.

## Vuln Databases
- NVD (National Vulnerability Database)
- Exploit-Db
- NVD displays publically categorized vulns also known as CVE's (common vulnerabilities and exposures)
