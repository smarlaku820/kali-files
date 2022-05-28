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
