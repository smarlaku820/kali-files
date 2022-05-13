# Use NMAP

For more info, visit [nmap room](./../nmap)

# GoBuster

- Using a fast directory discovery tool called `GoBuster`, you will locate a directory that you can use to upload a shell to.
- Lets first scan the website to find any hidden directories. To do this, we are going to use GoBuster.
- GoBuster is a tool used to brute-force URI's (directories & files), DNS sub-domains and virtual host names.
- use the following command.
- `gobuster dir -u http://10.10.131.12:3333 -w /usr/share/wordlists/dirb/common.txt`
```
-U - username  
-P - password
-c <http-cookies> - specify a cookie for simulating your auth
-p - proxy to use for requests
-e - print the full url's on the console

```
