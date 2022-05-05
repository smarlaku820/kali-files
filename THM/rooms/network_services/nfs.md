# NFS

## understanding NFS
- Network file system
- Files/Folders are mounted by making RPC calls to an NFS Daemon.
- Implementation is guided by NFS Protocol.
- If a computer wants to access a file using NFS, an RPC call is placed to NFSD (the NFS daemon)
on the server. This call takes parameters such as:
  - the file handle
  - the name of the file to be accessed
  - the user's user ID
  - the user's group ID
- to represent files and directories on the server, NFS uses `file handle`
- NFS uses RPC protocols to communicate between client and server.
- user ID / group ID are key parameters the NFS uses to control the permissions/access to a given file.
- The command to mount an nfs share `sudo mount -t nfs IP:share /path/mount_dir -nolock`


## enumerating NFS
- In order to do a more advanced enumeration of NFS, you need to have a package called `nfs-common`
- `showmount` and `mount.nfs` are very critical to enumerate and these are tools as part of the `nfs-common` package.

## root squash
- By default on nfsshares root squashing is enabled.
- this prevents anyone connecting to the nfs share from having root access to the NFS volume.
- remote users are assigned a user `nfsnobody` when connected which has least local privileges.
- if this is turned off, it will allow one to create SUID bit files allowing remote root user access. 

## Resources
- [what is nfs file share](https://www.datto.com/library/what-is-nfs-file-share)
