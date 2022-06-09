# FTP

- allow remote transfer of files over network
- uses client server model
- FTP operates in two channels
  - command or control channel
  - data channel
- command channel is for transmitting commands and replies to those commands
- data channel is for transmitting the data
- client initiates the connection and server validates credentials and open sessions
- while the session is open, the client may execute FTP commands on the server

## Active vs Passive
The FTP server may support active or passive connections or both.
In active FTP connection, the client opens a port & listens. the server is required to actively connect to it.
In passive FTP connection, the server opens a port & listens (passively) & the client connects to it.

The seperation of data & control channels doesn't block the commands to go through and reach server if there is a large file being transferred or in a slow internet connection.

## FTP server software
- vsftpd
- ProFTPD
- uFTP
FileZilla is an GUI based ftp client


References:-
[RFC 959](https://www.ietf.org/rfc/rfc959.txt)
[FTP Solaris Exploit](https://www.exploit-db.com/exploits/20745)
[ARP Poisioning with FTP](https://www.jscape.com/blog/bid/91906/Countering-Packet-Sniffers-Using-Encrypted-FTP)
