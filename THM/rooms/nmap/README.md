# nmap

hacker -> knowledge -> enumeration of a target/network

## port-scan 
- which services are running on the target host (port scanning)
- with port scanning - a port can be discovered to be open/closed/filtered(firewall)
- 65535 available ports on a network-enabled computer
- 1024 are well-known ports
- nmap is versatile, powerful in its functionality. It can find vulns and also exploit the target successfully in many cases.

## nmap important switches
- -A (service detection, operating system detection, traceroute and common script scanning)
- -sS (SYN Scan)
- -sU (UDP Scan)
- -O (Operating system the target is running on)
- -sV (Version of services running on target)
- -v (Verbosity - Level 1)
- -vv (Verbosity - Level 2)
- -oA (nmap results in all three formats)
- -oG (nmap results in grepable format)
- -oX (namp results in xml format)
- -oN (nmap results in normal format)
- -T5 (nmap timing templates, speed of the scan)
- -p 500 (scan a specific port)
- -P 1000-1500 (scan a port range)
- -p- (scan all ports)
- -script (flag to activate nmap scripting library)
- -script=vuln (flag to activate/run all scripts in the vuln library)

## nmap Scan types - port scanning - more common
- -sU (UDP scan)
- -sT (TCP Connect scans)
- -sS ("Half Open" scan - TCP SYN)

## nmap Scan types - port scanning - less common
- -sF (TCP FIN scans)
- -sN (TCP Null scans)
- -sX (TCP XMAS scan)

## nmap network scanning - ping or icmp scans

## TCP Connect Scans (-sT)

TCP Full connect scans work by performing a 3-way handshake with each Target port.
NMAP tries to connect to each specified TCP port, and determines if the service is open by the response it receives.

If a TCP Port is open, the 3-way handshake is ought to be performed with
SYN/SYN-ACK/ACK packets.
With SYN & ACK packets originating from source (attack machine) & SYN-ACK originating from the target machine, in that order.

If a TCP Port is closed, the 3-way handshake is incomplete & the way to know about it is through SYN/RST packets.
In other words, the NMAP sends a TCP request with SYN flag set to the closed port, the target server will respond with the RST(reset) flag set.
By this response, NMAP can establish that the port is closed.

If however, the request is sent to an open port, the target server will respond with a TCP packet with SYN-ACK flag set.NMAP thus marks the port as open and thus setsthe TCP 3-way handshake complete.

What if the port is open and is behind a firewall.
In this scenario, nmap sends a TCP packet with SYN flag set & the firewall drops the packet. And therefore nmap doesn't get anything in response. therefore it marks the port as filtered.

That set, it is very easy for a firewall to send a TCP packet with RST (Reset) flag.This can make extremely difficult to get an accurate picture of the target.

A Linux IPtables command which firewalls dbport
### Example:-
```
iptables -I input -p tcp --dbport 3369 -j REJECT --reject-with tcp-reset
```

## TCP SYN Scans (-sS) 

These scans are referred to as "Half-Open" Scans or "Stealth" Scans.
This is how the communication will look like between the attacker machine and the target host/port.
SYN/SYN-ACK/RST

Advantages
- By pass the Older Intrusion Detection Systems (as they look out for 3-way handshakes). The modern IDS are smarter, they can detect a TCP SYN scan.
- Applications don't log these connections as the logging usually starts after a full handshake has been established.
- SYN scans are significantly faster.

Dis-advantages
- They require sudo permissions as SYN scans require the ability to create raw packets.(only root user has the privilege)
- unstable services are brought down by a SYN scan, this would be problematic if the client has provided a production system for penetration testing.

When it comes to tackling filtered ports.
TCP SYN/TCP RST(from target) - marks it as filtered.
When it comes to tackling closed ports.
TCP SYN/No response - marks it as closed.

SYN scans can be made to work by giving NMAP CAP_NET_RAW,CAP_NET_ADMIN,CAP_NET_BIND_SERVICE capabilities. However, this may not allow many of the NSE scripts to run properly. 

## UDP Scans (-sU)

- scans are stateless
- response is not expected, however nmap sends the UDP packet to the target port.
- if it gets a udp response, then it is marked as open.
- if it doesn't get a response, it is marked open/filtered & it moves on.
- when a packet is sent to a UDP closed port, the target should respond with an icmp ping containing a message that port is not reachable. then it marks it as closed.
- Due to difficulty in identifying if a port is open, udp scans are slower than various tcp scans.(takes about 20 mins to scan first 1000 ports with a good connection)
- it's a good practice therefore to run the udp scan against top 20 or n udp ports. the syntax goes like this `nmap -sU --top-ports 20 target`. This results in a more acceptable scan time.
- udp scans often have raw udp packets but it does send proto specific payload to ellicit an accurate response for accurate results.

## NULL,FIN and XMAS scans (-sN, -sF, -sX)
- stealthier than the previous scans
- NULL scan will have no TCP flags set, the target responds with a RST flag on a TCP packet if its a closed port.
- FIN scan will have just the FIN flag set and all the other flags unset. And if its a closed port, the target reponds with a TCP packet with RST flag set.
- XMAS scan will have a malformed TCP packet.(PSH,URG and FIN) flags are set. It looks like a blinking christmas tree when looked with wireshark, hence the name. The target is supposed to respond with RST flag if the port is closed.

