rule helloworld_checker {
     strings:
             $hello_world = "Hello World!"
     condition:
             $hello_world
}
