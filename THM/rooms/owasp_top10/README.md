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


Below is an XML document that uses.
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

As we can see we are defining a ENTITY called `name` & assiging it a value called `feast`.
Later we are using ENTITY in our code.

We can also use XXE to read some sensitive file by defining an ENTITY & having it use the SYSTEM keyword.

```
<?xml version="1.0"?>
<!DOCTYPE root [<!ENTITY read SYSTEM 'file:///etc/passwd'>]>
<root>&read;</root>

```
we are defining an ENTITY with the name `read` but the difference is we are setting it to value `SYSTEM` & path of the file.

If we use this payload, then a website vulnerable to XXE would display the contents of the file `/etc/passwd`

In a similar manner, you can read other files 
