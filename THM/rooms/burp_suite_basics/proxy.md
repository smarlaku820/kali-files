# Burp Suite Proxy

## Introduction
- Burp Proxy is most fundamental and most important of the tools available in Burp Suite.
- It will allow us to capture requests and responses between ourselves and our target.
- These can be manipulated or sent to other tools for further processing before being allowed to continue to their destination.
- Install the foxyproxy extension and specify the burp suite proxy server which usually by default runs at (http://127.0.0.1:8080)
- Get the certs from portswigger & install it on your firefox (preferences -> search for "certificates" -> Import -> Trust this CA to identify websites)

## The Burp Suite Browser
- You can launch your own embedded browser. A chromium window will now pop up. Any requests we make in this will go through the proxy.
- If we are running on Linux as the root user, Burp Suite is unable to create a sandbox environment to start the Burp Browser in, causing it to throw an error & die.
- Solutions
  - The smart option: We could create a new user and run burp suite under a low privlege account.
  - The easy option: We could go to `Project options -> Misc -> Embedded Browser` & Check `Allow the embedded browser to run without a sandbox` option.
  - Checking this option will allow the browser to start, but be aware that it is disabled by default for security reasons.
  - If we get compromised using the browser, then an attacker will have access to our entire machine.

## Scoping and Targeting
- One of the most important parts of using the Burp Proxy: Scoping
- In short, allowing Burp to capture everything can quickly become as massive pain.
- What's the solution ? Scoping
- Setting a scope for the project allows us to define what gets proxied and logged. We can restrict Burp Suite to only target the web application(s) that we want to test.
- The easiest way to do this by switching over the "Target" Tab, right-clicking our target from our list on the left, then choosing "Add to Scope".
- Burp will then ask us if we want to stop logging anything which isn't in scope - most of the time we want to choose "yes" here.
- We just chose to disable logging for out of scope traffic, but the proxy will still be intercepting everything. To turn this off, we need to go into the Proxy Options sub-tab and select `And URL Is in target scope` from the intercept client requests section.

## Site Map & Issue Definitions
- There are three sub-tabs under Target:
- Site Maps
  - Site map allows us to map out the apps we are targeting in a tree structure.Every page we visit will show up here, allowing us to automatically generate a site map for the target by simply browsing around the web app.
  - Burp Pro would also allow us to spider the targets automatically (i.e., look through every page for links and use them to map out as much of the site as-is publicly accessible using the links between pages); however, with Burp community, we can still use this to accumulate data whilst we perform our initial enumeration steps.
  - The Site map can be especially useful if we want to map out an API, as whenever we visit a page, any API endpoints that the page retrieves data from whilst loading will show up here.
- Scope
  - It allows us to control Burp's target scope for this project. As we have seen in Scoping & targeting in the previous section
- Issue Definitions
  - Whilst we don't have access to Burp Suite Vuln scanner in Burp Community, we do still have access to a list of all vulns it looks for.
  - The issue definitions section gives us a huge list of web vulns (complete with descriptions and references) which we can draw from should we need citations for report or help describing a vulnerability

## Practical Example Attack
- In a real-world web app pentest, we would test this for a variety of things: One of which would be Cross-Site Scripting (or XSS). If you have not yet encountered XSS, it can thought of as injecting a client-side script (usually in Javascript) into a webpage in such a way that it executes.
- There are various kinds of XSS - the type that we are using here is referred to as "Reflected" XSS as it only affects the person making the web request.
- Lets Begin
  - Try typing: `<script>alert("Succ3ssful XSS")</script>` into the Contact Email field. You should find that there is a client-side filter in place which prevents you from adding any special characters that aren't allowed in email addresses.
  - Fortunately for us, since this is a client-side filter, it is absurdly easy to bypass. There are a variety of ways we could disable the script or just prevent it from loading in the first place.
  - After submitting, modify the email parameter from Proxy & Press Cntrl+U to url encode
  - this will be a successful XSS attack. 
