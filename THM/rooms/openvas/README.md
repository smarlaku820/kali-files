# Open Vulnerability Assessment Scanner (Open VAS)

```
sudo apt-get install docker.io
docker run -d -p 443:443 --name openvas mikesplain/openvas

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install gvm*
sudo gvm-setup

[*] Creating extension pgcrypto
CREATE EXTENSION
[>] Migrating database
[>] Checking for GVM admin user
[*] Creating user admin for gvm
[*] Please note the generated admin password
[*] User created with password 'fe844efe-fda0-4809-bdd8-fca67a77ef6f'.
[*] Define Feed Import Owner
[>] Updating GVM feeds
[*] Updating NVT (Network Vulnerability Tests feed from Greenbone Security Feed/Community Feed)
Greenbone community feed server - http://feed.community.greenbone.net/
This service is hosted by Greenbone Networks - http://www.greenbone.net/


sudo gvm-start



└─$ sudo gvm-start
[sudo] password for bluejay820: 
[>] Please wait for the GVM services to start.
[>]
[>] You might need to refresh your browser once it opens.
[>]
[>]  Web UI (Greenbone Security Assistant): https://127.0.0.1:9392

● gsad.service - Greenbone Security Assistant daemon (gsad)
     Loaded: loaded (/lib/systemd/system/gsad.service; disabled; vendor preset: disabled)
     Active: active (running) since Sun 2022-07-03 03:28:57 IST; 6ms ago
       Docs: man:gsad(8)
             https://www.greenbone.net
    Process: 2029 ExecStart=/usr/sbin/gsad --listen 127.0.0.1 --port 9392 (code=exited, status=0/SUCCESS)
   Main PID: 2031 (gsad)
      Tasks: 3 (limit: 4540)
     Memory: 3.0M
        CPU: 11ms
     CGroup: /system.slice/gsad.service
             ├─2030 /usr/sbin/gsad --listen 127.0.0.1 --port 9392
             └─2031 /usr/sbin/gsad --listen 127.0.0.1 --port 9392

Jul 03 03:28:57 kali systemd[1]: Starting Greenbone Security Assistant daemon (gsad)...
Jul 03 03:28:57 kali gsad[2029]: Oops, secure memory pool already initialized
Jul 03 03:28:57 kali systemd[1]: gsad.service: Supervising process 2031 which is not our child. We'll most likely not notice when it exits.
Jul 03 03:28:57 kali systemd[1]: Started Greenbone Security Assistant daemon (gsad).

● gvmd.service - Greenbone Vulnerability Manager daemon (gvmd)
     Loaded: loaded (/lib/systemd/system/gvmd.service; disabled; vendor preset: disabled)
     Active: active (running) since Sun 2022-07-03 03:28:52 IST; 5s ago
       Docs: man:gvmd(8)
    Process: 1989 ExecStart=/usr/sbin/gvmd --osp-vt-update=/run/ospd/ospd.sock --listen-group=_gvm (code=exited, status=0/SUCCESS)
   Main PID: 1990 (gvmd)
      Tasks: 2 (limit: 4540)
     Memory: 8.4M
        CPU: 189ms
     CGroup: /system.slice/gvmd.service
             ├─1990 "gvmd: Waiting for incoming connections"
             └─2009 gpg-agent --homedir /var/lib/gvm/gvmd/gnupg --use-standard-socket --daemon

Jul 03 03:28:51 kali systemd[1]: Starting Greenbone Vulnerability Manager daemon (gvmd)...
Jul 03 03:28:51 kali systemd[1]: gvmd.service: Can't open PID file /run/gvmd/gvmd.pid (yet?) after start: Operation not permitted
Jul 03 03:28:52 kali systemd[1]: Started Greenbone Vulnerability Manager daemon (gvmd).

● ospd-openvas.service - OSPd Wrapper for the OpenVAS Scanner (ospd-openvas)
     Loaded: loaded (/lib/systemd/system/ospd-openvas.service; disabled; vendor preset: disabled)
     Active: active (running) since Sun 2022-07-03 03:28:49 IST; 7s ago
       Docs: man:ospd-openvas(8)
             man:openvas(8)
    Process: 1958 ExecStart=/usr/bin/ospd-openvas --config /etc/gvm/ospd-openvas.conf --log-config /etc/gvm/ospd-logging.conf (code=exited, status=0/SUCCESS)
   Main PID: 1971 (ospd-openvas)
      Tasks: 4 (limit: 4540)
     Memory: 28.9M
        CPU: 147ms
     CGroup: /system.slice/ospd-openvas.service
             ├─1971 /usr/bin/python3 /usr/bin/ospd-openvas --config /etc/gvm/ospd-openvas.conf --log-config /etc/gvm/ospd-logging.conf
             └─1973 /usr/bin/python3 /usr/bin/ospd-openvas --config /etc/gvm/ospd-openvas.conf --log-config /etc/gvm/ospd-logging.conf

Jul 03 03:28:49 kali systemd[1]: Starting OSPd Wrapper for the OpenVAS Scanner (ospd-openvas)...
Jul 03 03:28:49 kali systemd[1]: Started OSPd Wrapper for the OpenVAS Scanner (ospd-openvas).

[>] Opening Web UI (https://127.0.0.1:9392) in: 5... 4... 3... 2... 1...

sudo gvm-check-setup

sudo -u _gvm -- greenbone-feed-sync --type SCAP

└─$ sudo -u _gvm -- greenbone-feed-sync --type SCAP
Greenbone community feed server - http://feed.community.greenbone.net/
This service is hosted by Greenbone Networks - http://www.greenbone.net/

All transactions are logged.

If you have any questions, please use the Greenbone community portal. 
See https://community.greenbone.net for details.

By using this service you agree to our terms and conditions.

Only one sync per time, otherwise the source ip will be temporarily blocked.

receiving incremental file list
timestamp
             13 100%   12.70kB/s    0:00:00 (xfr#1, to-chk=0/1)

sent 43 bytes  received 109 bytes  43.43 bytes/sec
total size is 13  speedup is 0.09
Greenbone community feed server - http://feed.community.greenbone.net/
This service is hosted by Greenbone Networks - http://www.greenbone.net/

All transactions are logged.

If you have any questions, please use the Greenbone community portal. 
See https://community.greenbone.net for details.

By using this service you agree to our terms and conditions.

Only one sync per time, otherwise the source ip will be temporarily blocked.

receiving incremental file list
./
nvdcve-2.0-2009.xml
     21,208,238 100%    2.53MB/s    0:00:08 (xfr#1, to-chk=35/45)
nvdcve-2.0-2010.xml
     22,010,196 100%  971.85kB/s    0:00:22 (xfr#2, to-chk=34/45)
nvdcve-2.0-2011.xml
     21,338,797 100%  969.74kB/s    0:00:21 (xfr#3, to-chk=33/45)
nvdcve-2.0-2012.xml
     24,736,568 100%  999.83kB/s    0:00:24 (xfr#4, to-chk=32/45)
nvdcve-2.0-2013.xml
     27,685,294 100%  978.27kB/s    0:00:27 (xfr#5, to-chk=31/45)
nvdcve-2.0-2014.xml
     28,343,879 100%  996.99kB/s    0:00:27 (xfr#6, to-chk=30/45)
nvdcve-2.0-2015.xml
     27,800,011 100%  995.76kB/s    0:00:27 (xfr#7, to-chk=29/45)
nvdcve-2.0-2016.xml
     37,652,116 100%  983.67kB/s    0:00:37 (xfr#8, to-chk=28/45)
nvdcve-2.0-2017.xml
     52,798,906 100%  992.31kB/s    0:00:51 (xfr#9, to-chk=27/45)
nvdcve-2.0-2018.xml
     53,341,385 100%  982.98kB/s    0:00:52 (xfr#10, to-chk=26/45)
nvdcve-2.0-2019.xml
     54,229,459 100%  987.75kB/s    0:00:53 (xfr#11, to-chk=25/45)
nvdcve-2.0-2020.xml
     64,370,048 100%  992.84kB/s    0:01:03 (xfr#12, to-chk=24/45)
nvdcve-2.0-2021.xml
     69,412,497 100%  988.65kB/s    0:01:08 (xfr#13, to-chk=23/45)
nvdcve-2.0-2022.xml
     25,669,962 100% 1000.41kB/s    0:00:25 (xfr#14, to-chk=22/45)
official-cpe-dictionary_v2.2.xml
    394,438,338 100%  999.14kB/s    0:06:25 (xfr#15, to-chk=21/45)
sha256sums
          3,012 100%    4.56kB/s    0:00:00 (xfr#16, to-chk=20/45)
sha256sums.asc
            833 100%    1.04kB/s    0:00:00 (xfr#17, to-chk=19/45)
timestamp
             13 100%    0.02kB/s    0:00:00 (xfr#18, to-chk=18/45)
oval/5.10/org.mitre.oval/c/oval.xml
        268,150 100%  251.07kB/s    0:00:01 (xfr#19, to-chk=9/45)
oval/5.10/org.mitre.oval/i/oval.xml
      9,480,204 100% 1004.23kB/s    0:00:09 (xfr#20, to-chk=8/45)
oval/5.10/org.mitre.oval/m/oval.xml
        143,834 100%    1.33MB/s    0:00:00 (xfr#21, to-chk=7/45)
oval/5.10/org.mitre.oval/p/oval.xml
     90,911,155 100%  998.72kB/s    0:01:28 (xfr#22, to-chk=6/45)
oval/5.10/org.mitre.oval/v/family/ios.xml
      2,012,118 100%  706.57kB/s    0:00:02 (xfr#23, to-chk=4/45)
oval/5.10/org.mitre.oval/v/family/macos.xml
        453,775 100%  390.43kB/s    0:00:01 (xfr#24, to-chk=3/45)
oval/5.10/org.mitre.oval/v/family/pixos.xml
         10,014 100%   75.23kB/s    0:00:00 (xfr#25, to-chk=2/45)
oval/5.10/org.mitre.oval/v/family/unix.xml
     31,372,831 100%  993.92kB/s    0:00:30 (xfr#26, to-chk=1/45)
oval/5.10/org.mitre.oval/v/family/windows.xml
     51,773,463 100%  994.90kB/s    0:00:50 (xfr#27, to-chk=0/45)

sent 24,529 bytes  received 1,096,939,332 bytes  1,018,063.91 bytes/sec
total size is 1,225,181,149  speedup is 1.12

─$ sudo -u _gvm -- greenbone-feed-sync --type CERT
Greenbone community feed server - http://feed.community.greenbone.net/
This service is hosted by Greenbone Networks - http://www.greenbone.net/

All transactions are logged.

If you have any questions, please use the Greenbone community portal. 
See https://community.greenbone.net for details.

By using this service you agree to our terms and conditions.

Only one sync per time, otherwise the source ip will be temporarily blocked.

receiving incremental file list
timestamp
             13 100%   12.70kB/s    0:00:00 (xfr#1, to-chk=0/1)

sent 43 bytes  received 109 bytes  33.78 bytes/sec
total size is 13  speedup is 0.09


```

