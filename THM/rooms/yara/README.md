# YARA

"The pattern matching swiss knife for malware researchers (and everyone else)" (Virustotal., 2020)

YARA is a tool aimed at (but not limited to) helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families (or whatever you want to describe) based on textual or binary patterns. Each description, a.k.a. rule, consists of a set of strings and a boolean expression which determine its logic. Let's see an example:

```
rule silent_banker : banker
{
    meta:
        description = "This is just an example"
        threat_level = 3
        in_the_wild = true

    strings:
        $a = {6A 40 68 00 30 00 00 6A 14 8D 91}
        $b = {8D 4D B0 2B C1 83 C0 27 99 6A 4E 59 F7 F9}
        $c = "UVODFRYSIHLNWPEJXQZAKCBGMT"

    condition:
        $a or $b or $c
}
```

The above rule is telling YARA that any file containing one of the three strings must be reported as *silent_banker*. This is just a sample example, more complex and powerful rules can be created by using wild-cards, case-insensitive strings, regular expressions, special operators and many other features that you will find explained in [Yara's Documentation](https://yara.readthedocs.io/en/stable/) 

## LOKI
- Indicator of Compromise (IOC) scanner

## Virus Total & Valhalla
- https://valhalla.nextron-systems.com/
- https://www.virustotal.com/gui/home/upload

## References
- https://github.com/virustotal/yara
- https://github.com/InQuest/awesome-yara
- https://github.com/Neo23x0/Loki/releases
- https://www.nextron-systems.com/thor-lite/
- https://github.com/Neo23x0/Fenrir
- https://www.bsk-consulting.de/2015/02/16/write-simple-sound-yara-rules/
- https://www.bsk-consulting.de/2015/10/17/how-to-write-simple-but-sound-yara-rules-part-2/
- https://www.bsk-consulting.de/2016/04/15/how-to-write-simple-but-sound-yara-rules-part-3/

