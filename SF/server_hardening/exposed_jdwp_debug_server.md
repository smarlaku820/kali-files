# Exposed JDWP

The company you work for runs an internal java app to manage the day-to-day tasks. However, due to the way the service running the app has been created, it dangerously exposes the Java Debug Wire Protocol (JDWP) protocol to the network allowing an attacker to gain entry. Reproduce how an attacker could have easily exploited this oversight to achieve remote command execution. Once you've nailed down how an attack would work, come up with an adequate solution to fix the shoddy configuration as soon as possible.


## Mimic An Attacker & Gain RCE

After you have located the JDWP server, mimic an attacker and gain remote code execution.

Instructions
- As Java debug servers are often left open by this organization's development team, switch to the terminal and use Nmap to scan the ports and see if anything of use is open.

- `nmap --script=+jdwp-version server.secureflag`
Observe that a JDWP service is running on port 8080, which is wide open and exposed on the network.

- Now mimic an attacker and exploit the service to gain remote command execution by using the provided attack tool with the following options:

- `./jdwp-shellifier.py -t server.secureflag -p 8080 --break-on='Java.lang.String.indexOf'`
Review the response, which provides system information.

- Finally, run the command above again, but this time with the --cmd flag to create the file PWND.txt in the /home/sfadmin directory. Use the command below to verify it has been created:

`ssh sfadmin@server.secureflag ls -al PWND.txt`

- Observe that an attacker could exploit this vulnerability to execute commands and ultimately compromise the underlying operating system.
