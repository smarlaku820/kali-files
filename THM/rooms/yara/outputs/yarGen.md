```
cmnatic@thm-yara:~/tools/yarGen$ python3 yarGen.py -m ~/suspicious-files/file2 --excludegood -o ~/suspicious-files/file2.yar
------------------------------------------------------------------------
                   _____            
    __ _____ _____/ ___/__ ___      
   / // / _ `/ __/ (_ / -_) _ \     
   \_, /\_,_/_/  \___/\__/_//_/     
  /___/  Yara Rule Generator        
         Florian Roth, July 2020, Version 0.23.3
   
  Note: Rules have to be post-processed
  See this post for details: https://medium.com/@cyb3rops/121d29322282
------------------------------------------------------------------------
[+] Using identifier 'file2'
[+] Using reference 'https://github.com/Neo23x0/yarGen'
[+] Using prefix 'file2'
[+] Processing PEStudio strings ...
[+] Reading goodware strings from database 'good-strings.db' ...
    (This could take some time and uses several Gigabytes of RAM depending on your db size)
[+] Loading ./dbs/good-imphashes-part9.db ...
[+] Total: 1 / Added 1 entries
[+] Loading ./dbs/good-exports-part6.db ...
[+] Total: 8065 / Added 8065 entries
[+] Loading ./dbs/good-imphashes-part2.db ...
[+] Total: 1056 / Added 1055 entries
[+] Loading ./dbs/good-imphashes-part7.db ...
[+] Total: 4648 / Added 3592 entries
[+] Loading ./dbs/good-imphashes-part1.db ...
[+] Total: 6227 / Added 1579 entries
[+] Loading ./dbs/good-imphashes-part6.db ...
[+] Total: 6256 / Added 29 entries
[+] Loading ./dbs/good-exports-part8.db ...
[+] Total: 22192 / Added 14127 entries
[+] Loading ./dbs/good-strings-part1.db ...
[+] Total: 1416757 / Added 1416757 entries
[+] Loading ./dbs/good-imphashes-part3.db ...
[+] Total: 10035 / Added 3779 entries
[+] Loading ./dbs/good-strings-part9.db ...
[+] Total: 1417513 / Added 756 entries
[+] Loading ./dbs/good-strings-part8.db ...
[+] Total: 1699743 / Added 282230 entries
[+] Loading ./dbs/good-strings-part5.db ...
[+] Total: 5764251 / Added 4064508 entries
[+] Loading ./dbs/good-strings-part6.db ...
[+] Total: 6382068 / Added 617817 entries
[+] Loading ./dbs/good-strings-part3.db ...
[+] Total: 9110194 / Added 2728126 entries
[+] Loading ./dbs/good-exports-part4.db ...
[+] Total: 110911 / Added 88719 entries
[+] Loading ./dbs/good-exports-part5.db ...
[+] Total: 236241 / Added 125330 entries
[+] Loading ./dbs/good-imphashes-part5.db ...
[+] Total: 17205 / Added 7170 entries
[+] Loading ./dbs/good-exports-part3.db ...
[+] Total: 279926 / Added 43685 entries
[+] Loading ./dbs/good-strings-part4.db ...
[+] Total: 10459690 / Added 1349496 entries
[+] Loading ./dbs/good-exports-part9.db ...
[+] Total: 279926 / Added 0 entries
[+] Loading ./dbs/good-exports-part2.db ...
[+] Total: 322362 / Added 42436 entries
[+] Loading ./dbs/good-strings-part2.db ...
[+] Total: 11433382 / Added 973692 entries
[+] Loading ./dbs/good-exports-part1.db ...
[+] Total: 381481 / Added 59119 entries
[+] Loading ./dbs/good-exports-part7.db ...
[+] Total: 404321 / Added 22840 entries
[+] Loading ./dbs/good-imphashes-part8.db ...
[+] Total: 17388 / Added 183 entries
[+] Loading ./dbs/good-imphashes-part4.db ...
[+] Total: 19764 / Added 2376 entries
[+] Loading ./dbs/good-strings-part7.db ...
[+] Total: 12284943 / Added 851561 entries
[+] Processing malware files ...
[+] Processing /home/cmnatic/suspicious-files/file2/1ndex.php ...
[+] Processing /home/cmnatic/suspicious-files/file2/loki_thm-yara_2022-07-01_02-29-12.log ...
[+] Generating statistical data ...
[+] Generating Super Rules ... (a lot of foo magic)
[+] Generating Simple Rules ...
[-] Applying intelligent filters to string findings ...
[-] Filtering string set for /home/cmnatic/suspicious-files/file2/1ndex.php ...
[-] Filtering string set for /home/cmnatic/suspicious-files/file2/loki_thm-yara_2022-07-01_02-29-12.log ...
[+] Generating Super Rules ...
[=] Generated 2 SIMPLE rules.
[=] Generated 0 SUPER rules.
[=] All rules written to /home/cmnatic/suspicious-files/file2.yar
[+] yarGen run finished
cmnatic@thm-yara:~/tools/yarGen$ cat ~/suspicious-files/file
cat: /home/cmnatic/suspicious-files/file: No such file or directory
cmnatic@thm-yara:~/tools/yarGen$ cat ~/suspicious-files/file2.yar 
/*
   YARA Rule Set
   Author: yarGen Rule Generator
   Date: 2022-07-01
   Identifier: file2
   Reference: https://github.com/Neo23x0/yarGen
*/

