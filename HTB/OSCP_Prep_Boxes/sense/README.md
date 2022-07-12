# Sense
- nmap scan
- burp the login screen to find out how the login is being performed
- run a gobuster with extensions (.txt) as you may get banned, you will find two files which are critical to expose vulns on the box
- take a curl copy from burp & use `set paste` mode in vi editor to copy the text. (for bruteforcing)
- try to login because of poor password issues
- find out the version of the app, find out the vulns & exploit the vuls with burp
- get a root shell & capture the flag


## References
- [CVE Details](https://www.cvedetails.com/vulnerability-list/vendor_id-11749/product_id-21763/Pfsense-Pfsense.html)
- [pfsense 2.1.3 vulnerabilities](https://www.proteansec.com/linux/pfsense-vulnerabilities-part-2-command-injection/)  


