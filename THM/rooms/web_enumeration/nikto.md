# nikto

- a powerful vulnerability scanner due to being both open-source and feature rich.
- nikto is capable of performing an assessment on all types of webservers & it isn't application specific such as `WPScan`
- nikto can be used to discover possible vulnerabilities using
```
Sensitive files
Outdated servers & programs
Common server and software misconfigurations (Directory indexing, cgi scripts, xss protections)
```
## Modes
### Basic Scanning
- The most basic scanning can be done by providing -h flag. `nikto -h <IP_ADDRESS:PORT> or dnsname`
- This scan will retrieve the headers advertised by the webserver or application & will look for any sensitive files or directories.
### Scanning multiple hosts & ports
- You can use nmap & nikto together
- `nmap -sT -p80 -oG 172.16.0.0/24 | nikto -h -`. You may try this when you have more than one host on the network to be scanned.
- You can also scan multiple ports. `nmap -h 10.10.0.0 -p80,8000,8080`
### Plugins
- to find the available list of plugins use - `nikto --list-plugins`
- Some of the interesting plugins are as follows:
  - apacheusers - attempt to enumerate Apache HTTP authentication users
  - cgi - Look for CGI scripts that we may be able to enumerate
  - robots - Analyse the robots.txt file which dictates what files/folders we are able to navigate to.
  - dir_traversal - Attempt to use a directory traversal attack, to look for system files such as /etc/passwd 
- `nikto -Plugin apacheuser -h 10.10.0.0:80`
### Other options
- `nikto -o report -f html`
- `nikto -o report.html`
- -Tuning option

|Category Name|Description |Tuning Option|
|-|-|-|
|File Upload|Search for anything on the webserver that may permit us to upload a file. This could be used to upload a reverse shell for an application to execute.|0|
|Misconfigurations/Default files|Search for common files that are sensitive & shouldn't be accessible such as config files on a web server|2|
|Information Disclosure|Gather information about the webserver or application (i.e., version numbers, HTTP headers or any information that may be useful to leverage in our attack later)|3|
|injection|search for possible locations where we can perform an injection like attack such as XSS or HTML|4|
|command injection|search for anything that permits us to execute OS commands|8|
|sql injection|look for applications that have URL parameters that are vulnerable to SQL injection|9|

## Sample scan
```
└─$ nikto -Display 2 -h 10.10.245.143:8080
- Nikto v2.1.6
---------------------------------------------------------------------------
+ Target IP:          10.10.245.143
+ Target Hostname:    10.10.245.143
+ Target Port:        8080
+ Start Time:         2022-05-29 06:03:13 (GMT5.5)
---------------------------------------------------------------------------
+ Server: Apache-Coyote/1.1
+ Retrieved x-powered-by header: Servlet/3.0; JBossAS-6
+ The anti-clickjacking X-Frame-Options header is not present.
+ The X-XSS-Protection header is not defined. This header can hint to the user agent to protect against some forms of XSS
+ The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OSVDB-39272: /favicon.ico file identifies this app/server as: JBoss Server
+ Allowed HTTP Methods: GET, HEAD, POST, PUT, DELETE, TRACE, OPTIONS 
+ OSVDB-397: HTTP method ('Allow' Header): 'PUT' method could allow clients to save files on the web server.
+ OSVDB-5646: HTTP method ('Allow' Header): 'DELETE' may allow clients to remove files on the web server.
+ /admin-console/config.php sent cookie: JSESSIONID=43A0E664E0E271B7423490D1C60CD216; Path=/admin-console
+ Cookie JSESSIONID created without the httponly flag```
```

## Rooms
- [RPWebScanning](https://tryhackme.com/room/rpwebscanning)
- [OWASP Top 10](https://tryhackme.com/room/owasptop10)
- [ToolsRUs](https://tryhackme.com/room/toolrus)
- [EasyCTF](https://tryhackme.com/room/easyctf)

