```
cmnatic@thm-yara:~/suspicious-files/file1$ python ../../tools/Loki/loki.py -p .
                                                                               
      __   ____  __ ______                            
     / /  / __ \/ //_/  _/                            
    / /__/ /_/ / ,< _/ /                              
   /____/\____/_/|_/___/                              
      ________  _____  ____                           
     /  _/ __ \/ ___/ / __/______ ____  ___  ___ ____ 
    _/ // /_/ / /__  _\ \/ __/ _ `/ _ \/ _ \/ -_) __/ 
   /___/\____/\___/ /___/\__/\_,_/_//_/_//_/\__/_/    

   Copyright by Florian Roth, Released under the GNU General Public License
   Version 0.32.1
  
   DISCLAIMER - USE AT YOUR OWN RISK
   Please report false positives via https://github.com/Neo23x0/Loki/issues
  
                                                                               

[NOTICE] Starting Loki Scan VERSION: 0.32.1 SYSTEM: thm-yara TIME: 20220701T02:22:33Z PLATFORM:     PROC: x86_64 ARCH: 64bit 
[NOTICE] Registered plugin PluginWMI
[NOTICE] Loaded plugin /home/cmnatic/tools/Loki/plugins/loki-plugin-wmi.py
[NOTICE] PE-Sieve successfully initialized BINARY: /home/cmnatic/tools/Loki/tools/pe-sieve64.exe SOURCE: https://github.com/hasherezade/pe-sieve
[INFO] File Name Characteristics initialized with 2841 regex patterns
[INFO] C2 server indicators initialized with 1541 elements
[INFO] Malicious MD5 Hashes initialized with 19034 hashes
[INFO] Malicious SHA1 Hashes initialized with 7159 hashes
[INFO] Malicious SHA256 Hashes initialized with 22841 hashes
[INFO] False Positive Hashes initialized with 30 hashes
[INFO] Processing YARA rules folder /home/cmnatic/tools/Loki/signature-base/yara
[INFO] Initializing all YARA rules at once (composed string of all rule files)
[INFO] Initialized 653 Yara rules
[INFO] Reading private rules from binary ...
[NOTICE] Program should be run as 'root' to ensure all access rights to process memory and file objects.
[NOTICE] Running plugin PluginWMI
[NOTICE] Finished running plugin PluginWMI
[INFO] Scanning . ...  
[WARNING] 
FILE: ./ind3x.php SCORE: 70 TYPE: PHP SIZE: 80992 
FIRST_BYTES: 3c3f7068700a2f2a0a09623337346b20322e320a / <?php/*b374k 2.2 
MD5: 1606bdac2cb613bf0b8a22690364fbc5 
SHA1: 9383ed4ee7df17193f7a034c3190ecabc9000f9f 
SHA256: 5479f8cd1375364770df36e5a18262480a8f9d311e8eedb2c2390ecb233852ad CREATED: Mon Nov  9 15:15:32 2020 MODIFIED: Mon Nov  9 13:06:56 2020 ACCESSED: Fri Jul  1 02:22:38 2022 
REASON_1: Yara Rule MATCH: webshell_metaslsoft SUBSCORE: 70 
DESCRIPTION: Web Shell - file metaslsoft.php REF: - 
MATCHES: Str1: $buff .= "<tr><td><a href=\\"?d=".$pwd."\\">[ $folder ]</a></td><td>LINK</t
[NOTICE] Results: 0 alerts, 1 warnings, 7 notices
[RESULT] Suspicious objects detected!
[RESULT] Loki recommends a deeper analysis of the suspicious objects.
[INFO] Please report false positives via https://github.com/Neo23x0/signature-base
[NOTICE] Finished LOKI Scan SYSTEM: thm-yara TIME: 20220701T02:22:38Z
 
Press Enter to exit ...
cmnatic@thm-yara:~/suspicious-files/file1$ 
cmnatic@thm-yara:~/suspicious-files/file1$ cd ../..
cmnatic@thm-yara:~$ ls
go  suspicious-files  tools  yara-python
cmnatic@thm-yara:~$ cd suspicious-files/
cmnatic@thm-yara:~/suspicious-files$ cd file2
cmnatic@thm-yara:~/suspicious-files/file2$ python ../../tools/Loki/loki.py -p .
                                                                               
      __   ____  __ ______                            
     / /  / __ \/ //_/  _/                            
    / /__/ /_/ / ,< _/ /                              
   /____/\____/_/|_/___/                              
      ________  _____  ____                           
     /  _/ __ \/ ___/ / __/______ ____  ___  ___ ____ 
    _/ // /_/ / /__  _\ \/ __/ _ `/ _ \/ _ \/ -_) __/ 
   /___/\____/\___/ /___/\__/\_,_/_//_/_//_/\__/_/    

   Copyright by Florian Roth, Released under the GNU General Public License
   Version 0.32.1
  
   DISCLAIMER - USE AT YOUR OWN RISK
   Please report false positives via https://github.com/Neo23x0/Loki/issues
  
                                                                               

[NOTICE] Starting Loki Scan VERSION: 0.32.1 SYSTEM: thm-yara TIME: 20220701T02:29:12Z PLATFORM:     PROC: x86_64 ARCH: 64bit 
[NOTICE] Registered plugin PluginWMI
[NOTICE] Loaded plugin /home/cmnatic/tools/Loki/plugins/loki-plugin-wmi.py
[NOTICE] PE-Sieve successfully initialized BINARY: /home/cmnatic/tools/Loki/tools/pe-sieve64.exe SOURCE: https://github.com/hasherezade/pe-sieve
[INFO] File Name Characteristics initialized with 2841 regex patterns
[INFO] C2 server indicators initialized with 1541 elements
[INFO] Malicious MD5 Hashes initialized with 19034 hashes
[INFO] Malicious SHA1 Hashes initialized with 7159 hashes
[INFO] Malicious SHA256 Hashes initialized with 22841 hashes
[INFO] False Positive Hashes initialized with 30 hashes
[INFO] Processing YARA rules folder /home/cmnatic/tools/Loki/signature-base/yara
[INFO] Initializing all YARA rules at once (composed string of all rule files)
[INFO] Initialized 653 Yara rules
[INFO] Reading private rules from binary ...
[NOTICE] Program should be run as 'root' to ensure all access rights to process memory and file objects.
[NOTICE] Running plugin PluginWMI
[NOTICE] Finished running plugin PluginWMI
[INFO] Scanning . ...  
[NOTICE] Results: 0 alerts, 0 warnings, 7 notices
[RESULT] SYSTEM SEEMS TO BE CLEAN.
[INFO] Please report false positives via https://github.com/Neo23x0/signature-base
[NOTICE] Finished LOKI Scan SYSTEM: thm-yara TIME: 20220701T02:29:16Z
 
Press Enter to exit ...
cmnatic@thm-yara:~/suspicious-files/file2$ 

mnatic@thm-yara:~$ cd suspicious-files/file2
cmnatic@thm-yara:~/suspicious-files/file2$ python ../../tools/Loki/loki.py -p .
                                                                               
      __   ____  __ ______                            
     / /  / __ \/ //_/  _/                            
    / /__/ /_/ / ,< _/ /                              
   /____/\____/_/|_/___/                              
      ________  _____  ____                           
     /  _/ __ \/ ___/ / __/______ ____  ___  ___ ____ 
    _/ // /_/ / /__  _\ \/ __/ _ `/ _ \/ _ \/ -_) __/ 
   /___/\____/\___/ /___/\__/\_,_/_//_/_//_/\__/_/    

   Copyright by Florian Roth, Released under the GNU General Public License
   Version 0.32.1
  
   DISCLAIMER - USE AT YOUR OWN RISK
   Please report false positives via https://github.com/Neo23x0/Loki/issues
  
                                                                               

[NOTICE] Starting Loki Scan VERSION: 0.32.1 SYSTEM: thm-yara TIME: 20220701T02:43:51Z PLATFORM:     PROC: x86_64 ARCH: 64bit 
[NOTICE] Registered plugin PluginWMI
[NOTICE] Loaded plugin /home/cmnatic/tools/Loki/plugins/loki-plugin-wmi.py
[NOTICE] PE-Sieve successfully initialized BINARY: /home/cmnatic/tools/Loki/tools/pe-sieve64.exe SOURCE: https://github.com/hasherezade/pe-sieve
[INFO] File Name Characteristics initialized with 2841 regex patterns
[INFO] C2 server indicators initialized with 1541 elements
[INFO] Malicious MD5 Hashes initialized with 19034 hashes
[INFO] Malicious SHA1 Hashes initialized with 7159 hashes
[INFO] Malicious SHA256 Hashes initialized with 22841 hashes
[INFO] False Positive Hashes initialized with 30 hashes
[INFO] Processing YARA rules folder /home/cmnatic/tools/Loki/signature-base/yara
[INFO] Initializing all YARA rules at once (composed string of all rule files)
[INFO] Initialized 654 Yara rules
[INFO] Reading private rules from binary ...
[NOTICE] Program should be run as 'root' to ensure all access rights to process memory and file objects.
[NOTICE] Running plugin PluginWMI
[NOTICE] Finished running plugin PluginWMI
[INFO] Scanning . ...  
[WARNING] 
FILE: ./1ndex.php SCORE: 70 TYPE: PHP SIZE: 223978 
FIRST_BYTES: 3c3f7068700a2f2a0a09623337346b207368656c / <?php/*b374k shel 
MD5: c6a7ebafdbe239d65248e2b69b670157 
SHA1: 3926ab64dcf04e87024011cf39902beac32711da 
SHA256: 53fe44b4753874f079a936325d1fdc9b1691956a29c3aaf8643cdbd49f5984bf CREATED: Mon Nov  9 15:16:03 2020 MODIFIED: Mon Nov  9 13:09:18 2020 ACCESSED: Fri Jul  1 02:29:16 2022 
REASON_1: Yara Rule MATCH: _home_cmnatic_suspicious_files_file2_1ndex SUBSCORE: 70 
DESCRIPTION: file2 - file 1ndex.php REF: https://github.com/Neo23x0/yarGen 
MATCHES: Str1: var Zepto=function(){function G(a){return a==null?String(a):z[A.call(a)]||"object"}function H(a){return G(a)=="function"}fun Str2: $c ... (truncated)
[WARNING] 
FILE: ./loki_thm-yara_2022-07-01_02-29-12.log SCORE: 70 TYPE: UNKNOWN SIZE: 2657 
FIRST_BYTES: 32303232303730315430323a32393a31325a2074 / 20220701T02:29:12Z t 
MD5: 560d188f22bf31b631f79e870b712176 
SHA1: 7e2122aedfeb6fd68fe76ebef0a39f66a3179b86 
SHA256: a5d3f598ad7844d5b82c5aee7678bb8a49f3fc82be2c5bc6f3a919b92f04e6f1 CREATED: Fri Jul  1 02:29:16 2022 MODIFIED: Fri Jul  1 02:29:16 2022 ACCESSED: Fri Jul  1 02:37:38 2022 
REASON_1: Yara Rule MATCH: loki_thm_yara_2022_07_01_02_29_12 SUBSCORE: 70 
DESCRIPTION: file2 - file loki_thm-yara_2022-07-01_02-29-12.log REF: https://github.com/Neo23x0/yarGen 
MATCHES: Str1: 20220701T02:29:12Z thm-yara LOKI: Notice: MODULE: PESieve MESSAGE: PE-Sieve successfully initialized BINARY: /home/cmnatic/tools Str2 ... (truncated)
[NOTICE] Results: 0 alerts, 2 warnings, 7 notices
[RESULT] Suspicious objects detected!
[RESULT] Loki recommends a deeper analysis of the suspicious objects.
[INFO] Please report false positives via https://github.com/Neo23x0/signature-base
[NOTICE] Finished LOKI Scan SYSTEM: thm-yara TIME: 20220701T02:43:55Z
 
Press Enter to exit ...
cmnatic@thm-yara:~/suspicious-files/file2$ cd ..
cmnatic@thm-yara:~/suspicious-files$ ls
file1  file2  file2.yar
cmnatic@thm-yara:~/suspicious-files$ vi file2.yar 
cmnatic@thm-yara:~/suspicious-files$ vi file2.yar 
cmnatic@thm-yara:~/suspicious-files$ cat file2.yar | grep Zepto
      $x1 = "var Zepto=function(){function G(a){return a==null?String(a):z[A.call(a)]||\"object\"}function H(a){return G(a)==\"function\"}fun" ascii
cmnatic@thm-yara:~/suspicious-files$ cat file2.yar | grep size
      uint16(0) == 0x3f3c and filesize < 700KB and
      uint16(0) == 0x3032 and filesize < 7KB and
cmnatic@thm-yara:~/suspicious-files$ 



```
