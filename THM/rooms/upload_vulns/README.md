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
http://shell.uploadvulns.thm/resources/pentest_monkey.php
```
## Filtering
- Client-Side filtering: Scripts executed on your browser. This is not difficult to bypass.
- Server-Side filtering: Scripts executed on the web server.Traditionally, PHP was a server-side language.This is more difficult to bypass. Instead we have to form a payload which conforms to the filters in place, but still allows us execute our code.

### Extension Validation:
- File extensions are used to identify the contents of a file.Windows does that.
- There are blacklist extensions & whitelist extensions

### File type filtering
- In this the contents of the file are examined & verified.
- In this we are looking at two types of validation
  - MIME validation 
    - MIME types are identifiers for files 
    - originally when transfered as attachments over email, but now when files are being transferred over HTTP(s).
    - the MIME type for a file upload is attached in the header of the request and looks something like this.`Content-Type: image/jpeg`
    - they follow the convention - `<type>/<sub-type>`
    - The MIME type for a file can be checked client-side or server-side.
  - Magic Number Validation
    - the "magic number" of the file is a string of bytes at the beginning of the file content.
- Unix systems uses magic number to validate the file type. This is not a perfect solution but it is better than checking the file extensions.

### File length filtering
- this prevents from huge files being uploaded to the server via a upload form
- there won't be any problem when we upload shells.
- if there are restrictions on the file length to be of certain size, then our shell should satisfy that min file length requirement.

### File name filtering
- don't allow duplicate file names by appending a random string to the name of the file
- or throw an error by ensuring if that file name already exists on the server
- additionally ensure that the file names do not contain any bad characters as they can cause problems on the file system.
- for example NULL BYTES or forward slashes on linux as well as control characters `;` and potentially unicode characters.

### File Content filtering
- more complicated file filtering systems may even scan the uploaded content to ensure that its not ensuring its spoofing its extension.
- this is a more complex & significant process.

these filtering techniques are applied as a multi-layer, thus increasing the security of the upload significantly. Any of these filters are applied either at client-side or server-side or both. it also depends on the language.for example, until PHP version 5, it was possible to bypass an extension filter by appending a null byte followed by a malicious extension `.php` file. most recently it is also possible to inject php code into an exif data of an otherwise valid image file, then force the server to execute it.

## client-side filtering
- there are four easy ways to bypass an average client side upload filter
  - Turn off javascript in your browser
  - Intercept & modify the incoming page.
  - Intercept & modify the file upload.
  - Send the file directly to the upload point. (`curl -X POST -F "submit:<value>" -F "<file-parameter>:@<path-to-file>" <site>`)
- use burpsuite to remove any client-side filterning java scripts
- or upload a legitimate extension, but before clicking the upload button change the file name & MIME type to the one's you desired(Content-Type: text/x-php) & filename as follows - (filename renaming from shell.png to shell.php)

## server-side filtering

- We can see that the code is filtering out the .php and .phtml extensions, so if we want to upload a PHP script we're going to have to find another extension. 
- The wikipedia page for PHP gives us a few common extensions that we can try; however, there are actually a variety of other more rarely used extensions available that webservers may nonetheless still recognise. 
- These include: .php3, .php4, .php5, .php7, .phps, .php-s, .pht and .phar. 
- Many of these bypass the filter (which only blocks.php and .phtml), but it appears that the server is configured not to recognise them as PHP files, as in the below example & evenutually we may find that .phar extension could be allowed.
- This is by no means an exhaustive list of upload vulnerabilities related to file extensions. 
- As with everything in hacking, we are looking to exploit flaws in code that others have written; this code may very well be uniquely written for the task at hand. 
- This is the really important point to take away from this task: **there are a million different ways to implement the same feature when it comes to programming -- your exploitation must be tailored to the filter at hand. The key to bypassing any kind of server side filter is to enumerate and see what is allowed, as well as what is blocked; then try to craft a payload which can pass the criteria the filter is looking for.**

# server-side filtering - magic number filtering

- as mentioned earlier, magic numbers are used as a more accurage identifier of the files. The magic number of a file is a string of hex digits & is always the very first thing in the file.
- knowing this it is useful to validate magic numbers during file uploads.
- so, the technique is by simply by reading those first few bytes & crossing them through a whitelist or blacklist.
- R1ckRul3s
