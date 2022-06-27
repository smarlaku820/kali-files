# WireShark
- It is a tool which captures packets and analyzes network traffic.

## Collection Methods
- Network Taps
- MAC Floods
- ARP Poisioning

## Basic Filtering
- ip.addr == <ip-address>
- ip.src == <src-ip-address> and ip.dst == <dst-ip-address>
- tcp.port == 80
- tcp.proto == TCP
- eth.addr == <mac-address>

## HTTP(s) traffic
- statistics/endpoints
- statistics/protocol hierarchy
- submitting the RSA keys for https packet decryption (edit->preferences->protocols->TLS->edit RSA Keys)
```
Host -> 127.0.0.1
Protocol -> http
Port -> start_tls
Key -> given the RSA key
```

## References
- [more captures](https://wiki.wireshark.org/SampleCaptures)
- [THM additional room](https://tryhackme.com/room/overpass2hacked)
- [DIFR madness](https://dfirmadness.com/case-001-pcap-analysis/)
