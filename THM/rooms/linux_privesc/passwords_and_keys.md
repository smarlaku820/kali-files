# passwords and keys

## history files
- if the passwords are entered on the command prompt, it will be recorded in the `~\.*.history` files.
- do a `cat ~/.*history | less` and search for any passwords.
 
## config files
- config files will often contain passwords in plain text or other reversible formats.
- For example, take a look at the following openvpn file.
```

user@debian:~$ cat myvpn.ovpn 
client
dev tun
proto udp
remote 10.10.10.10 1194
resolv-retry infinite
nobind
persist-key
persist-tun
ca ca.crt
tls-client
remote-cert-tls server
auth-user-pass /etc/openvpn/auth.txt
comp-lzo
verb 1
reneg-sec 0

user@debian:~$ cat /etc/openvpn/auth.txt 
root
password123
user@debian:~$ 

```

## SSH keys

- look for hidden files & directories in system root.
- `ls -la /`
- also check for `ls -la /.ssh`
- check for sensitive files
