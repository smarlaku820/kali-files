# Burp Suite Basics

## What is Burp Suite ?
- It is a framework written in java and a one-stop shop for web application penetration testing.
- It is also used when assessing mobile applications
- At the simplest level, burp suite can capture and manipulate all the traffic between an attacker and a webserver.
- After you capture the requests you can send it to various parts of the burp suite framework.
- This ability to intercept, view and modify web requests prior to being sent to the target web server (or in some cases the responses before they are received by our browser), makes burp suite perfect for any kind of manual web app testing.
- we use community edition
- Brup suite professional has additional features
  - An automated vuln scanner
  - A fuzzer/bruteforcer that isn't rate limited.
  - Saving projects for future use
  - A built-in API to allow integration of other tools.
  - Unrestricted access to add new extensions for greater functionality
  - Burp suite pro is costly priced at 400 USD per person
- Burp suite Enterprise is continously used for scanning. Just like how nessus performs infra scanning. this performs web app scanning.
  - And this sits on a dedicated server for scanning the web apps
- Burp suite scans web apps as well as mobile apps.

## Features of Burp Community

### Proxy
- Proxy allows you to intercept and modify requests/responses when interacting with web applications.

### Repeater
- Repeater allows you to capture, modify, then resend the same request numerous times.
- Very useful when we need to craft a payload through trial and error (Eg., A SQL injection attack) or when testing the functionality of an endpoint for flaws.

### Intruder
- Intruder allows us to spray and endpoint with requests.
- Often used for bruteforce attacks or to fuzz endpoints.

### Decoder
- Decoder is useful when transforming data.
- It could be either in terms of decoding captured information, or encoding a payload prior to sending it to the target.

### Comparer
- Allows us to compare two pieces of data at either word or byte level.
- Being able to send (potentially very large) pieces of data directly into a comparison tool with a single keyboard shortcut can speed things considerably.

### Sequencer
- When assessing the randomness of tokens such as session cookie values or other supposedly random generated data.
- If the algo is not generating secure random vals, then this could open up some devastating avenues for attack.

### Extender
- Extender can quickly and easily load extensions into the framework, as well as providing a marketplace to download 3rd party modules. (**BApp Store**)
- Many modules require professional license, but there are not modules that you cannot use without a license.
- For example, you may wish to extend the inbuilt logging functionality of Burp Suite with the `Logger++` module.

## Options for configuring Burp Suite

### User Options
- We can set a proxy for Burp Suite to connect through; this is very useful if we want to use Burp Suite through a network pivot.
- The TLS sub-tab allows us to enable and disable various TLS (Transport Layer Security) options, as well as giving us a place to upload client certs should a web app
require us to use one for connections
- An essential set of options to control display & font
- You can set hotkeys. Setting keybinds can speed up your workflow massively.

### Project options
- It is possible to set proxy for just the project, overriding any proxy settings that you set in the user options tab.
- How to handle unusual response codes.
- How can we handle sessions. It allows us to define, save and use session cookies that it receives from target sites.
- It can allow us to define macros which we can use to automate things such as logging into web apps