/* Rule Set ----------------------------------------------------------------- */

rule _home_cmnatic_suspicious_files_file2_1ndex {
   meta:
      description = "file2 - file 1ndex.php"
      author = "yarGen Rule Generator"
      reference = "https://github.com/Neo23x0/yarGen"
      date = "2022-07-01"
      hash1 = "53fe44b4753874f079a936325d1fdc9b1691956a29c3aaf8643cdbd49f5984bf"
   strings:
      $x1 = "var Zepto=function(){function G(a){return a==null?String(a):z[A.call(a)]||\"object\"}function H(a){return G(a)==\"function\"}fun" ascii
      $s2 = "$cmd = execute(\"taskkill /F /PID \".$pid);" fullword ascii
      $s3 = "return (res = new RegExp('(?:^|; )' + encodeURIComponent(key) + '=([^;]*)').exec(document.cookie)) ? (res[1]) : null;" fullword ascii
      $s4 = "$cmd = trim(execute(\"ps -p \".$pid));" fullword ascii
      $s5 = "$buff = execute(\"wget \".$url.\" -O \".$saveas);" fullword ascii
      $s6 = "$buff = execute(\"curl \".$url.\" -o \".$saveas);" fullword ascii
      $s7 = "(d=\"0\"+d);dt2=y+m+d;return dt1==dt2?0:dt1<dt2?-1:1},r:function(a,b){for(var c=0,e=a.length-1,g=h;g;){for(var g=j,f=c;f<e;++f)0" ascii
      $s8 = "$cmd = execute(\"kill -9 \".$pid);" fullword ascii
      $s9 = "$cmd = execute(\"tasklist /FI \\\"PID eq \".$pid.\"\\\"\");" fullword ascii
      $s10 = "ngs.mimeType||xhr.getResponseHeader(\"content-type\")),result=xhr.responseText;try{dataType==\"script\"?(1,eval)(result):dataTyp" ascii
      $s11 = "execute(\"tar xzf \\\"\".basename($archive).\"\\\" -C \\\"\".$target.\"\\\"\");" fullword ascii
      $s12 = "execute(\"tar xf \\\"\".basename($archive).\"\\\" -C \\\"\".$target.\"\\\"\");" fullword ascii
      $s13 = "$body = preg_replace(\"/<a href=\\\"http:\\/\\/www.zend.com\\/(.*?)<\\/a>/\", \"\", $body);" fullword ascii
      $s14 = "$check = strtolower(execute(\"node -h\"));" fullword ascii
      $s15 = "$buff = execute(\"lwp-download \".$url.\" \".$saveas);" fullword ascii
      $s16 = "$check = strtolower(execute(\"ruby -h\"));" fullword ascii
      $s17 = "$buff = execute(\"lynx -source \".$url.\" > \".$saveas);" fullword ascii
      $s18 = "$check = strtolower(execute(\"python -h\"));" fullword ascii
      $s19 = "$check = strtolower(execute(\"gcc --help\"));" fullword ascii
      $s20 = "$check = strtolower(execute(\"perl -h\"));" fullword ascii
   condition:
      uint16(0) == 0x3f3c and filesize < 700KB and
      1 of ($x*) and 4 of them
}

