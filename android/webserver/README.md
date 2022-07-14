# Host a Web Server on Android

## Install Termux and Hacker's Keyboard
- Go to Playstore and find the above apps & Install them
- Termux from `Fredrik Fornwall`
- Hacker's Keyboard from `Klaus Weidner`
- Or Download F-Droid from your chrome browser & install termux from there
- `termux-change-repo` if required and select a mirror

## Install packages on Termux
```
pkg update && pkg upgrade
pkg install apache2 git neovim wget curl
```

## Connect to Android via SSH
```
pkg install openssh neofetch fish nmap

# enable ssh
sshd

whoami
u0_a288

ifconfig wlan0

# find out which port ssh service is running
nmap -sV 127.0.0.1

# From your PC
ssh -p 8022 u0_a288@192.168.0.106

# change default shell
chsh /data/data/com.termux/files/usr/bin/fish
```

## Start the webserver on Android
```
apachectl

# access web server from your pc
http://<ip-address>:8080

vi ${PREFIX}/share/apache2/default-site/htdocs/index.html
<html><body>
<h1>My Google Pixel 4a 5G</h1>
</body></html>
```

## Port forwarding with Ngrok
```
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm64.tgz
tar -xvzf ngrok-stable-linux-arm64.tgz

# sign up on ngrok website to get an auth token
./ngrok authtoken <token>

# now you have acces to more features and longer sessions. Finally with our webserver still running, type:
./ngrok http 8080

# you get a ngrok link, where we would find our webserver's homepage:
# now you can access the web server from outside our local network using the ngrok link!
```

Thus in this way we can use our Android phones as web servers. On non-rooted phones, you can host a webserver on any of the higher ports while on rooted phones
you can use the default port 80.

## References
- [Host a WebServer on Android](https://www.journaldev.com/49290/host-a-web-server-on-android)
