# RabbitMQ and Mosquitto

What is Mosquitto? An open source message broker that implements the MQTT protocol. It is lightweight and is suitable for use on all devices from low power single board computers to full servers.. The MQTT protocol provides a lightweight method of carrying out messaging using a publish/subscribe model. This makes it suitable for Internet of Things messaging such as with low power sensors or mobile devices such as phones, embedded computers or microcontrollers.

What is RabbitMQ? A messaging broker - an intermediary for messaging. RabbitMQ gives your applications a common platform to send and receive messages, and your messages a safe place to live until received.


## Lack of TLS Authentication in MQTT server

- Your company is launching a new line of industrial automation devices, and you are in charge of securing the MQTT messaging channel that the fleet of IoT devices will use. 
- Show the engineers how trivially a well-positioned attacker could eavesdrop on the devices' communications. 
- Then, show the now stunned team how enforcing mutual authentication via TLS client certificates could secure the communication between the devices and the back-end systems.

## Run Nmap & Observe the unencrypted MQTT server wide open
- `1883/tcp open mqtt`

## Use tcpdump & tshark to monitor the traffic
- `ssh sfadmin@server.secureflag sudo tcpdump -i ens5 -U -s0 -w - 'port 1883' | tshark -r - -T fields -e mqtt.username -e mqtt.passwd -Y mqtt.passwd`
- Obtain the username & password
- Then use `mosquito_sub`, a MQTT client to connect to the server and use a multi-level topic wildcard to unwarrantedly read any message published on any topic.
`mosquito_sub -h server.secureflag -p 1883 -u fleet -P queen9ah019 -t /#`
- # is the multi-level topic wildcard, / denotes the hierarchy of the topics
- for your reference, http://www.steves-internet-guide.com/understanding-mqtt-topics/


## Remediate
- Only the clients that present a valid TLS certificate signed by a CA should be allowed to connect to the service.
- The following are the instructions

- The first step when setting up an encrypted TLS service is to generate the private key and certificate for the server.

- Open a new terminal and type the following command to create the signed certificates.

`sf-gen-sign-cert server.secureflag`

- Then, securely copy the newly created certs directory into the "sfadmin" home directory on the remote server.

`scp -r certs sfadmin@server.secureflag:~/`

- Now type ssh `sfadmin@server.secureflag` to connect to the remote server.

- You're logged in as the administrative user "sfadmin". Type `sudo -s` to gain root access.

- You can now use nano or vi to edit the Mosquitto configuration file `/etc/mosquitto/mosquitto.conf`.

- Comment out the allow_anonymous and password_file directives that were used to enforce the password-based authentication.

- Add the port directive to open 8883, used for MQTT encrypted communications.

- Add the cafile /usr/share/pki/ca-trust-source/anchors/cacert.pem directive to load the root CA certificate.

- Set up the private key and certificate files to point to the server certificates you uploaded. It is recommended to move the certificate and the key file to a more appropriate system directory (e.g. /etc/mosquitto/certs/) and to refer to the new paths accordingly.

- Finally, enable the certificate request setting require_certificate and set the use_identity_as_username directives to true.

- Restart the Mosquitto daemon to apply your changes:

- `systemctl restart mosquitto`

- Now, let's generate the private key and certificate for the clients.

- Open a new terminal and type the following command to create the signed certificates for the clients.

- sf-gen-sign-cert device-1
Now verify whether the client certificate, private key, and CA certificate correctly authenticate to the remote, encrypted MQTT, and start listening to the passing messages.

```
mosquitto_pub \
   -h server.secureflag \
   -p 8883 \
   --cert certs/device-1-cert.pem \
   --key certs/device-1-key.pem \
   --cafile /home/sf/.sf/ca/cacert.pem \
   -t '/test' \
   -m '{"msg":"test"}'
```

If everything has been set correctly, the command should exit without any print.

- You can create many other certificates with sf-gen-sign-cert and then emulate a multi-device fleet by running the test-mqtt-mutual-tls.sh tool in your home folder.

- Press Continue to test your solution's validity. Optionally, retry the hack prior to continuing to prove the attack is no longer feasible.
