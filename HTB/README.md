# General Guidelines for Pentesting Engagements
- Beware of your pentest engagements
  - The box may BAN you ! 
  - You may crash the box
- Either scenario is not good.
- If the box bans you, there is an alternative if you don't want to revert the box. You can tunnel from a specific port on your host through an already compromised box. And below is the command.
  - `ssh -L 9000:localhost:80 user@<already-compromised-box>` or
  - `ssh -D1080 10.10.10.75` (Your localhost will listen on 1080 & all the connections will go to the target ssh box, essentially its a proxy through SSH connection)
  - Now utilize burpsuite, go to `user options` and `SOCKS proxy` (check use socks proxy) provide (`127.0.0.1` & `1080`) & verify that all connections are through via proxy
  - You can also do it from local host by modifying `/etc/proxychains.conf`  go to the `[ProxyList]` & add an entry `socks5 127.0.0.1 1080`. Finally run the command `proxychains curl <target-ip>` to verify that connection is going through socks5 proxy.
  - `socks4` is metasploit & `socks5` is ssh
  - Ensure the following lines are both uncommented.
```
Proxy DNS requests - no leak for DNS data
proxy_dns
```
- When running nmap scans, if there is a firewall use the flag `-sT` explicitly as nmap usually runs the stealth scan which is also invoked by invoking `-sS` which is the default.
- `nc -lnvp 9000 < commands.txt` commands.txt contains list of commands to be sent over when someone tries to netcat on the port 9000 on the attack box

## Boxed referred by ippsec for additional learning
- `October` for learning more about binary exploitation and/or buffer-overflow exploitation
- `CrimeStoppers` for learning more about php exfiltration
- `beep` for more LFI stuff

## References
- [Setting Up ProxyChains](https://medium.com/cyberxerx/how-to-setup-proxychains-in-kali-linux-by-terminal-618e2039b663)
