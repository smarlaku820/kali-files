# SMTP

- SMTP is for handling of emails
- SMTP server has 3 main functions
  - verifies who is sending mails through the SMTP server
  - takes care of sending outgoing email 
  - outgoing mail can't be delivered it sends the message back to the sender

## Components in email delivery
- Mail User Agent (email client)
- Mail Submission Agent (MUA connects to MSA to send its message, MSA checks message for any errors before transferring it to MTA which is hosted on the same server) 
- Mail Transfer Agent (The MTA will send the message to MTA of the recipient, the MTA can also act as MSA)
- Mail Delivery Agent(A typical setup will have the MTA act as MDA)

## POP3/IMAP
- MUA downloads/reads email messages from MDA using POP3/IMAP protocols
- POP3 will usually download and delete messages & is not able to keep the messages (read/unread) syncrhonized if there are multiple email clients. Hence IMAP has come into picture.
- IMAP is more sophisticated than POP3. Every detail is synced with MDA


steps in smtp
1. mail agent connects to SMTP server of your domain. An SMTP handshake is initiated over SMTP port 25. Once the handshake has been   made, SMTP session starts.
2. the process of sending email (sender, recipients email address, body of the email with any attachments)
3. SMTP server checks domain name of the recipient & the sender is the same ?
4. SMTP server of the sender will make a connection to the recipients SMTP server before relaying the email. If recipient can't be reached it puts onto an SMTP queue.
5. Recipients email will verify the incoming email. Then the server will forward the email to the POP or IMAP server.
6. The email will show up in the recipients inbox.

## Enumerating SMTP servers
- We need to fingerprint the server to make our targeting as precise as possible. we are going to use the `smtp_version` module in 
MetaSpoilt to do this. As this name imples, it will scan a range of IP addresses and determine the version of any mail servers it encouters.

## Enumerating Users from SMTP
- The SMTP service has two internal commands that allow the enumeration of users `VRFY` and `EXPN`.
- `VRFY` confirms the names of the valid users
- `EXPN` reveals actual address of user's aliases and lists of e-mail (mailing lists). 
- We can do this over telnet, but there is a handy metasploit module called `smtp_enum`.

Note:-
There are other non-metasploit tools such as `smtp-user-enum` that work even better for enumerating OS-level user accounts on solaris via the SMTP service. It uses another command `RCPT TO` along with `VRFY` and `EXPN`.

This technique could be adapted in future to work against other vulnerable SMTP daemons.

