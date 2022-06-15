# Burp Suite Intruder

## Sniper Attack
- One Payload Set -> Single file containing a wordlist or a list of numbers
- If there are 2 positions & 3 words, then there will be 6 sniper attack requests
- no.of.requests = no.of.positions * no.of.words
- intruder starts with first position, goes through will all possible list of items and then goes to the second position & so on...
- It is good for attacks where we are attacking only a single parameter 

```
payload: burp, suite, intruder 
request positions: username=§pentester§&password=§Expl01ted§              

Sniper Attack:-
username=burp&password=Expl01ted
username=suite&password=Expl01ted
username=intruder&password=Expl01ted
username=pentester&password=burp
username=pentester&password=suite
username=pentester&password=intruder

```

## Battering Ram Attack
- One Payload Set
- Unlike sniper, Battering RAM attack puts the same payload across all the positions (or parameters) rather than each position in turn.

```
payload: burp, suite, intruder
request positions: username=§pentester§&password=§Expl01ted§              

Battering Ram Attack:-
username=burp&password=burp
username=suite&password=suite
username=intruder&password=intruder

```

## Pitch Fork Attack
- Most likely to use attack
- Numerous snipers running simultaneously
- Pitchfork uses one payload set per one position (Upto a 20) & run through all of them
- Pitchfork takes an item from each list and puts it into their corresponding positions. Payload sets should be identical lengths when using Pitchfork attack.
- If you have two payload sets one with 100 lines & other with 90 lines, intruder will be able to make only 90 requests if pitch fork attack is used.
- Exceptionally useful when performing credential stuffing attacks.

```
first wordlist: joel, harjeet, alex
second wordlist: j03l, Emma123, Sk1ll

username=joel&password=j03l
username=harjeet&password=Emma123
username=alex&password=Sk1ll

```

## Cluser Bomb
- Multiple payload sets or lists can be used like pitch fork attack
- While pitchfork iterates through each payload set simultaneously, cluster bomb will iterate through each payload set individually, making sure that every possible combination of payloads is tested.
- Cluster Bomb will iterate through every combination of provided payload sets to ensure that every possibility has been tested. 
- This type of attack can create a huge-amount of network traffic.
- Burp usually is rate-limiting and therefore this can usually take longer time of the payload sets are large.


