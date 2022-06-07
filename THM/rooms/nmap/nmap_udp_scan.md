```
└─$ sudo nmap -sV -sU -F -v 10.10.196.31
Starting Nmap 7.92 ( https://nmap.org ) at 2022-06-07 23:06 IST
NSE: Loaded 45 scripts for scanning.
Initiating Ping Scan at 23:06
Scanning 10.10.196.31 [4 ports]
Completed Ping Scan at 23:06, 0.21s elapsed (1 total hosts)
Initiating Parallel DNS resolution of 1 host. at 23:06
Completed Parallel DNS resolution of 1 host. at 23:06, 13.01s elapsed
Initiating UDP Scan at 23:06
Scanning 10.10.196.31 [100 ports]
Discovered open port 111/udp on 10.10.196.31
Discovered open port 53/udp on 10.10.196.31
Increasing send delay for 10.10.196.31 from 0 to 50 due to max_successful_tryno increase to 4
Increasing send delay for 10.10.196.31 from 50 to 100 due to max_successful_tryno increase to 5
Increasing send delay for 10.10.196.31 from 100 to 200 due to max_successful_tryno increase to 6
Increasing send delay for 10.10.196.31 from 200 to 400 due to 11 out of 12 dropped probes since last increase.
UDP Scan Timing: About 49.62% done; ETC: 23:07 (0:00:31 remaining)
Increasing send delay for 10.10.196.31 from 400 to 800 due to 11 out of 11 dropped probes since last increase.
Completed UDP Scan at 23:08, 101.37s elapsed (100 total ports)
Initiating Service scan at 23:08
Scanning 3 services on 10.10.196.31
Completed Service scan at 23:10, 97.66s elapsed (3 services on 1 host)
NSE: Script scanning 10.10.196.31.
Initiating NSE at 23:10
Completed NSE at 23:10, 0.20s elapsed
Initiating NSE at 23:10
Completed NSE at 23:10, 1.05s elapsed
Nmap scan report for 10.10.196.31
Host is up (0.17s latency).
Not shown: 97 closed udp ports (port-unreach)
PORT    STATE         SERVICE VERSION
53/udp  open          domain  ISC BIND 9.9.5 (Debian Linux 8.0 (Jessie))
68/udp  open|filtered dhcpc
111/udp open          rusersd 2-4 (RPC #100002)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 213.91 seconds
           Raw packets sent: 261 (15.749KB) | Rcvd: 108 (8.771KB)
```
