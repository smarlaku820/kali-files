# WPScan

- Released in 2011, important tool in a pentester's toolkit
- WPScan is capable of enumerating & researching a few security vulnerability categories present in wordpress sites.
- the following are the areas of overlap
```

Sensitive information disclosure
Path Discovery
Weak Password Policies
Presence of Default Installation
Testing Web Application Firewalls (WAF Plugins)
``` 
- WPScan uses information present in the database when enumerating themes & plugins
- Make it a point to update the database frequently. `wpscan --update`


## Enumerating for Installed themes
- You can identify the theme with `-enumerate` flag. The command is as follows: `wpscan --url http://cmnatics.playground/ --enumerate t`
- The great thing about WPScan is that the tool lets you know how it determined the results it has got.

## Enumerating for Installed Plugins
- A very common feature of webservers is "Directory Listing" & is often enabled by default.
- `wpscan --url http://cmnatics.playground/ --enumerate p`
- To find vulnerable plugins - `wpscan --url http://cmnatics.playground --enumerate vp`

## Enumerating for users
- `wpscan --url http://cmnatics.playground/ --enumerate u`
- `wpscan --url http://cmnatics.playground/ --passwords rockyou.txt --usernames cmnatic`

## Adjusting WPScan Agressiveness
- To be noisy/less noisy. 
- Lot of requests to a web server can be noisy & you may get blocked at the firewall. If you want to be less noisy, some plugins & themes may be missed by your scan.
- `--plugins-detection aggressive`
- `--plugins-detection passive`

## Rooms
- [RPWebScanning](https://tryhackme.com/room/rpwebscanning)
- [Blog](https://tryhackme.com/room/blog)
