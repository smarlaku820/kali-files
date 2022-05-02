# ping - command line networking tools

- Often used to test connection to a remote computer.
- Ping uses ICMP protocol, slightly well-known TCP/IP protocols.
- ICMP works at network layer of the OSI Model thus at Internet Layer of the TCP/IP model.
- `ping target` is the command syntax
For more details, `man ping`

### Example
`ping -4 -v -i 5 -a muirlandoracle.co.uk` at an interval of 5 seconds for every ping request & use ipv4 only and print more verbose output with audible ping.