rule loki_thm_yara_2022_07_01_02_29_12 {
   meta:
      description = "file2 - file loki_thm-yara_2022-07-01_02-29-12.log"
      author = "yarGen Rule Generator"
      reference = "https://github.com/Neo23x0/yarGen"
      date = "2022-07-01"
      hash1 = "a5d3f598ad7844d5b82c5aee7678bb8a49f3fc82be2c5bc6f3a919b92f04e6f1"
   strings:
      $s1 = "20220701T02:29:12Z thm-yara LOKI: Notice: MODULE: PESieve MESSAGE: PE-Sieve successfully initialized BINARY: /home/cmnatic/tools" ascii
      $s2 = "20220701T02:29:16Z thm-yara LOKI: Info: MODULE: Results MESSAGE: Please report false positives via https://github.com/Neo23x0/si" ascii
      $s3 = "/Loki/tools/pe-sieve64.exe SOURCE: https://github.com/hasherezade/pe-sieve" fullword ascii
      $s4 = "20220701T02:29:16Z thm-yara LOKI: Info: MODULE: Results MESSAGE: Please report false positives via https://github.com/Neo23x0/si" ascii
      $s5 = "20220701T02:29:14Z thm-yara LOKI: Info: MODULE: Init MESSAGE: Processing YARA rules folder /home/cmnatic/tools/Loki/signature-ba" ascii
      $s6 = "20220701T02:29:14Z thm-yara LOKI: Info: MODULE: Init MESSAGE: Processing YARA rules folder /home/cmnatic/tools/Loki/signature-ba" ascii
      $s7 = "20220701T02:29:16Z thm-yara LOKI: Notice: MODULE: Init MESSAGE: Program should be run as 'root' to ensure all access rights to p" ascii
      $s8 = "20220701T02:29:14Z thm-yara LOKI: Info: MODULE: Init MESSAGE: Malicious SHA1 Hashes initialized with 7159 hashes" fullword ascii
      $s9 = "20220701T02:29:14Z thm-yara LOKI: Info: MODULE: Init MESSAGE: Malicious SHA256 Hashes initialized with 22841 hashes" fullword ascii
      $s10 = "20220701T02:29:12Z thm-yara LOKI: Notice: MODULE: Init MESSAGE: Starting Loki Scan VERSION: 0.32.1 SYSTEM: thm-yara TIME: 202207" ascii
      $s11 = "20220701T02:29:12Z thm-yara LOKI: Notice: MODULE: PESieve MESSAGE: PE-Sieve successfully initialized BINARY: /home/cmnatic/tools" ascii
      $s12 = "20220701T02:29:14Z thm-yara LOKI: Info: MODULE: Init MESSAGE: Malicious MD5 Hashes initialized with 19034 hashes" fullword ascii
      $s13 = "20220701T02:29:14Z thm-yara LOKI: Info: MODULE: Init MESSAGE: False Positive Hashes initialized with 30 hashes" fullword ascii
      $s14 = "20220701T02:29:16Z thm-yara LOKI: Notice: MODULE: Results MESSAGE: Finished LOKI Scan SYSTEM: thm-yara TIME: 20220701T02:29:16Z" fullword ascii
      $s15 = "20220701T02:29:12Z thm-yara LOKI: Notice: MODULE: Init MESSAGE: Loaded plugin /home/cmnatic/tools/Loki/plugins/loki-plugin-wmi.p" ascii
      $s16 = "20220701T02:29:12Z thm-yara LOKI: Notice: MODULE: Init MESSAGE: Loaded plugin /home/cmnatic/tools/Loki/plugins/loki-plugin-wmi.p" ascii
      $s17 = "20220701T02:29:16Z thm-yara LOKI: Result: MODULE: Results MESSAGE: SYSTEM SEEMS TO BE CLEAN." fullword ascii
      $s18 = "20220701T02:29:16Z thm-yara LOKI: Notice: MODULE: Init MESSAGE: Finished running plugin PluginWMI" fullword ascii
      $s19 = "20220701T02:29:15Z thm-yara LOKI: Info: MODULE: Init MESSAGE: Initializing all YARA rules at once (composed string of all rule f" ascii
      $s20 = "20220701T02:29:16Z thm-yara LOKI: Notice: MODULE: Init MESSAGE: Running plugin PluginWMI" fullword ascii
   condition:
      uint16(0) == 0x3032 and filesize < 7KB and
      8 of them
}

/* Super Rules ------------------------------------------------------------- */


```
