# GoBuster

## Modes

- dir mode to enumerate directories
- dns mode to enumerate domains & sub-domains
- flags

```
-c - cookies to use for requests
-x - file extensions to search for
-H - specify headers
-k - no-tls-validation
-n - don't print status codes
```

`dns` mode will allow gobuster to brute force sub-domains.Just because something is patched in the regular domain, does not mean that it is patched in the sub-domain. There may be a vulnerability for you to exploit in one of these sub-domains.

the above tells gobuster to do a sub-domain scan on the domain "mydomain.thm". If there are any sub-domains available, gobuster will find them & report them in your terminal.

```
-c - show CNAME records
-i - show ips
-r - use custom DNS server
```

`vhost` mode will allow gobuster to brute force virtual hosts. The following command will tell gobuster to do a virtual host scan on http://example.com usingthe selected wordlist.
after you find the sub-domains, try running gobuster again with the following command.

`gobuster dir -t 64 -u http://products.webenum.thm -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x.txt,.php`

## Important wordlistings
```
/usr/share/wordlists/dirbuster/directory-list-1.0.txt
/usr/share/wordlists/dirb/big.txt
/usr/share/wordlists/dirb/common.txt
/usr/share/wordlists/dirb/small.txt
/usr/share/wordlists/dirb/extensions_common.txt - Useful for when fuzzing for files!
```

## More Rooms
- [OWASP Top 10](https://tryhackme.com/room/owasptop10)
- [EasyPeasyCTF](https://tryhackme.com/room/easypeasyctf)

