# Traceroute

- traceroute is used to map the path your request takes to the destination computer.
- it allows you to see every intermediate step between your computer and the requested resource.
- windows traceroute utility is `tracert` and uses ICMP protocol (network - osi, internet - tcp/ip)
- unix traceroute equivalent uses udp protocol & can also use ICMP protocol (using -I, ICMP/echo) or TCP protocol (using -T, TCP/SYN).
- refer `man traceroute` for more information.
- syntax: `traceroute target`

## Example
traceroute tryhackme.com    (uses udp proto)
traceroute -I tryhackme.com (uses icmp proto - icmp/echo)
traceroute -T tryhackme.com (uses tcp proto - tcp syn)
