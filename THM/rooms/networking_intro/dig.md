# DIG

- The process of converting a name into an IP address is possible through DNS. 
- DNS is a TCP/IP Protocol. (transport - osi & tcp/ip models)
- This is the flow of finding the IP address for a given Domain Name.
  1. Local Cache
  2. Recursive DNS Server (known to the routers on the network - your ISP may maintain a recursive DNS server. The info about recursive DNS servers is stored on your routers. These recursive DNS servers often will have a cache of popular domain servers).
  3. rootname Server. (There are 13 rootname DNS servers in the world.)
  4. Toplevel Domain Server. (TLD)
  5. Authoritative name Server.
- DIG will allows us to query recursive DNS servers of our choice to retrieve info about domains.
- The Answer Section is important
- It contains essentially the IP address and the TTL values
- TTL will tell the time in seconds after which the info has to be queried again


## Example:-

dig tryhackme.com

```
...
;; ANSWER SECTION:
tryhackme.com.          300     IN      A       172.67.27.10
tryhackme.com.          300     IN      A       104.22.54.228
tryhackme.com.          300     IN      A       104.22.55.228
...
```
