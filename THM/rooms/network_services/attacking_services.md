# Attacking Network Services
- Sniffing Attack
- Man in the Middle Attack
- Authentication Attack

## CIA Traid - DAD
- Confidentiality - Disclosure - Intelligence Agency 
- Integrity - Alteration - Banking Systems
- Availability - Destruction - Ad Servers

Different vulns can affect different aspects of CIA triad.
- DoS can affect Availability
- RCE can affect Integrity/Confidentiality and can cause severe damage.

Vuln by itself creates risk. we always must focus on how a protocol can be upgraded/updated or protected against disclosure and alteration i.e, protecting the confidentiality and integrity of transformed data.

## Sniffing Attack
- A network packet capture tool to attack to collect information about target.
- this attack can be carried out using Ethernet (802.3) network card.
- `tcpdump`, `wireshark` and `Tshark`
- Alternatively if we can access the traffic and modify it while the traffic is in transit then this refers to MIM attack.
- The only requirement for this attack to succeed is to have access to a system between two communicating systems. This attack requires attention. 

## TLS Protection
- Encryption layer is introduced via the Layer-6 (presentation layer)
- Netscape came up with SSL in 1994 and SSL 3.0 in 1996
- TLS was introduced in 1999 and is way more secure than SSL
- The mitigation lies in adding an encryption layer on top of any network protocol.For example, TLS has been added to HTTP,FTP,SMTP,POP3,IMAP & many others. Telnet has been replaced by SSH.
|Protocol|Default Ports|Secured Protocol|Default Port with TLS|
|-|-|-|
|HTTP|80|HTTPS|443|
|FTP|21|FTPS|990|
|SMTP|25|SMTPS|465|
|POP3|110|POP3S|995|
|IMAP|143|IMAPS|993|
|DNS|53|DoT (DNS over TLS)|853|
- To perform a SSL/TLS connection, the client needs to perform a proper handshake with the server. It will happen in the following order.
 - client - ClientHello message to the server to indicate its capabilities (such as supported algorithms)
 - server - ServerHello;Certificate;ServerKeyExchange;CertificateRequest;ServerHelloDone (the server reponds with serverhello, presents its cert (if there is auth required), it might also send additional info to generate master key, its in serverkeyexchange message)
 - client - Certificate;ClientKeyExchange;CertificateVerify;ChangeCipherSpec; (the client responds with a clientkeyexchange which contains additional info required to generate the master key. Furthermore, it switches to use encryption and informs the server using ChangeCipherSpec message)
 - server - ChangeCipherSpec;Finished (the server also responds with encryption and the SSL/TLS connection is established successfully)

## Man in the Middle Attack
- If the chosen protocol does not provide secure authentication or integrity checking then it makes them susceptiable to MITM attacks
- `Ettercap` and `Bettercap` are some of tools that can help with MITM attacks
- Mitigation against such attacks require one to use cryptography.with the help of PKI infrastructure(PKI) and trusted root certificates, Transport Layer Security (TLS) protects from MITM attacks.

## References
- [ettercap](https://www.ettercap-project.org/about.html)
- [bettercap](https://bettercap.org/usage)
