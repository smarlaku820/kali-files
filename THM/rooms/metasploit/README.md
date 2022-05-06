# Metasploit

## Introduction
- Most widely used exploitation framework. 
- Powerful tool that can support all phases of a pen testing engagement, from info gathering to post-exploitation.
- Metasploit has two versions
  - Metasploit Pro: Commercial version with Automation & mgmt of tasks. It also has GUI.
  - Metasploit Framework: Open-Source version that works from command line. 
- Metasploit Framework has a set of tools to allow information gathering, scanning, exploitation, exploit development, post-exploitation and more.
- It is mainly used for vulnerability reasearch and exploit development.

## Components of metasploit framework
- `msfconsole` - the main command line interface
- `Modules` - supporting modules such as exploits, scanners, payloads etc.
- `Tools` - Stand-alone tools that will help vuln reasearch, vuln assessment or pen testing. some of these tools are `mfsvenom`, `pattern_create` & `pattern_offset`. `pattern_*` tools are mainly useful in exploit development.

## Vulnerability, Exploit and Payload.
- **Exploit** - A piece of code that uses a vuln present on the target system.
- **Vulnerability** - A design, coding or logic flaw affecting the target system.
- **Payload** - An exploit will take advantage of a vuln. If we want the exploit to have the result we want (gaining access to the target system, read confidential information etc.,) we need to use payload. payloads are the code that will run on the target system.

There are various types of modules.
- auxiliary - supporting modules such as scanners, crawlers & fuzzers.
- encoders - that will allow you to encode the exploit & payload in the hope that a signature-based antivirus solun may miss them.
  signature-based antivirus and security solutions have a database of known threats. they detect threats by comparing suspicious files to this database and raise an alert if there is a match. Thus encoders can have a limited success rate as antivirus solutions can perform additional checks.
- evasion - mail intended to evade antivirus software.
- nops
- payloads - code that runs on the target system.
  - singles (generic/shell_reverse_tcp, windows/x64/pingback_reverse_tcp)
  - stages (windows/x64/shell/reverse_tcp)
  - stagers

When there is an `_` between shell and reverse it is called a signle payload. if there is a `/` its a staged payload.

## Summary
- Metasploit is a powerful tool that facilitates the exploitation process.
- Exploitation process has 3 main steps - finding the exploit, customizing the exploit and explotiing the vuln service
- Metasploit provides many modules that you can use for each step of the exploitation process.
