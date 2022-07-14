# Install Kali on Android

## Install Apps
- F-Droid
- Termux
- Hackers KeyBoard

## Setting up our env
```
pkg update && pkg upgrade
termux-setup-storage
```

## Install kali
```
wget https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-project/raw/master/nethunter-rootless/install-nethunter-termux
chmod +x install-nethunter-termux
./install-nethunter-termux
```

## Launch kali
```
nethunter
```

## References
- [Kali on non-rooted android phone](https://www.journaldev.com/49329/install-kali-linux-non-rooted-android)
- [Termux Storage](https://wiki.termux.com/wiki/Termux-setup-storage)
- [Kali GUI](https://www.kali.org/docs/nethunter/nethunter-kex-manager/)