when the ports are open, there is no expected response as the packets are malformedand it is just like UDP scans.
So, it can either be open/filtered when there is no reponse.

But it is definitely filtered if you get a ICMP ping response back stating the message to be node unreachable.

RFC793 mandatest that you should respond with a RST flag for malformed TCP packets and doesn't have to respond at all for open ports.
Its not true in some of the cases like MS windows and cisco's networking devices, they respond with a TCP RST flag when they a receive a malformed TCP packet on one of their open ports. So, this is understood by these scans (NULL/FIN/XMAS) as closedports.

The goal here is firewall evasion as most of the firewalls are configured to drop the TCP packets with SYN flag set (thus blocking neSo, it can either be open/filtered when there is no reponse.

But it is definitely filtered if you get a ICMP ping response back stating the message to be node unreachable.

RFC793 mandatest that you should respond with a RST flag for malformed TCP packets and doesn't have to respond at all for open ports.
Its not true in some of the cases like MS windows and cisco's networking devices, they respond with a TCP RST flag when they a receive a malformed TCP packet on one of their open ports. So, this is understood by these scans (NULL/FIN/XMAS) as closedports.

The goal here is **firewall evasion** as most of the firewalls are configured to drop the TCP packets with SYN flag set (thus blocking new connection initiation requests).
By sending requests that do not have SYN flag set, we bypass this firewall rules.Whilst this is good, modern IDS are aware of these scans.w connection initiation requests).
By sending requests that do not have SYN flag set, we bypass this firewall rules.Whilst this is good, modern IDS are aware of these scans.

- NULL/FIN/XMAS scans are generally used for firewall evasion.


|Scan type|        Open     |    Closed   | filtered   | open/filtered |
| - | - | - | - | - |
|Full| SYN/SYN-ACK/ACK | SYN/No Reponse | SYN/RST | SYN/RST or No reponse |
|SYN| SYN/SYN-ACK/RST | SYN/No Reponse | SYN/RST | SYN/RST or No response |
|UDP| UDP/No Response | UDP/ICMP unreachable | UDP/No response | UDP/No response|  
|NULL|  No response |  Malformed TCP with no flags set/RST | ICMP unreachable | No response |
|FIN|   No response |  Malformed TCP with FIN flag set/RST | ICMP unreachable | No response |

## ICMP Network scanning
- In a black box assignment, our first objective is to obtain a "map" of network structure or in other words we want to see which IP addressess contain active hosts.
- -sn is the flag
- -sn doesnt scan any ports
- it just sends ICMP echo packets to identify targets, hence it is called a "ping sweep".
- In addition to ICMP echo requests, -sn switch will cause nmap to send a TCP SYN packet to port 443 & TCP ACK(or TCP SYN packet if not run as root) packet to port 80.

## NSE (Nmap Scripting Engine)
- NSE scripts are written in `Lua` programming language.
- You can scan vuls,exploit them.
- The following categories are available.
  - safe - won't affect the target
  - intrusive - likely to affect the target
  - vuln - scan for vulnerabilities
  - exploit - attempt to exploit a vulnerability
  - auth - attempt to bypass authentication for running services.(i.e, Log in to FTP server anonymously)
  - brute - attempt to bruteforce credentials for running services.
  - discovery - attempt to query running services for further information about the network.(eg. query an SNMP server)
- multiple scripts can be run `--script=http-fileupload-exploiter` or `--script=smb-enum-users,smb-enum-shares`
- arguments can be specified with `--script-args`
- here is an example
```
nmap -p 80 --script http-put --script-args http-put.url='/dav/shell.php',http-put.file='./shell.php'
```

If scripts are missing, just do the following
```
Option 1:-
sudo apt update
sudo apt install nmap

Option 2:-

sudo wget -O /usr/share/nmap/scripts/<script_name>.nse https://svn.nmap.org/nmap/scripts/<script_name>.nse

sudo nmap --script-updatedb 
which updates the script.db file to contain the newly downloaded script
```
## Firewall Evasion
- we have already looked at FIN/NULL/XMAS scans and understood why these are firewallevasive.
- By default all windows hosts block ICMP pings. NMAP by default uses ICMP proto to ping and if it gets a response, it marks it for scanning. This will mark the entire host to be down.
- We have an option `-Pn` which tells nmap don't bother to ping, before it scans.
- This means that nmap will treat the target as a live host. this increases time as nmap needs to scan the entire port list even if its dead really.
- You can have NMAP also to rely on arp activity to detect hosts, if you are on a local network.

### Specific Switches for firewall evasion
- `-f` (fragment the packets, hoping that the firewall cannot detect it)
- or use a `--mtu number` to specify the packet size.
- `--scan-delay time_delay(ms)` delay between packets sent, for evading any time based firewall/IDS triggers.
- `--badsum` any real TCP/IP stack will drop this packet. However firewalls may potentially respond automatically without bothering to check the checksum of the packet.As such this switch can be used to check the presence of a firewall.

## References
[NMAP.org](https://nmap.org)
[NMAP option summary](https://nmap.org/book/man-briefoptions.html)
[nse usage](https://nmap.org/book/nse-usage.html)
[scripts](https://nmap.org/nsedoc/scripts/)
[scripts and arguments](https://nmap.org/nsedoc/)
[firewall evasion](https://nmap.org/book/man-bypass-firewalls-ids.html)
