# Upload Vulns

- The file uploading feature on websites if handled bandly can cause a lot of serious issues.
- This can lead to the following
  - relatively minor, nuisance problems
  - or could go all the way upto full remote code execution
  - with unrestricted upload access to the server, an attacker could deface and alter existing content & upto including malicious web pages which may lead to XSS and CSRF
  - by uploading the arbitrary files, an attacker could potentially also use the server to host and/or serve illegal content or leak sensitive info.
  - an attacker with the ability to upload file of their choice is a dangerous proposition.

The purpose of this room is to handle vuls that resulted as part of improper handling of file uploads.
- overwriting existing files on the server
- uploading & executing shells on a server
- by pass client-side filtering
- by pass various kinds of server-side filtering
- fooling content type validation checks


## General Methodology
- If you find a website with file upload feature, try to look at the source code & see if there is any client side filtering being applied.
- Scanning the website with dir mode with tool like gobuster will give a sense of where the files are being uploaded to.
- Intercepting requests with burpsuite is also another way to see where the files are going.
- Browser extensions such as `Wapanalyzer` can provide valuable information about the website.
- We need to see how the website is handling our input, and what kind of inputs are allowed & dis-allowed.
- if the website has client-side filtering then we can easily look at the code & try to bypass it.
- if the website has server-side filtering then we need to see what kind of errors we get & try to bypass it.

## Upload Vulns - Methodologies
- see if you can overwrite the existing files
- Remote code execution through a web application tends to be a result of uploading a program written in the same language as the back-end of the website.
  - Traditionally this would have been PHP, however in more recent times there are other common languages like python.
  - Two ways to achieve a RCE on a webserver - web shells or reverse shells
  - A simple webshell works by taking a parameter & executing a system command. `<?php echo system($_GET["cmd"]); ?>`.
```
http://shell.uploadvulns.thm/resources/shell.php?cmd=id;whoami;pwd
```
- 
