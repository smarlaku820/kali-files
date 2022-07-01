# condition states if hello_world occurences with in a file/directory are less than 10.
rule helloworld_checker {
     strings:
             $hello_world = "Hello World!"
     condition:
             $hello_world < 10
}
